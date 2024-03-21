def solution(arr):
    answer = 0
    a=[]
    b= 0
    c = 0
    while b != 1:
        for i in range(len(arr)):
            if arr[i] % 2 == 1 and arr[i] <= 50:
                answer = arr[i] * 2 +1
                a.append(answer)
                print('1',a)
            elif arr[i] % 2 == 0 and arr[i] >= 50:
                answer = arr[i] / 2
                a.append(answer)
                print('2',a)
            else:
                a.append(arr[i])
                print('3',a)
        print(a)
        if arr == a:
            b = 1
        else:
            arr = a
            a =[]
            c += 1
        
    answer = c
    return answer

a= [1, 2, 3, 100, 99, 98]
print(solution(a))