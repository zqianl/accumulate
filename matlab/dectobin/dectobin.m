function y=dectobin(innum,N)

%ʮ����С��ת��Ϊ��������
%�������Ϊinnum��N
%innumΪ�����ʮ����С��
%NΪָ��ת��������Ƶ�λ��
if (innum>1)||(N == 0)%�ж��������Ч��
    disp('error!');
    return;
end
count=0;
tempnum=innum;
record=zeros(1,N);
while(N)
    count=count+1;%����С��N
    if(count>=N)
        N=0;
    end
    tempnum=tempnum*2;%С��ת��Ϊ������,��2ȡ��
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