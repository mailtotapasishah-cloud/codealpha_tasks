import cv2
from ultralytics import YOLO
from sort import Sort

model = YOLO("yolov8n.pt")
tracker = Sort()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    detections = []
    for r in results.boxes.data.tolist():
        x1,y1,x2,y2,conf,cls = r
        if conf > 0.4:
            detections.append([x1,y1,x2,y2,conf])

    tracked = tracker.update(detections)

    for obj in tracked:
        x1,y1,x2,y2,obj_id = obj
        x1,y1,x2,y2 = map(int, [x1,y1,x2,y2])

        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(frame, f"ID:{int(obj_id)}", (x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
