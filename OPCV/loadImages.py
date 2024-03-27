import cv2
labels = {'image1.jpg': [' pranjal', 'suyash'], 'image2.jpg': [' suyash', 'pranjal', 'vedant'], 'image3.jpg': [' suyash', 'pranjal', 'vedant'], 'image4.jpg': [' suyash', 'pranjal', 'vedant'], 'image5.jpg': [' suyash', 'vedant', 'pranjal '], 'image6.jpg': [' suyash', 'vedant', 'pranjal '], 'image7.jpg': [' vedant', 'suyash', 'pranjal'], 'image8.jpg': [' nikunj', 'pranjal', 'abhishek', 'prakhar', 'amartya'], 'image9.jpg': [' suyash', 'pranjal'], 'image10.jpg': [' amartya', 'suyash', 'pranjal', 'abhishek', 'priyansh'], 'image11.jpg': [' amartya', 'suyash', 'pranjal', 'abhishek'], 'image12.jpg': [' pranjal', 'suyash', 'amartya', 'abhishek'], 'image13.jpg': [' pranjal', 'suyash', 'amartya', 'abhishek'], 'image14.jpg': [' abhishek', 'pranjal', 'omkar', 'suyash ', 'amartya'], 'image15.jpg': [' suyash', 'pranjal'], 'image16.jpg': [' abhishek', 'pranjal', 'omkar', 'suyash', 'amartya'], 'image17.jpg': [' pranjal', 'suyash', 'amartya', 'abhishek'], 'image18.jpg': [' shaury', 'suyash', 'vedant'], 'image19.jpg': [' triven', 'suyash', 'shaury', 'dinesh'], 'image20.jpg': [' sarvesh', 'shaury', 'suyash', 'vedant', 'pranjal', 'priyansh', 'dinesh', 'triven'], 'image21.jpg': [' shaury'], 'image22.jpg': [' shaury', 'suyash', 'vedant'], 'image23.jpg': [' vedant', 'ayush', ''], 'image24.jpg': [' aditya', 'aastha', 'ayush']}

image_dir = 'C:\\Users\\ASUS\\Desktop\\Impromptu\\Impromptu\\OPCV\\Dataset'
for image_filename in labels.keys():
    image_path = image_dir +"\\"  +image_filename
    image = cv2.imread(image_path)
    if image is not None:
        image[image_filename] = image
        print('Image Loaded' + image_filename)
    else:
        print(f"Failed to load image: {image_filename}")
