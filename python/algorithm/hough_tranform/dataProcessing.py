#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *
import numpy as np
import math
import pandas as pd
from xlwt import *
import matplotlib.pyplot as plt

with open('2.txt','r') as f:
	data = f.readline()
data=data.split(',')
data=[float(element) for element in data]

angle_min=-2.35619449615
angle_max=2.09234976768
angle_increment=(angle_max-angle_min)/(len(data) - 1)

#将原始数据转换到直角坐标系
x_all = []
y_all = []
a = -1
for distance in data:
	a +=1
	if not math.isnan(distance):
		angle_curr = angle_min + a * angle_increment
		x = distance * sin(angle_curr)
		y = distance * cos(angle_curr)
		x_all.append(x)
		y_all.append(y)
	else:
		x_all.append(nan)
		y_all.append(nan)

x_all_not_nan = [a for a in x_all if not isnan(a)]
y_all_not_nan = [a for a in y_all if not isnan(a)]
plt.figure('fig1')
plt.scatter(x_all_not_nan,y_all_not_nan,s=2)

#为所有点加上序号，观察点的走向
# n = np.arange(len(x_all_not_nan))
# for i,label in enumerate(n):
# 	plt.annotate(label,(x_all_not_nan[i],y_all_not_nan[i]))
# plt.show()

max_distance = max(data)
interval_dist = 0.1
interval_angle = 5 #角度
num_group_dist = max_distance / interval_dist
num_group_dist = int(ceil(num_group_dist))
num_group_angle = 180/interval_angle

count_matrix = np.zeros((num_group_dist,num_group_angle))
point_include_matrix = pd.DataFrame([],index=range(num_group_dist),columns=range(num_group_angle))
for i in range(num_group_angle):
	for j in range(num_group_dist):
		point_include_matrix.iloc[j,i]=[]
p_all=[]

#以p为纵坐标、theta为横坐标作出所有点的在p_o_theta坐标系下的分布图
# a = -1
# for distance in data:
# 	a += 1
# 	for i in range(num_group_angle):
# 		theta_curr = pi/180 * i * interval_angle
# 		p_curr = abs(x_all[a] * sin(theta_curr) - y_all[a] * cos(theta_curr))
# 		p_all.append(p_curr)
# 	theta_all = arange(0,180,interval_angle)
# 	plt.plot(theta_all,p_all)
# 	p_all = []
# plt.show()

#hough变换的核心，将直角xoy坐标系中的每个点映射到p_o_theta坐标系下
#并计算出落在每个网格中的点的个数以及点的序号
a = -1
for i in range(num_group_angle):
	theta_curr = pi/180 * i * interval_angle
	for distance in data:
		a += 1
		if not math.isnan(distance):
			p_curr = abs(x_all[a] * sin(theta_curr) - y_all[a] * cos(theta_curr))
			seq_p_curr = int(floor(p_curr/interval_dist))
			count_matrix[seq_p_curr,i] += 1
			point_include_matrix.iloc[seq_p_curr,i].append(a)
	a = -1

#每个网格中落下的点的个数输出到excel表
# file_name_num_point = 'num_point_angle_05_dist_10.xls'
# file = Workbook(encoding = 'utf-8')
# table_num_point = file.add_sheet(file_name_num_point)
# for i,p in enumerate(count_matrix):
# 	for j,q in enumerate(p):
# 		table_num_point.write(i,j,q)
# file.save(file_name_num_point)

# 每个网格中分别落下的点的序号输出到Excel表
# file_name_seq_point = 'seq_point_angle_05_dist_10.xls'
# file = Workbook(encoding = 'utf-8')
# table_seq_point = file.add_sheet(file_name_seq_point)
# for i in range(num_group_dist):
# 	for j in range(num_group_angle):
# 		table_seq_point.write(i,j,str(point_include_matrix.iloc[i,j]))
# file.save(file_name_seq_point)

#对所有点进行统计，初步将成直线的点取出
threshold_num_point = 30    #一条直线上点的个数的最小值
line_include_point = []
for i in range(num_group_dist):
	for j in range(num_group_angle):
		count = 1
		start = 0
		end = 1
		if count_matrix[i,j] > threshold_num_point:
			while end < len(point_include_matrix.iloc[i,j]):
				#第一种判断方式，直接用点是否相邻，不佳
				# if point_include_matrix.iloc[i,j][end] - point_include_matrix.iloc[i,j][end - 1] <= 1:
				#第二种方式通过距离进行判断，较好
				distance_neighbor = math.sqrt(pow(x_all[point_include_matrix.iloc[i,j][end]]-x_all[point_include_matrix.iloc[i,j][end - 1]],2) +
											  pow(y_all[point_include_matrix.iloc[i,j][end]]-y_all[point_include_matrix.iloc[i,j][end - 1]],2))
				if distance_neighbor < 0.08:   #如果相邻点的距离小于0.08，则认为是同一条直线上的点
					count += 1
					end += 1
				else:
					if count >= threshold_num_point:
						line = point_include_matrix.iloc[i,j][start : end]
						line_include_point.append(line)
					start = end
					end += 1
					count = 1
			if count >= threshold_num_point:
				line = point_include_matrix.iloc[i, j][start: end]
				line_include_point.append(line)

