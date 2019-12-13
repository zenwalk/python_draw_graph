# -*- coding: utf-8 -*-

content = u'''
规则 1 - 估计的准确性 95.01% [加 91.9%]
	B3 <= 131.152 [ 模式: 自然林 ]
		B7 <= 0.596 [ 模式: 茶园 ]
			B9 <= 86.956 [ 模式: 绿草 ]
				B4 <= 838 [ 模式: 水域 ]
					B5 <= 20.630 [ 模式: 水域 ] => 水域
					B5 > 20.630 [ 模式: 橡胶林 ] => 橡胶林
				B4 > 838 [ 模式: 绿草 ]
					B2 <= 47.562 [ 模式: 水域 ] => 水域
					B2 > 47.562 [ 模式: 绿草 ]
						B10 <= 117 [ 模式: 绿草 ]
							B5 <= 6.730 [ 模式: 绿草 ]
								B4 <= 1,437 [ 模式: 茶园 ] => 茶园
								B4 > 1,437 [ 模式: 绿草 ] => 绿草
							B5 > 6.730 [ 模式: 绿草 ] => 绿草
						B10 > 117 [ 模式: 茶园 ] => 茶园
			B9 > 86.956 [ 模式: 茶园 ]
				B4 <= 1,395 [ 模式: 茶园 ]
					B2 <= 56.372 [ 模式: 自然林 ] => 自然林
					B2 > 56.372 [ 模式: 茶园 ]
						B4 <= 1,003 [ 模式: 橡胶林 ]
							B3 <= 125.190 [ 模式: 茶园 ] => 茶园
							B3 > 125.190 [ 模式: 橡胶林 ]
								B3 <= 128.171 [ 模式: 橡胶林 ]
									B11 <= 51 [ 模式: 橡胶林 ] => 橡胶林
									B11 > 51 [ 模式: 茶园 ] => 茶园
								B3 > 128.171 [ 模式: 橡胶林 ] => 橡胶林
						B4 > 1,003 [ 模式: 茶园 ]
							B5 <= 18.780 [ 模式: 茶园 ]
								B9 <= 146.484 [ 模式: 茶园 ] => 茶园
								B9 > 146.484 [ 模式: 浅草 ] => 浅草
							B5 > 18.780 [ 模式: 浅草 ]
								B7 <= 0.491 [ 模式: 绿草 ] => 绿草
								B7 > 0.491 [ 模式: 浅草 ] => 浅草
				B4 > 1,395 [ 模式: 浅草 ] => 浅草
		B7 > 0.596 [ 模式: 自然林 ]
			B2 <= 59.895 [ 模式: 自然林 ]
				B4 <= 1,852 [ 模式: 自然林 ] => 自然林
				B4 > 1,852 [ 模式: 浅草 ] => 浅草
			B2 > 59.895 [ 模式: 灌木林 ]
				B7 <= 0.605 [ 模式: 橡胶林 ] => 橡胶林
				B7 > 0.605 [ 模式: 灌木林 ] => 灌木林
	B3 > 131.152 [ 模式: 橡胶林 ]
		B9 <= 101.394 [ 模式: 建筑用地 ]
			B1 <= 135.231 [ 模式: 水域 ] => 水域
			B1 > 135.231 [ 模式: 建筑用地 ]
				B11 <= 24 [ 模式: 水田 ] => 水田
				B11 > 24 [ 模式: 建筑用地 ]
					B11 <= 248 [ 模式: 建筑用地 ]
						B4 <= 1,178 [ 模式: 建筑用地 ] => 建筑用地
						B4 > 1,178 [ 模式: 建筑用地 ]
							B6 <= 278.130 [ 模式: 建筑用地 ] => 建筑用地
							B6 > 278.130 [ 模式: 旱地 ] => 旱地
					B11 > 248 [ 模式: 道路 ] => 道路
		B9 > 101.394 [ 模式: 橡胶林 ]
			B3 <= 155.002 [ 模式: 橡胶林 ]
				B9 <= 235.245 [ 模式: 橡胶林 ]
					B2 <= 68.705 [ 模式: 水田 ] => 水田
					B2 > 68.705 [ 模式: 橡胶林 ]
						B4 <= 572 [ 模式: 水田 ] => 水田
						B4 > 572 [ 模式: 橡胶林 ]
							B11 <= 165 [ 模式: 橡胶林 ]
								B5 <= 28.632 [ 模式: 橡胶林 ]
									B2 <= 70.467 [ 模式: 橡胶林 ]
										B3 <= 137.115 [ 模式: 橡胶林 ] => 橡胶林
										B3 > 137.115 [ 模式: 水田 ] => 水田
									B2 > 70.467 [ 模式: 橡胶林 ] => 橡胶林
								B5 > 28.632 [ 模式: 绿草 ] => 绿草
							B11 > 165 [ 模式: 道路 ] => 道路
				B9 > 235.245 [ 模式: 灌木林 ]
					B4 <= 534 [ 模式: 灌木林 ] => 灌木林
					B4 > 534 [ 模式: 灌木林 ]
						B4 <= 611 [ 模式: 水田 ] => 水田
						B4 > 611 [ 模式: 灌木林 ] => 灌木林
			B3 > 155.002 [ 模式: 未利用地 ]
				B4 <= 785 [ 模式: 未利用地 ]
					B2 <= 116.275 [ 模式: 未利用地 ]
						B9 <= 130.602 [ 模式: 道路 ]
							B11 <= 228 [ 模式: 道路 ]
								B4 <= 558 [ 模式: 道路 ] => 道路
								B4 > 558 [ 模式: 未利用地 ]
									B3 <= 160.965 [ 模式: 道路 ] => 道路
									B3 > 160.965 [ 模式: 未利用地 ] => 未利用地
							B11 > 228 [ 模式: 河漫滩 ] => 河漫滩
						B9 > 130.602 [ 模式: 未利用地 ]
							B5 <= 10.648 [ 模式: 未利用地 ] => 未利用地
							B5 > 10.648 [ 模式: 橡胶林 ] => 橡胶林
					B2 > 116.275 [ 模式: 河漫滩 ]
						B1 <= 315.564 [ 模式: 河漫滩 ]
							B1 <= 259.210 [ 模式: 河漫滩 ] => 河漫滩
							B1 > 259.210 [ 模式: 河漫滩 ]
								B10 <= 121 [ 模式: 河漫滩 ]
									B4 <= 537 [ 模式: 河漫滩 ] => 河漫滩
									B4 > 537 [ 模式: 未利用地 ] => 未利用地
								B10 > 121 [ 模式: 河漫滩 ] => 河漫滩
						B1 > 315.564 [ 模式: 道路 ] => 道路
				B4 > 785 [ 模式: 道路 ]
					B11 <= 29 [ 模式: 旱地 ] => 旱地
					B11 > 29 [ 模式: 道路 ] => 道路
'''

