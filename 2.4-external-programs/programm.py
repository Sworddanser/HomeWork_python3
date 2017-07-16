import subprocess
import os.path
import os

FILE_PATH = os.path.abspath(os.path.dirname(__file__))



def create_dir():
    os.chdir(FILE_PATH)
    if os.path.exists(os.path.join(FILE_PATH, 'Results')) != True:
        os.mkdir('Results', 0o777)

def convert():
    image = os.listdir(os.path.join(FILE_PATH, 'Source'))
    for i in image:
        subprocess.run('convert .\Source\%s -resize 200 .\Results\%s' % (i, i) )

def main():
    create_dir()
    convert()


main()
