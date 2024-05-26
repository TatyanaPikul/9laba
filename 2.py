VALID_IMAGE_EXTS = ("jpg", "jpeg", "png")

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

try:
        for image_name in source_images_name:
            img_name, img_ext = os.path.splitext(image_name)
            if img_ext in VALID_IMAGE_EXTS:
                with Image.open(os.path.join(source_path_dir, image_name)) as image:
                    filtered_image = image.convert("BLUR").filter(
                        random.choice(applied_filters)
                    )
                    filtered_image.save(
                        os.path.join(output_path_dir, f"{img_name}_filtered.{img_ext}")
                    )
except OSError:
    print("[ОШИБКА] Проблемы с файлами.")