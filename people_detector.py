from ultralytics import YOLO
import cv2
from datetime import datetime

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    # Get current date & time
    now = datetime.now()
    time_text = now.strftime("%H:%M:%S")
    date_text = now.strftime("%d-%m-%Y")

    # Run YOLO detection
    results = model(frame, conf=0.5)

    person_count = 0

    for r in results:
        for box in r.boxes:
            if int(box.cls[0]) == 0:  # person class
                person_count += 1

                # Draw bounding box
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display person count
    cv2.putText(frame, f"Persons: {person_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display time
    cv2.putText(frame, f"Time: {time_text}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Display date
    cv2.putText(frame, f"Date: {date_text}", (20, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Show output
    cv2.imshow("People Counter with Time & Date", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()