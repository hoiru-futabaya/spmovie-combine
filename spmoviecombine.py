#!/usr/bin/python
# coding: utf8
import ffmpeg
import os
import shutil
import subprocess

text = 'concat.txt'

with open(text, mode = 'w') as f:
        f.write('')

#まとめたいフォルダを選択
print('フォルダのパスを入力')	
folder = 'test/'

#動画を番号順に読み込み、縦動画ならtranspose

fcount = len(os.listdir(folder))

print(fcount)

pathf = folder + 'copy/'
shutil.rmtree(pathf)
os.mkdir(pathf)


for i in range(fcount-1):
        number = str(i+1)
        path = folder + number.zfill(3) + '.mp4'
	path2 =  pathf + number.zfill(3) + '.mp4'
        os.chmod(path, 0777)
	input = 0
        input = ffmpeg.input(path)
        audio = input.audio
        info = ffmpeg.probe(path)
        video_info = next((stream for stream in info['streams'] if stream['codec_type'] == 'video'), None)

        w = video_info['width']
        h = video_info['height']
        r = video_info['tags']

        textc = 'file ' + path2 + "\n"

        hantei = 'rotate' in r
	print(hantei)


        if hantei == True :

                x = w / 9 * 16

                a = x - h 

                input = input.filter('transpose', 1)
                input = input.filter('pad', 0, x, 0, a/2, 'black')
                input = input.filter('scale', -1, 1920)
                input = input.filter('transpose', 2)

                out =ffmpeg.output(input, audio, path2)

                ffmpeg.run(out, overwrite_output=True)

		print('padding')

                with open(text, mode ='a') as f:
                        f.write(textc)
	        os.chmod(path2, 0777)


        else:
		out =ffmpeg.output(input, audio, path2)

                ffmpeg.run_async(out, overwrite_output=True)
		print('not padding')
                with open(text, mode ='a') as f:
                        f.write(textc)
	        os.chmod(path2, 0777)



else:
	cmd = ['ffmpeg', '-y', '-safe', '0', '-f', 'concat', '-i', 'concat.txt', '-c:v', 'copy', '-c:a', 'copy', '-c:s', 'copy', '-map', '0:v', '-map', '0:a', '-map', '0:s?', 'out2.mp4']

	subprocess.Popen(cmd)