from itertools import takewhile


def to_envi(s):
	s = s.replace('<=', 'LE')
	s = s.replace('>', 'LT')
	return s


codes = {
    u"水田": 112, u'旱地': 122,
    u'自然林': 21, u'灌木林': 22,
    u'橡胶林': 24, u'茶园': 25,
    u'绿草': 32, u"浅草": 33,
    u'水域': 41, u'建筑用地': 51,
    u'道路': 53, u'河漫滩': 55,
    u'未利用地': 65
}


class Node():
	def __init__(self, s, code, location1, location2):

		if s.find(u"规则") != -1:
			self.type = 'Root'
			print 'Root'
		elif s.find('=>') != -1:
			self.type = 'Result'
			self.calculate = to_envi(s.strip()[:s.strip().find('[')])
		else:
			self.type = 'Decision'

		if self.type == 'Decision':
			self.calculate = to_envi(s.strip()[:s.strip().find('[')])
			#self.expression = line.strip()[:line.strip().find('[')]

		if self.type == 'Result':
			self.target = s[s.find('=>')+2:]

		self.code = code

		self.location = (location1, location2)


	def class_value(self):

		return codes[self.target.strip()]



s = content.strip().split('\n')

from itertools import takewhile
import string

is_space = lambda x: x in string.whitespace or x in ':.'

get_head = lambda line: list(takewhile(is_space, line))

#s = open('g:/Cultivated Land.out').readlines()[10:98]

heads = list(len(get_head(line)) + 1 for line in s)



