import cv2

image_location = input("Please enter location of a image : ")
image = cv2.imread(image_location)
if image is not None:
    print("--------------------")
    print("Choose the Option")
    print("1. save image")
    print("2. covert into grayscale")
    print("3. show image")
    print("4. Exit/Quit")
    print("--------------------")
    print()

    while True:
        choice = int(input("enter the given option : "))
        match choice:
            case 1:
                image_name = input("enter the name of image that you want to save : ")
                save = cv2.imwrite(image_name, image)
                if save:
                    print("save Successe ")
                else:
                    print("error: unable to save")

            case 2:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                print("image convert gray succussefully done")
            
            case 3:
                cv2.imshow("image tab", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            case 4:
                break


else:
    print("image could not load")
