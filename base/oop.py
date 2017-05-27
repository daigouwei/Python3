#!/usr/bin/python3
# -*- coding: utf-8 -*-

#std1 = {'name':'guowei', 'score':'99'}
#def print_score1(std):
#    print('%s: %s' % (std['name'],std['score']))
#print_score1(std1)

#std2 = {'a':1, 'b':2, 'c':3, 'd':4}
#def print_score2(std):
#   print(std['a'])
#print_score2(std2)

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
stu1 = Student('guowei', 99)
stu2 = Student('malu', '99')
stu1.print_score()
stu2.print_score()

print('%s' % (25))
print('%d' % (25))
