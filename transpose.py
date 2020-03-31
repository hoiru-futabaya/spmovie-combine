import ffmpeg
import os

path = '001.mp4'

os.chmod(path, 0777)

input = ffmpeg.input(path)

input = input.filter('transpose', 1)

out =ffmpeg.output(input, 'test.mp4')

ffmpeg.run(out)
