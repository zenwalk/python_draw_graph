from pyquery import PyQuery as pq

d = pq(url='http://v.163.com/special/Khan/probability.html')

d = d('#list2.m-clist')


def handle_down(t, idx):
    return t.find('a').attrib['href'].split('/')[-1]


def handle_title(t, idx):
    #return t.text.strip() + t.find('a').text + '.mp4'
    return '{:02d}_'.format(idx // 2 + 1) + t.find('a').text.strip() + '.mp4'


functions = {
    'u-cdown': handle_down,
    'u-ctitle': handle_title
}

l = [functions[i.attrib['class']](i, idx) for (idx, i) in enumerate(d('.u-even>td,.u-odd>td'))]

l = zip(l[::2], l[1::2])

import os
import shutil

os.chdir(r'e:\\qdownload')

for new, old in l:
    print(old, new)

    shutil.move(old, new)
