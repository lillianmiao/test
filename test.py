import time
import csv
from lens import Lens

class LensDataCollector:
    def __init__(self, lens, output_file="lens_data.csv"):
        
        self.lens = lens
        self.output_file = output_file

        with open(self.output_file, mode='w', newline='') as file: # write mode 
            writer = csv.writer(file)
            writer.writerow([
                "Timestamp", "Lens Serial", "Firmware Type", "Firmware Version",
                "Firmware Branch", "Device ID", "Max Output Current", 
                "Temperature", "Current", "Diopter", "Mode", 
            ])

    def collect_data(self):
        try:
            while True:
                # Gather data
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                lens_serial = self.lens.get_lens_serial_number()
                firmware_type = self.lens.get_firmware_type()
                firmware_version = self.lens.get_firmware_version()
                firmware_branch = self.lens.get_firmware_branch()
                device_id = self.lens.get_device_id()
                max_output_current = self.lens.get_max_output_current()
                temperature = self.lens.get_temperature()
                current = self.lens.get_current()
                diopter = self.lens.get_diopter()
                mode = self.lens.refresh_active_mode()

                # Write data to CSV
                with open(self.output_file, mode='a', newline='') as file: # append mode
                    writer = csv.writer(file)
                    writer.writerow([
                        timestamp, lens_serial, firmware_type, firmware_version,
                        firmware_branch, device_id, max_output_current, 
                        temperature, current, diopter, mode
                    ])    
    
                print(f"Data collected at {timestamp}")
                time.sleep(5)

        except KeyboardInterrupt:
            print("Data collection stopped.")

from test import LensDataCollector

lens = Lens(port="/dev/ttyACM0", debug=True) 

collector = LensDataCollector(lens, output_file="lens_data.csv")

collector.collect_data()