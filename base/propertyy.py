#!/usr/bin/env
#-*- coding:utf-8 -*-

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015-self._birth

student = Student()
student.birth = 1990
print(student.birth)
print(student.age)


