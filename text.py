# -*- coding: utf-8 -*-
# str store bytes
# Unicode store unicode points
# Unicode strings has 'encode' method -> turns code points into bytes
# bytes string has 'decode' method -> turns bytes into code points

my_unicode= u'Hi \u2119\u01b4\u2602\u210c\xf8\u1f24'
print len(my_unicode)

my_utf8= my_unicode.encode('utf-8')
print len(my_utf8)

print my_utf8

s=my_utf8.decode('utf-8') # decode back to unicode
print type(s)

# trying chinese words
s= u'哈囉你好wwwy3y3'
for char in s:
	print char.encode('utf-8')

print s[0:3].encode('utf-8')
print s[1:5].encode('utf-8')
# pro tip 1
# Unicode sandwitch
# bytes on the outside, unicode on the inside
# encode/docode at the edge
