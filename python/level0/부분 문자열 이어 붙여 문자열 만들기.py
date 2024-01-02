def solution(my_strings, parts):
    answer = ''
    q = ''
    e = 0
    for a, b in parts:
         q = my_strings[e]
         answer += q[a:b+1]
         e+=1
    return answer
   
my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
print(solution(my_strings, parts))
