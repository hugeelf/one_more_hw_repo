# Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

print ('imput number')
n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print("{0} * {1} = {2}".format(i, j, i*j))
    print ("")
# структурная парадигма, так как используются управляющие конструкции (не представляю, как решать эту задачу без циклов), а также эта задача решается для того, чтобы решить задачу, а следовательно переиспользовать процедуры нет смысла, по этому они не объявляются.