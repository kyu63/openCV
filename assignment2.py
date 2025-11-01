import cv2
camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recoder = cv2.VideoWriter("video2.avi",codec, 30, (frame_width,frame_height))
print("<-----Choose Option----->")
print("1. take photo")
print("2. Make video")
print("3. Exit/Quit")

while True:
    choice = int(input("enter option : "))
    match choice:
        case 1:
            succuss , frame = camera.read()
            if not succuss:
                print("could not load")
            else:
                cv2.imshow("image" , frame)
                cv2.waitKey(0)
                cv2.destroyWindow("image")
                isSave = input("do you want to save the image (y/n) : ")
                if isSave == 'y':
                    file_name = input("enter file name : ")
                    cv2.imwrite(file_name, frame)

        case 2:
            while True:
                ret, image = camera.read()
                if not ret:
                    print("could not load")
                    break

                recoder.write(image)
                cv2.imshow("video recording", image)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("quitting....")
                    break

            cv2.destroyAllWindows()

                
                
        case 3:
            break


camera.release()
recoder.release()
cv2.destroyAllWindows()