list1 = [1,2,3,4,5,6,7,8,9,10]

# def findIdx(num):
#     list2 = list1
#     cnt = 0
#     while(1):
#         midIdx = round(((len(list2)-1)/2))
#         midNum = list2[midIdx]
#         cnt += 1
#         if(num > midNum):
            
#             list2 = list2[midIdx+1:]
#         elif(num < midNum):
            
#             list2 = list2[:midIdx]
#         elif(num == midNum):
            
#             return print("%d의 인덱스는 %d로 %d 번 만에 찾았습니다."%(num,list1.index(midNum),cnt))
        
# findIdx(2)

def findIdx(num):
    cnt = 0
    startIdx = 0
    endIdx = len(list1) - 1
    
    while (1):
        midIdx = (startIdx + endIdx) // 2
        cnt += 1
        if(num not in list1):
            return print("리스트에 없는 값입니다.")
        elif list1[midIdx] == num:
            return print("%d의 인덱스는 %d로 %d 번 만에 찾았습니다."%(num,midIdx,cnt))
        elif list1[midIdx] < num:
            startIdx = midIdx + 1
        else:
            endIdx = midIdx - 1

findIdx(-22)
