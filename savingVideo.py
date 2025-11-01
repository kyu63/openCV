import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')  #create codec(COmpress  DECompress) code
recoder = cv2.VideoWriter("video.avi", codec, 30, (frame_width,frame_height))

while True:
    succuss, image = camera.read()
    if not succuss:
        print("you failed")
        break

    recoder.write(image)
    cv2.imshow("camera", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quitting")
        break

camera.release()
cv2.destroyAllWindows()
    
