import cv2

image1  = input("enter the file loction of image : ")

image = cv2.imread(image1)


if image is None:
    print("image could not load")
else:
    print("<-----Choose the option----->")
    print("1. Add Line")
    print("2. Add Ractangle")
    print("3. Add Circle")
    print("4. Add Text")
    print("5. show image")
    print("6. Save")
    print("7. Exit/Quit")
    while True:
        choice = int(input("enter Your option : "))
        match choice:
            case 1:
                pt1 = (
                    int(input("enter X value of starting point of line : ")),
                    int(input("enter Y value of starting point of line : ")))
                pt2 = (
                    int(input("enter X value of ending point of line : ")),
                    int(input("enter Y value of ending point of line : ")))
                color = (
                    int(input("enter value of blue color (0 - 255) : ")),
                    int(input("enter value of green color (0 - 255) : ")),
                    int(input("enter value of red color (0 - 255) : "))
                )
                thickness = int(input("enter thickness of line : "))
                cv2.line(image, pt1, pt2, color, thickness)
            case 2:
                pt1 = (
                    int(input("enter X value of starting coner point of ractangle : ")),
                    int(input("enter Y value of starting coner point of ractangle : ")))
                pt2 = (
                    int(input("enter X value of ending coner point of ractangle : ")),
                    int(input("enter Y value of ending coner point of ractangle : ")))
                color = (
                    int(input("enter value of blue color (0 - 255) : ")),
                    int(input("enter value of green color (0 - 255) : ")),
                    int(input("enter value of red color (0 - 255) : "))
                )
                thickness = int(input("enter thickness of ractangle : "))
                cv2.rectangle(image, pt1, pt2, color, thickness)
            case 3:
                center = (
                    int(input("enter x value of center of the circle : ")),
                    int(input("enter Y value of center of the circle : "))
                )
                radius = int(input("enter the radius of the circle : "))
                color = (
                    int(input("enter value of blue color (0 - 255) : ")),
                    int(input("enter value of green color (0 - 255) : ")),
                    int(input("enter value of red color (0 - 255) : "))
                )
                thickness = int(input("enter thickness of ractangle : "))
                cv2.circle(image, center, radius, color, thickness)
            case 4:
                text = input("enter the text that you want to show : ")
                org = (
                    int(input("enter x value of bottom left coner of Text : ")),
                    int(input("enter y value of bottom left coner of Text : "))
                )
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = int(input("enter the size of font : "))
                color = (
                    int(input("enter value of blue color (0 - 255) : ")),
                    int(input("enter value of green color (0 - 255) : ")),
                    int(input("enter value of red color (0 - 255) : "))
                )
                thickness = int(input("enter the thickness of text : "))
                cv2.putText(image , text, org, font, fontScale, thickness)
            case 5:
                cv2.imshow("reactange", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            case 6:
                image_name = input("enter image name (with extension) : ")
                cv2.imwrite(image_name, image)
            case 7:
                break
            