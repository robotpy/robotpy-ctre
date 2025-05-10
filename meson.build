project('robotpy-ctre', ['cpp'],
        default_options: ['warning_level=1', 'cpp_std=c++20',
                          'b_colorout=auto', 'optimization=2', 'b_pie=true'])

subdir('semiwrap')

phoenix5_sources += files(
    'phoenix5/ctre.cpp',
)

subdir('semiwrap/modules')
