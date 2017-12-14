#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:11:55 2017

@author: wei
"""

import os
import urllib.request as url_request
import gevent
from gevent import monkey;
monkey.patch_all()         #添加io操作标准，让程序可以并行下载网页

def download_pdf(num):
    try:
        download_url = 'http://cbafaculty.org/Dynamics/Chapter%20{}.pdf'.format(num)
        response = url_request.urlopen(download_url)
        file_name = download_url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response.read())
    except:
        print('{}except:can not find'.format(num))
    
    print("Completed")
    

if __name__ == '__main__':
    file_dir = './download'
    os.chdir(file_dir)
    print(os.getcwd())
    
    for num in range(1, 22, 1):
        task = [gevent.spawn(download_pdf, num)]
    gevent.joinall(task)
        