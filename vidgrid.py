from moviepy.editor import *
import random, argparse

#Separates clip list into chunks
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

def main():
	parser = argparse.ArgumentParser(description='creates a grid of delayed video clips')
	parser.add_argument("input", help="input filename [REQUIRED]", type=str)

	parser.add_argument("-o", help="output filename, default is output.mp4", type=str)
	parser.add_argument("-rows", help="number of rows in the grid, default is 3", type=int)
	parser.add_argument("-d", help="delay time between each clip, default is  0.25", type=float)
	parser.add_argument("-rand", help="random delay time variation between each clip, default is  0", type=int)

	inputfile = ''
	outputfile = 'output.mp4'
	rows = 3
	delay = 0.25
	rand = 0

	args = parser.parse_args()

	if(args.input):
		inputfile = args.input
	if(args.o):
		outputfile = args.o
	if(args.rows):
		rows = args.rows
	if(args.d):
		delay = args.d
	if(args.rand):
		rand = args.rand

	#Load clip
	original_clip = VideoFileClip(inputfile).subclip(0,-0.1).volumex(0.4)
	original_clip = original_clip.resize(width=((original_clip.w)/rows))

	#init clips list
	clips_list = []
	offset = delay

	#Build clips list
	for i in range(rows*rows):
		# print(offset)
		new_clip = original_clip.set_start(offset)	
		clips_list.append(new_clip)
		offset += (0.3)	
		

	arranged_clips = clips_array(chunkIt(clips_list,rows))

	
	arranged_clips.write_videofile(outputfile)

if __name__ == "__main__":
   main()

#Load clip
# original_clip = VideoFileClip(target).subclip(0,-0.1).volumex(0.4)
# original_clip = original_clip.resize(width=((original_clip.w)/3))

# #Init clips list and delay
# clips_list = []
# delay = 0


# #Build clips list
# for i in range(rows*rows):
#     new_clip = original_clip.set_start(delay)
#     clips_list.append(new_clip)
#     delay += random.uniform(0.1,0.5)


# arranged_clips = clips_array(chunkIt(clips_list,rows))

# # clip = clips_array([[clip1, clip2, clip3],
# #                           [clip4, clip5, clip6],
# #                             [clip7, clip8, clip9]])

# arranged_clips.write_videofile("out.mp4", threads=16)