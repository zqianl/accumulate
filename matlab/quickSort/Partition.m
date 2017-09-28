function [index,unSortedNum]=Partition(unSortedNum,sizeUnSortedNum,start,finish)
index=floor(rand()*(finish-start+1))+start;
while(index==finish+1)
    index=floor(rand()*(finish-start+1))+start;
end
unSortedNum=Swap(unSortedNum,index,finish);
small=start-1;
for t=start:finish-1
    if unSortedNum(t)<unSortedNum(finish)
        small=small+1;
        if(small~=t)
            unSortedNum=Swap(unSortedNum,t,small);
        end
    end
end
small=small+1;
unSortedNum=Swap(unSortedNum,small,finish);
index=small;
end

function unSortedNum=Swap(unSortedNum,indexA,indexB)
mid=unSortedNum(indexA);
unSortedNum(indexA)=unSortedNum(indexB);
unSortedNum(indexB)=mid;
end
