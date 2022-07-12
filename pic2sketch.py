import cv2

def img2sketch(photo, k_size, name):
    #Read Image
    img=cv2.imread(photo)
    
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

    # Save Sketch 
    cv2.imwrite(f'./to_sketch/{name}.png', sketch_img)

    # Display sketch
    # cv2.imshow(f'./korea/pic_to_sketch/{name}.png',sketch_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
#Function call
# for i in range(1, 484):
img2sketch(photo=f'./user_drawing_img/mou.png', k_size=7, name=f'to_scketch')