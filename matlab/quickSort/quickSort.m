function sortedNum=quickSort(unSortedNum,sizeUnSortedNum,start,finish)
if(start==finish)
    sortedNum=unSortedNum;
    return;
end
[index,unSortedNum]= Partition(unSortedNum,sizeUnSortedNum,start,finish);
if(index>start)
    unSortedNum=quickSort(unSortedNum,sizeUnSortedNum,start,index-1);
end
if(index<finish)
    unSortedNum=quickSort(unSortedNum,sizeUnSortedNum,index+1,finish);
end
sortedNum=unSortedNum;
end



