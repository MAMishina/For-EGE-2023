# coding=windows-1251
# ���������� � � � � ���������� ��������� � ��������� ��
for x in '012345678':
    for y in '012345678':
        # ���� �������� ��������� �� ������� � ���������� � � � 
        result = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        # ��������� ������� �� ������� �������� ��������������� ��������� �� 61
        if result % 61 == 0:
            # ������� ���������� ����� � ������� � ��������� ���������. 
            print(result// 61)
            exit()








          
'''


# ����������� ������� ��� �������� ��������� �������� 
# ���������� Si (Si - S ������ � ��������� ����,
# pozition -  ����� ���� � ����)
def f(Si, pozition):
    if Si >= 26: # ������� ���������� ����
        return pozition == 2
    # �������� �������� ����
    return f(Si + 1, pozition + 1) or f(Si * 2, pozition + 1)
 
for Si in range(1, 25): # ������� ���� ���������� �������� Si
    # ����� ���� ��������� 0 �.�. ��� ��������� �������, ��� ����� �� �����
    if f(Si, 0) == 1: 
        print("������ 19: ", Si)
        break
# �.�. �� ���� ����������� �������� S, �� ������� ���������� ���������� ���������
# ��� ������ ������� ������ ���������� ��������.  

import turtle as t  # ��������� ������ ���������
k = 15  # ����������� ��� ������������ ����� �������� ��������
t.left(90)
t.speed(10)
for i in range(6):  # �������� �������� ���������� ������ �� �������
    t.forward(10 * k)
    t.right(60)
t.up()
t.speed(10)  # �������� �������� ���������
for x in range(19, -10, - 1):  # �������� ���������� �����
    for y in range(20, -10, - 1):
        t.goto(x * k, y * k)
        t.dot(4)  # ����� �������� 4 �������
t.done()
'''