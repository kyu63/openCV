#important

#contour, herarachy = cv2.findContours(image, mode , method)

#mode = three mode 1.  retr_tree   2. retr_external , 3. retr_list
#method = how much detail to return contour


#cv2.drawContour is use to show the contour
#cv2.drawContour(image, contours, contours_index, color, thickness)
#contour_index = decide which shape is draw
#if 0 draw first 
# if 1 draw second 
# if -1 draw all shape in list


import cv2

img = cv2.imread("360_F_177678528_hHnIMvUYZ4nhthYTaLyzZMRkJm2vw9IT.jpg")

if img is None:
    print("image could not load")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    contour, herarachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contour, -1, (0,255,0), 3)



    # cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()