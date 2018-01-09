#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os


soc_path="living_room_traj2_loop/"
tar_path="xiaobao/"
if not os.path.exists(tar_path):
	os.makedirs(tar_path)

file_list=os.listdir(soc_path)

a = 0
for file in file_list:
	file_list[a] = (file.split('.'))[0].split('_')[2]
	a+=1
file_list.sort()

a = 0
for file in file_list:
	if(a % 3 == 0):
		file_list[a] = "scene_00_"+file+".depth"
	if (a % 3 == 1):
		file_list[a] = "scene_00_" + file + ".png"
	if (a % 3 == 2):
		file_list[a] = "scene_00_" + file + ".txt"
	a += 1

flag = 0
for file_path in file_list:
	if (flag % 9 == 0 or flag % 9 == 1 or flag % 9 == 2):
		soc_fullname = soc_path + file_path
		tar_fullname = tar_path + file_path
		shutil.copy(soc_fullname, tar_fullname)
	flag += 1
