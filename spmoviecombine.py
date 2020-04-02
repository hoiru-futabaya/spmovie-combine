#!/usr/bin/python
# coding: utf8
import ffmpeg
import os

#os.chmod(path, 0777)

#まとめたいフォルダを選択
folder = os.getcwd()

#動画を番号順に読み込み、縦動画ならtranspose

fcount = len(os.listdir(folder))

print(fcount)

for i in range(fcount):
	path = folder + i + '.mp4'
