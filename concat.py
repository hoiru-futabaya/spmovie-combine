#!/usr/bin/python
# coding: utf8
import ffmpeg
import os
import subprocess

path = 'concat.txt'

cmd = ['ffmpeg', '-y', '-safe', '0', '-f', 'concat', '-i', 'concat.txt', '-c:v', 'copy', '-c:a', 'copy', '-c:s', 'copy', '-map', '0:v', '-map', '0:a', '-map', '0:s?', 'test.mp4']

subprocess.Popen(cmd)

#ffmpeg.input(path).concat(n=2).output('test.mp4').run()
#input = ffmpeg.concat(input)

#input = ffmpeg.input("concat:" + "|".join(path))
#
#audio = input.audio
#
#out =ffmpeg.output(input, audio, 'test.mp4')
#
#ffmpeg.run(out, overwrite_output=True)
