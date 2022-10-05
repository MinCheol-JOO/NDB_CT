N = int(input())
num_list = list(map(int,input().split()))
# 연산자 양
operator_amount = list(map(int,input().split()))
operators = ['+','-','*','/']
# 연산자 itertools 사용하기 위한 tmp 지정
operator_dict = {x:0 for x in operators}

import itertools
from itertools import permutations

operator_all_amount = []
for i in range(len(operator_amount)):
    for j in range(operator_amount[i]):
        operator_all_amount.append(operators[i])
        
# permutation 설정
perm_operaor_all = itertools.permutations(operator_all_amount,len(operator_all_amount))

for i 