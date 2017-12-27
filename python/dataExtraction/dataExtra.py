#!/usr/bin/env python
# -*- coding: utf-8 -*-

filename_read = 'hector_filter.txt'
filename_result = 'hector_map_data.txt'
final_result = []
with open(filename_read,'r') as file_to_read:
	while 1:
		line = file_to_read.readline()
		if not line:
			break
		list_line = line.split()
		flag = 0
		count = -1
		for string in list_line:
			count += 1
			if string == 'hector_map+':
				flag += 1
				break
		if flag:
			line_result = [list_line[count-3],list_line[count-2],list_line[count-1]]
			final_result.append(line_result)
		else:
			pass

num_line_result = len(final_result)
for i in range(num_line_result):
	final_result[i][2] = int(final_result[i][2].split(':')[0]) * 60 + float(final_result[i][2].split(':')[1])

with open(filename_result, 'w') as file_to_write:
	for i in final_result:
		for j in i:
			file_to_write.write(str(j)+' ')
		file_to_write.write('\n')