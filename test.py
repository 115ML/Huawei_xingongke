import sys
import os
from time import *
import EAST.eval as eval
#import EAST.multigpu_train as multigpu_train
import tensorflow as tf

tf.app.flags.DEFINE_string('test_data_path', 'model\EAST/test/', '')
tf.app.flags.DEFINE_string('gpu_list', '0', '')
tf.app.flags.DEFINE_string('checkpoint_path', 'model\EAST\model', '')
tf.app.flags.DEFINE_string('output_dir', 'model\EAST/out/', '')
tf.app.flags.DEFINE_bool('no_write_images', False, 'do not write images')

if __name__ == '__main__':
    time1 = time()
    print("begin")
    eval.main()
    print("end")
    time2 = time()
    print("耗时间："+str(time2-time1))