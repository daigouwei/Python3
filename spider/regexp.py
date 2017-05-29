#!/usr/bin/env
# -*- coding: utf-8 -*-

'''1
import re

pattern = re.compile(r'hello')
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello, CQC!')
if result1:
    print(result1.group())
else:
    print('1sb')
if result2:
    print(result2.group())
else:
    print('2sb')
if result3:
    print(result3.group())
else:
    print('3sb')
if result4:
    print(result4.group())
else:
    print('4sb')
'''

'''2 problem
import re

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print('m.string: %s' % m.string)
print('m.re: %s' % m.re)
print('m.pos: %s' % m.pos)
print('m.endpos: %s' % m.endpos)
print('m.lastindex: %s' % m.lastindex)
print('m.lastgroup: %s' % m.lastgroup)
print('m.group(): %s' % m.group())

print('m.group(1,2): ', m.group(1,2))
#print(m.group(1,2))
print('m.groups(): ', m.groups())
#print(m.groups())

print('m.groupdict(): %s' % m.groupdict())
print('m.start(2): %s' % m.start(2))
print('m.end(2): %s' % m.end(2))

print('m.span(2): ', m.span(2))
#print(m.span(2))

print("m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3'))
'''

'''3
import re

pattern = re.compile(r'world')
match = re.search(pattern, 'hello world!')
if match:
    print(match.group())
'''

'''4
import re

#pattern = re.compile(r'\d+')
match = re.split(r'\d+', 'one1two2three3four', 2)
print(match)
'''

#'''5
import re

pattern = re.compile(r'\d+')
match = re.findall(pattern, 'one1two2three3four')
print(match)
for item in match:
    print(item[0])
#'''

'''6
import re

pattern = re.compile(r'\d+')
match = re.finditer(pattern, 'one1two2three3four4')
for m in match:
    print(m.group(), end='')
'''

'''7
import re

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(re.sub(pattern, r'\2\1', s, 2))
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print(re.sub(pattern, func, s))
'''

'''8
import re

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print(re.subn(pattern,r'\2 \1', s))
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print(re.subn(pattern,func, s))
'''
