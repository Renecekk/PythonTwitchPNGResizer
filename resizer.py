from PIL import Image
import os

def resizetoallsizes(imgPath):
	img = Image.open(imgPath)
	resizedImage = img.resize((72, 72), resample=Image.LANCZOS)
	resizedImage.save("72x72-" + imgPath)
	resizedImage = img.resize((36, 36), resample=Image.LANCZOS)
	resizedImage.save("36x36-" + imgPath)
	resizedImage = img.resize((18, 18), resample=Image.LANCZOS)
	resizedImage.save("18x18-" + imgPath)

listoffiles = os.listdir(".")

for f in listoffiles:
	if (f.endswith(".png")):
		resizetoallsizes(f)