# coding: utf-8
import os
import re
def list_files(rootDir):
    fileList = list()
    for root,dirs,files in os.walk(rootDir):
        for filespath in files:
            if os.path.join(root,filespath)[-3:] == '.md':
                fileList.append((os.path.join(root,filespath), filespath))
    return fileList
def adjust_siteurl(filename):
    fileH = open(filename, 'r')
    content = fileH.read()
    fileH.close()
    # print content
    print "%s read..." % (filename),
    content = re.sub('\\{\\{\\s*site\\.url\\s*\\}\\}', '', content)
    fileH = open(filename, 'w')
    fileH.write(content)
    fileH.close()
    print "%s processed."

    return None
def rename (filename, basename):
    if basename[:2] == "20":
        return None
    fileH = open(filename, 'r')
    content = fileH.read()
    fileH.close()
    # print content
    print "%s read..." % (filename)
    list_content = content.split('\n')
    for item in list_content:
        pass
    matchObj = re.search(r"(([0-9][0-9])|([1-2][0,9][0-9][0-9]))\/(([1-9])|(0[1-9])|(1[0-2]))\/(([0-2][0-9])|(3[0-1])|([0-9]))", content)
    str_ready = "./%s-%s" % (matchObj.group().replace('/', '-'), basename)
    fileH = open(str_ready, 'w')
    fileH.write(content)
    fileH.close()
    print "%s write..." % (str_ready)


if __name__ == '__main__':
    for filename, basename in list_files('.'):
        rename(filename, basename)
