from PIL import Image
from dataset.mnist import load_mnist
import numpy as np

(train_img,train_label),(test_img,test_label) = load_mnist(flatten=False,normalize=False)

img = train_img[0]
img = img.reshape(28,28)
label = train_label[0]

print("--------------train----------------")
print(train_img.shape)
print(train_label.shape)

print(label)

Image.fromarray(np.uint16(img)).show()
#pilimg = Image.fromarray(np.uint8(img))
#pilimg.show()
print("--------------test----------------")

print(test_img.shape)
print(test_label.shape)
img2 = test_img[0]
img2 = img2.reshape(28,28)
Image.fromarray(np.uint32(img2)).show()