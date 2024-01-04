def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        print(finished[i])
        if finished[i]:
            continue
        else:
            answer.append(todo_list[i])
    return answer