#初步去除重复的直线，集合中所有点均相同则保留其一
unique_line_include_point = list(set([tuple(t) for t in line_include_point]))

#去除一个是另一个子集的情况
num_line = len(unique_line_include_point)
for i in range(num_line - 1):
	for j in arange(i+1, num_line, 1):
		if len(unique_line_include_point[i]) and len(unique_line_include_point[j]):
			if set(unique_line_include_point[i])>set(unique_line_include_point[j]):
				unique_line_include_point[j] = []
			elif set(unique_line_include_point[j])>set(unique_line_include_point[i]):
				unique_line_include_point[i] = []
				break
			else:
				continue
unique_line_include_point = [x for x in unique_line_include_point if len(x)]

#对任意两条直线，如果其重复的点超过较短的30%则将两条直线合并
num_unique_line_include_point = len(unique_line_include_point)
for i in range(num_unique_line_include_point - 1):
	for j in arange(i+1, num_unique_line_include_point, 1):
		if len(unique_line_include_point[i]) != 0 and len(unique_line_include_point[j]) != 0:
			intersection_list = list((set(unique_line_include_point[i]).union(set(unique_line_include_point[j])))^
									 (set(unique_line_include_point[i])^set(unique_line_include_point[j])))
			if len(intersection_list) >= 0.3 * min([len(unique_line_include_point[i]),len(unique_line_include_point[j])]):
				if len(unique_line_include_point[i]) > len(unique_line_include_point[j]):
					unique_line_include_point[j] = []
					unique_line_include_point[i] = list(set(unique_line_include_point[i]).union(set(unique_line_include_point[j])))
				else:
					unique_line_include_point[i] = []
					unique_line_include_point[j] = list(set(unique_line_include_point[i]).union(set(unique_line_include_point[j])))
					break
merge_line_include_point = [x for x in unique_line_include_point if len(x)]

#再次去重
merge_line_include_point = list(set([tuple(t) for t in merge_line_include_point]))

#将挤在一堆的点组成的直线去掉
threshold_distance = 0.5   #如果该线段的长度小于0.5则直接将该线段舍去不计
num_merge_line_include_point = len(merge_line_include_point)
for i in range(num_merge_line_include_point):
	distance_start_to_end = math.sqrt(pow(x_all[merge_line_include_point[i][0]] - x_all[merge_line_include_point[i][-1]], 2) +
									  pow(y_all[merge_line_include_point[i][0]] - y_all[merge_line_include_point[i][-1]], 2))
	if distance_start_to_end <threshold_distance:
		merge_line_include_point[i] = []
final_line_include_point = [x for x in merge_line_include_point if len(x)]

#line输出到excel表
# file_name_line = 'final_line_angle_05_dist_10.xls'
# file = Workbook(encoding = 'utf-8')
# table_line = file.add_sheet(file_name_line)
# for i,p in enumerate(final_line_include_point):
# 	for j,q in enumerate(p):
# 		table_line.write(i,j,q)
# file.save(file_name_line)

#将最终检测出的直线上的点画出
plt.figure('fig2')
x = []
y = []
for i in final_line_include_point:
	for j in i:
		x.append(x_all[j])
		y.append(y_all[j])
	plt.scatter(x,y,s=2)
	x = []
	y = []

#最小二乘拟合每条直线
plt.figure('fig1')
x_all = np.array(x_all)
y_all = np.array(y_all)
num_final_line = len(final_line_include_point)
for i in range(num_final_line):
	#最小二乘计算k和b
	sum_x = sum(x_all[np.array(final_line_include_point[i])])
	sum_y = sum(y_all[np.array(final_line_include_point[i])])
	sum_xy = sum(x_all[np.array(final_line_include_point[i])] * y_all[np.array(final_line_include_point[i])])
	sum_x2 = sum(x_all[np.array(final_line_include_point[i])] * x_all[np.array(final_line_include_point[i])])
	b = (sum_x2 * sum_y - sum_x * sum_xy) / (len(final_line_include_point[i]) * sum_x2 - sum_x * sum_x)
	k = (len(final_line_include_point[i]) * sum_xy - sum_x * sum_y) / (len(final_line_include_point[i]) * sum_x2 - sum_x * sum_x)
	#x的起点与终点的计算
	x_start = x_all[final_line_include_point[i][0]] + \
			  abs(k) * (k * x_all[final_line_include_point[i][0]] + b - y_all[final_line_include_point[i][0]]) / (k * k + 1)
	x_end = x_all[final_line_include_point[i][-1]] + \
			  abs(k) * (k * x_all[final_line_include_point[i][-1]] + b - y_all[final_line_include_point[i][-1]]) / (k * k + 1)
	#画图
	x_plot = np.linspace(float(x_start),float(x_end),100)
	y_plot = [k * x + b for x in x_plot]
	plt.plot(x_plot, y_plot, color = 'r',linewidth = 1)
plt.show()






























