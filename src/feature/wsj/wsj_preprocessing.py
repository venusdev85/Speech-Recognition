#-*- coding:utf-8 -*-
#!/usr/bin/python
''' Automatic Speech Recognition
author(s):
zzw922cn
     
date:2017-5-5

we process the data using Kaldi s5 recipe
train set: si284
validation set: eval92
test set: dev93
'''

import sys
sys.path.append('../')
sys.dont_write_bytecode = True


import shutil
import os
from core.fileUtils import check_path_exists

def split_data_by_s5(src_dir, des_dir, keywords=['train_si284', 'test_eval92', 'test_dev93']):
  for key in keywords:
    wav_file_list = os.path.join(src_dir, key+'.flist') 
    label_file_list = os.path.join(src_dir, key+'.txt') 
    new_path = check_path_exists(os.path.join(des_dir, key))

    with open(wav_file_list, 'r') as wfl:
      wfl_contents = wfl.readlines()
      for line in wfl_contents:
        line = line.strip()
        shutil.copyfile(line, os.path.join(des_dir, key, line.split('/')[-1]))
        print line

    with open(label_file_list, 'r') as lfl:
      lfl_contents = lfl.readlines()
      for line in lfl_contents:
        label = ' '.join(line.strip().split(' ')[1:])
        with open(os.path.join(des_dir, key, line[0]+'.label'), 'w') as lf:
          lf.writeline(label)
        print line[0]
        

if __name__ == '__main__':
  src_dir = '/media/pony/DLdigest/study/ASR/corpus/wsj/s5/data'
  des_dir = '/media/pony/DLdigest/study/ASR/corpus/wsj/standard'
  split_data_by_s5(src_dir, des_dir)

