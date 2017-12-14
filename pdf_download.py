# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:54:26 2017

@author: VX
"""

import os
import urllib.request as url_request

file_dir = './download'
os.chdir(file_dir)
print(os.getcwd())

for num in range(0, 1000000, 100):
    try:
        download_url = 'http://epaper.gotop.com.tw/PDFSample/ACL{0:0>6d}.pdf'.format(num)
        response = url_request.urlopen(download_url)
        file_name = download_url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response.read())
    except:
        print('{0:0>6d}except:can not find'.format(num))
    

    print("Completed")

