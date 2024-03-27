import csv
import cv2
labels_file = 'C:\\Users\\ASUS\\Desktop\\Impromptu\\Impromptu\\OPCV\\labels.csv'
labels = {}
with open(labels_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        image_filename = row[0]
        image_labels = row[1:]
        labels[image_filename] = image_labels
    # print(labels)

image_dir = 'C:\\Users\\ASUS\\Desktop\\Impromptu\\Impromptu\\OPCV\\Dataset'
images = {}
for image_filename in labels.keys():
    image_path = image_dir +"\\"  +image_filename
    image = cv2.imread(image_path)
    if image is not None:
        images[image_filename] = image
        print('Image Loaded' + image_filename)
    else:
        print(f"Failed to load image: {image_filename}")

# target_size = (224, 224) 
# for image_filename, image in images.items():
#     resized_image = cv2.resize(image, target_size)
#     normalized_image = resized_image / 255.0
#     images[image_filename] = normalized_image

target_size = (224,224)
for image_filename, image in images.items():
    resized_image = cv2.resize(image, target_size)
    normalized_image = resized_image / 255.0
    image[image_filename] = normalized_image



30th august