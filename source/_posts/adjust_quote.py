# coding: utf-8
import os
def list_files(rootDir):
    fileList = list()
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            if os.path.join(root,filespath)[-3:] == '.md':
                fileList.append(os.path.join(root,filespath))
    return fileList
def adjust_quote(filename):
    fileH = open(filename, 'r')
    content = fileH.read().replace('「', '『『').replace('」','』』').replace('『', '「').replace('』','」').replace('「「', '『').replace('」」','』')
    fileH.close()
    # print content
    fileH = open(filename, 'w')
    fileH.write(content)
    fileH.close()
    return None
if __name__ == '__main__':
    for filename in list_files('.'):
        adjust_quote(filename)
