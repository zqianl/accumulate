clc
clear all
Num=10000;
num_bit=16;
data=zeros(Num,1);
data_bin=zeros(Num,num_bit);
for t=1:Num
    data(t)=rand(1,1);
    data_bin(t,:)=dectobin(data(t),num_bit);
end
fid=fopen('test.dat','wt');%写入文件路径
matrix=data_bin;                       %input_matrix为待输出矩阵
[m,n]=size(matrix);
 for i=1:m
   for j=1:n
      if j==n
        fprintf(fid,'%g\n',matrix(i,j));
     else
       fprintf(fid,'%g',matrix(i,j));
      end
   end
end
fclose(fid);