import os
basedir=os.path.abspath(os.path.dirname(__file__))
basedir1=os.path.abspath(os.path.dirname(__name__))
def read():
    with open('D:\Python_project\movie\movie.txt','r') as  f:
        a=f.readlines()
        for x  in a:
            print(x)


if __name__ == '__main__':
    print(__file__)
    print(basedir1)
    read()