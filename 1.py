from PIL import Image, ImageFilter
import os

if not os.path.exists('blur'):
    os.makedirs('blur')

image1 = Image.open('1.png')
image2 = Image.open('2.png')
image3 = Image.open('3.png')
image4 = Image.open('4.png')
image5 = Image.open('5.png')

blur_img1 = image1.filter(ImageFilter.BLUR)
blur_img2 = image2.filter(ImageFilter.BLUR)
blur_img3 = image3.filter(ImageFilter.BLUR)
blur_img4 = image4.filter(ImageFilter.BLUR)
blur_img5 = image5.filter(ImageFilter.BLUR)

blur_img1.save('blur/blur_img1.png')
blur_img2.save('blur/blur_img2.png')
blur_img3.save('blur/blur_img3.png')
blur_img4.save('blur/blur_img4.png')
blur_img5.save('blur/blur_img5.png')