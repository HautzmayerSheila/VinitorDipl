from PIL import Image
import glob

PATH = "field_data/*.tiff"
i = 26
for image_path in sorted(glob.glob(PATH)):
    if i > 7:
        image = Image.open(image_path)
        print(image_path)
    #image_resize = image.resize((224, 224))
    #image_resize.save("images_aug/"+image_path.split("/")[-1], "png")
        image.save("new_data/field_"+str(i)+"_mask.tiff", "tiff")
    i += 1
