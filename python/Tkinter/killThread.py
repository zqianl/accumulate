#!/usr/bin/env python
# -*- coding: utf-8 -*-

#linux下依据进程的名字杀掉进程
import os,re,sys

def kill_by_name(name):
	cmd='ps aux|grep %s'%name
	f=os.popen(cmd)
	regex=re.compile(r'\w+\s+(\d+)\s+.*')
	txt=f.read()
	if len(txt)<5:
		print 'there is no thread by name or command %s'%name
		return

	ids=regex.findall(txt)
	cmd="kill %s"%' '.join(ids)
	os.system(cmd)

if __name__=='__main__':
	kill_by_name('gedit')