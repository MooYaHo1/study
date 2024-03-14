def solution(nums):
    answer = []
    a=0
    for i in range(len(nums)):
        if nums[i] not in answer:
            answer.append(nums[i])
            if len(answer) == len(nums)/2:
                a = len(answer)
                break
    if len(answer) != len(nums)/2:
        a=len(answer)
    return a

#set 함수 적용 후
def solution(nums):
    answer = 0
    a=set(nums)
    if len(a) == len(nums)/2:
        answer = len(a)
    elif len(a) > len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(a)
    return answer

#set 사용 초간단
def solution(nums):
    answer = min(len(nums) // 2, len(set(nums))) # 예시가 4,3,2,2 이면 왼쪽하면 3 오른쪽 2 min하면 더 작은 2 선택, 2,2,2,3,3,3 하면 왼쪽 2 오른쪽 3 min하면 왼쪽 2선택
    return answer