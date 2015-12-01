#!/usr/bin/python
# -*- coding: utf-8 -*-

# windows2003からエクスポートしたxmlを2008r2用にコンバートするツール

from __future__ import print_function

import os.path
import subprocess
import glob
import string

src_path = '/Users/nagais/tmp/xml_lists_b1/work'
dst_path = '/Users/nagais/tmp/xml_lists_b1/out'

file_list = glob.glob(os.path.join(src_path, '*'))
file_name = [os.path.relpath(x, src_path) for x in file_list]

match1 = 'version="1.1"'
rep1 = 'version="1.2"'
match2 = '</Principal>'
rep2 = '  <RunLevel>HighestAvailable</RunLevel>\r\n    </Principal>'
match3 = 'BATCHSRV1'
rep3 = 'BATCHSRV4'

def main():
    for tf in file_name:
        sedfile = os.path.join(src_path, tf)
        addfile = os.path.join(dst_path, tf)
        f_sedfile = open(sedfile, "r")
        f_addfile = open(addfile, "w")
        for line in f_sedfile:
            line = line.replace(match1, rep1)
            line = line.replace(match2, rep2)
            line = line.replace(match3, rep3)
            f_addfile.write(line)
        f_sedfile.close()
        f_addfile.close()

if __name__ == "__main__":
    main()
