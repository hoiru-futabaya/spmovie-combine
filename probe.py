import ffmpeg
import json

path = "/storage/761C-FA25/DCIM/101INCAM/191217_165243.mp4"

info = ffmpeg.probe(path)

rotate = next((stream for stream in info['streams'] if stream['codec_type'] == 'video'), None)

print(rotate["tags"]["rotate"])

input = ffmpeg.input(path)

out = ffmpeg.output(input, "test.mp4")

ffmpeg.run(out)
