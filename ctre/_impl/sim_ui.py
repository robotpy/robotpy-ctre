
import tkinter as tk
from pyfrc.sim.ui_widgets import CheckButtonWrapper, Tooltip, ValueWidget

from hal_impl.data import hal_data
from .constants import TalonSRXConst as tsrxc

#from hal import TalonSRXConst as tsrxc

class CtreUI:
    
    can_mode_map = {
         tsrxc.kMode_CurrentCloseLoop: 'PercentVbus',
         tsrxc.kMode_DutyCycle:'PercentVbus',
         tsrxc.kMode_NoDrive:'Disabled',
         tsrxc.kMode_PositionCloseLoop:'Position',
         tsrxc.kMode_SlaveFollower:'Follower',
         tsrxc.kMode_VelocityCloseLoop:'Speed',
         tsrxc.kMode_VoltCompen:'Voltage'
    }
    
    def __init__(self):
        self.can = {}
    
    def update_tk_widgets(self, sim):
        
        for k, data in hal_data['CAN'].items():
            
            if data['type'] != 'talonsrx':
                continue
            
            if not data['sim_display']:
                self._add_CAN(sim, k, data)
                data['sim_display'] = True
           
            (motor, fl, rl, mode_lbl_txt, enc_txt, analog_txt, pwm_txt) = self.can[k]
            data = hal_data['CAN'][k]
            mode = data['mode_select']
            mode_lbl_txt.set(self.can_mode_map[mode])
            #change how output works based on control mode
            if   mode == tsrxc.kMode_DutyCycle :  
                #based on the fact that the vbus has 1023 steps
                motor.set_value(data['value']/1023)
                
            elif mode == tsrxc.kMode_VoltCompen:
                #assume voltage is 12 divide by muliplier in cantalon code (256)
                motor.set_value(data['value']/12/256)
                
            elif mode == tsrxc.kMode_SlaveFollower:
                #follow the value of the motor value is equal too
                try:
                    followed = self.can[data['value']]
                except KeyError:
                    value = 0
                else:
                    value = followed[0].get_value()
                
                motor.set_value(value)
            #
            # currently other control modes are not correctly implemented
            #
            else:
                motor.set_value(data['value'])
                
            enc_txt.set('E: %s' % data['enc_position'])
            analog_txt.set('A: %s' % data['analog_in_position'])
            pwm_txt.set('P: %s' % data['pulse_width_position'])
            
            ret = fl.sync_value(data['limit_switch_closed_for'])
            if ret is not None:
                data['limit_switch_closed_for'] = ret
                
            ret = rl.sync_value(data['limit_switch_closed_rev'])
            if ret is not None:
                data['limit_switch_closed_rev'] = ret 
    
    def _add_CAN(self, sim, canId, device):
        
        # TODO: this is not flexible
        
        row = len(self.can)*2
        
        lbl = tk.Label(sim.can_slot, text=str(canId))
        lbl.grid(column=0, row=row)
        
        motor = ValueWidget(sim.can_slot, default=0.0)
        motor.grid(column=1, row=row)
        sim.set_tooltip(motor, 'CAN', canId)
        
        fl = CheckButtonWrapper(sim.can_slot, text='F')
        fl.grid(column=2, row=row)
        
        rl = CheckButtonWrapper(sim.can_slot, text='R')
        rl.grid(column=3, row=row)
        
        Tooltip.create(fl, 'Forward limit switch')
        Tooltip.create(rl, 'Reverse limit switch')
        
        mode_lbl_txt = tk.StringVar(value = self.can_mode_map[device['mode_select']])
        mode_label = tk.Label(sim.can_slot, textvariable=mode_lbl_txt)
        mode_label.grid(column=4, row=row)
        
        labels = tk.Frame(sim.can_slot)
        labels.grid(column=0, row=row+1, columnspan=6)
        
        enc_value = tk.StringVar(value='E: 0')
        enc_label = tk.Label(labels, textvariable=enc_value)
        enc_label.pack(side=tk.LEFT)
        
        analog_value = tk.StringVar(value='A: 0')
        analog_label = tk.Label(labels, textvariable=analog_value)
        analog_label.pack(side=tk.LEFT)
        
        pwm_value = tk.StringVar(value='P: 0')
        pwm_label = tk.Label(labels, textvariable=pwm_value)
        pwm_label.pack(side=tk.LEFT)
        
        Tooltip.create(enc_label, "Encoder Input")
        Tooltip.create(analog_label, "Analog Input")
        Tooltip.create(pwm_label, "PWM Input")
        
        self.can[canId] = (motor, fl, rl, mode_lbl_txt, enc_value, analog_value, pwm_value)
        
        
