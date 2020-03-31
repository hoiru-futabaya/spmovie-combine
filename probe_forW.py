import ffmpeg
import json
import sys
import os

sys.path.append(r"D:\aquar\python2\Lib\site-packages\ffmpeg\ffmpeg-20200324-e5d25d1-win32-static\ffmpeg-20200324-e5d25d1-win32-static")

path = r"D:\aquar\Pictures\002.mp4"

os.chmod(path, 0777)

info = ffmpeg.probe(path)

rotate = next((stream for stream in info['streams'] if stream['codec_type'] == 'video'), None)

print(rotate["tags"]["rotate"])

#print(json.dumps(info, indent = 2))

input = ffmpeg.input(path)

out = ffmpeg.output(input, "test.mp4", transpose=1, rotate=0)

ffmpeg.run(out)
