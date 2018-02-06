# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import time
import logging
import progressbar
bar = progressbar.ProgressBar()
for i in bar(range(100)):
    time.sleep(0.02)
    # progressbar.streams.wrap_stderr()
    bar = progressbar.ProgressBar()
    for i in bar(range(10)):
        logging.error('Got %d', i)
        time.sleep(0.5)