import sys

input = list(str(sys.stdin.readline()))

while input != ['.','\n']:
    lst = []
    for i in input:
        if i == '(' or i == ')' or i == '[' or i == ']':
            lst.append(i)
        while len(lst) >= 2 and lst[-2] == '(' and lst[-1] ==')':
            lst.pop()
            lst.pop()
        while len(lst) >= 2 and lst[-2] == '[' and lst[-1] ==']':
            lst.pop()
            lst.pop()
    print('yes' if lst==[] else 'no')
    input = list(sys.stdin.readline())