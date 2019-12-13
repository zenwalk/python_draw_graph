# -*- coding: utf-8 -*-

__author__ = 'chenn'

from pprint import pprint
import itertools

def left_idx(cur):
	return cur * 2


def right_idx(cur):
	return cur * 2 + 1


import math


def level(cur):
	return int(math.floor(math.log(float(cur), 2))) + 1


def do_pre_order(cur, f):
	if cur <= 2 ** 16:
		f((cur, level(cur), cur - 2 ** (level(cur) - 1) + 1))
		do_pre_order(left_idx(cur), f)
		do_pre_order(right_idx(cur), f)


def pre_order(f):
	do_pre_order(1, f)


from spss_tree import heads

idx = 0
result = []


def cursor(x):
	#print x[1]
	global idx

	if idx < len(heads) and x[1] == heads[idx]:
		#print x[1:]
		result.append(x)
		idx += 1

pre_order(cursor)

print len(result)

from spss_tree import Node, s

nodes = [Node(line, code, x, y) for ((code, x, y), line) in zip(result, s)]

# update the expression for envi tree output
for node in nodes:

	if node.type != "Decision":
		continue

	leftChild = node.code * 2
	#x = itertools.dropwhile(lambda x: x.code == leftChild, iter(nodes))
	for node2 in nodes:
		if node2.code == leftChild:
			node.calculate = node2.calculate



from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('myTree', '.'))
template = env.get_template('envi.jinja2')

#print template.render(nodes=nodes)

open('f.txt', 'w').write(template.render(nodes=nodes))

nodes = []
for i in result:
	nodes.append((i[0] / 2, i[0]))

template = env.get_template('graphviz.dot')
open('a.dot', 'w').write(template.render(nodes=nodes))