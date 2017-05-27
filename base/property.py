#!/usr/bin/python3
#-*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, w):
        self._width = w
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, h):
        self._height = h
    @property
    def resolution(self):
        self._resolution = self._width*self._height
        return self._resolution

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
