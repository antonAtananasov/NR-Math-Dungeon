import numpy as np
from PIL import Image as im

def drawRoomWalls(segmentPixelsX, segmentPixelsY, doorPixels, roomSegmentsX=1, roomSegmentsY=1): 
	size = width, height = segmentPixelsX, segmentPixelsY
	doorsize = doorPixels
	roomsize = rwidth, rheight = roomSegmentsX, roomSegmentsY
	pixels=np.array([[(0,0,0)]*width]*height).astype(np.uint8)
	for i in range(len(pixels)):
		row = pixels[i]
		for j in range(len(row)):
			if (i == 0 or i == height - 1) or (j == 0 or j == width - 1):
				if not ((i >= width/2-doorsize/2 and i < width/2+doorsize/2) or (j >= height/2-doorsize/2 and j < height/2+doorsize/2)):
					pixels[i][j] = [255,255,255]
	pixels = np.concatenate([np.concatenate([pixels]*rwidth, axis=1)]*rheight)
	for i in range(len(pixels)):
		row = pixels[i]
		for j in range(len(row)):
			if not ((i == 0 or i == height*rheight - 1) or (j == 0 or j == width*rwidth - 1)):
				pixels[i][j] = [0,0,0]
				# print(i,j, pixels[i][j])
	im.fromarray(pixels).save('sample.png')

# drawRoomWalls(int(input("width: ")), int(input("height: ")),int(input('doorsize: ')),int(input("segments width: ")), int(input("segments height: ")))