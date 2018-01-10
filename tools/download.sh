pushd ../devdir
#wget hal-2018.1.1-beta-5-20171217230225-1-g166d9e0-linuxathena.zip --output-document=hal.zip
	wget http://first.wpi.edu/FRC/roborio/maven/development/edu/wpi/first/hal/hal/2018.1.1-beta-5-20171217230225-1-g166d9e0/hal-2018.1.1-beta-5-20171217230225-1-g166d9e0-linuxathena.zip --output-document=hal.zip
unzip hal.zip -d hal
wget http://www.ctr-electronics.com/downloads/lib/CTRE_Phoenix_FRCLibs_NON-WINDOWS_v5.1.3.1.zip --output-document=ctre.zip
unzip ctre.zip -d ctre
popd

