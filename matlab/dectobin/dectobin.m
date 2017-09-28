function y=dectobin(innum,N)

%十进制小数转换为二进制数
%输入参数为innum和N
%innum为输入的十进制小数
%N为指定转换后二进制的位数
if (innum>1)||(N == 0)%判断输入的有效性
    disp('error!');
    return;
end
count=0;
tempnum=innum;
record=zeros(1,N);
while(N)
    count=count+1;%长度小于N
    if(count>=N)
        N=0;
    end
    tempnum=tempnum*2;%小数转换为二进制,乘2取整
    if tempnum>1
        record(count)=1;
        tempnum=tempnum-1; 
    elseif(tempnum==1)
        record(count)=1;
        N=0;%stop loop
    else
       record(count)=0;    
    end
end
 y=record;