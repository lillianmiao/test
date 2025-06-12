from lens import Lens
import time

lens = Lens('/dev/ttyACM0', debug=False)  # set debug to True to see a serial communication log
print(lens.firmware_type)
print(lens.firmware_version)
print(lens.get_firmware_branch())
print('Lens serial number:', lens.lens_serial)
print('Lens temperature:', lens.get_temperature())

# focal power mode example
min_fp, max_fp = lens.to_focal_power_mode()
print('Minimal diopter:', min_fp)
print('Maximum diopter:', max_fp)
print(lens.set_temperature_limits(20,45 ))
lens.set_diopter(3)
lens.set_diopter(-0.2)


import random
num_values = 5
min_diopter = 0
max_diopter = 15.0

for _ in range(num_values):
    diopter = random.uniform(min_diopter, max_diopter)
    lens.set_diopter(diopter)
    time.sleep(1)  # Wait for 1 second to allow the lens to adjust
    diopter = lens.get_diopter()
    print(diopter)


