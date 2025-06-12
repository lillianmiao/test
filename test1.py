import cv2
import time
from lens import Lens

cap = cv2.VideoCapture(0)
lens = Lens(port="/dev/ttyACM0", debug=True)  
min_fp, max_fp = lens.to_focal_power_mode()
img_counter = 0

while True:
    ret, frame = cap.read()

    cv2.imshow('video feed',frame)

    key = cv2.waitKey(1) & 0xFF
    if not ret:
        print("Failed frame")
        break

    if key == ord('x'):
        break # Exit when 'x' is pressed

    elif key == ord('s'):
        # Save the frame when 's' is pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter += 1

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print("{} written at {}!".format(img_name, timestamp))

    elif key == ord('d'):
        try:
            new_diopter = float(input("Enter new diopter value: "))
            lens.set_diopter(new_diopter)
            print(f"Diopter set to {new_diopter}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

cap.release()
cv2.destroyAllWindows()

