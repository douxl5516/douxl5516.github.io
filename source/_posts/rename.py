# coding: utf-8
import os
def dict_files(rootDir = '.'):
    nameDict = dict()
    for root,dirs,files in os.walk('.'):
        for name in files:
            if name[-3:] == '.md':
                print 'cd %s && ren %s %s' % (root, name, name[11:])
                os.system('cd %s && ren %s %s' % (root, name, name[11:]))

if __name__ == '__main__':
    dict_files()
