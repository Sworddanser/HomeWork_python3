import subprocess
import os.path
import os

file_path = os.path.abspath(os.path.dirname(__file__))
image = os.listdir(os.path.join(file_path, 'Source'))
for i in image:
	subprocess.run('convert .\Source\*.jpg -resize 200 .\Results\image.jpg')

  	
	 