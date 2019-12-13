# -*- coding: gbk -*-

from __future__ import division


content = '''
规则 1 - 估计的准确性 94.21% [加 91.3%]
	Band_3 <= 19 [ 模式: 1 ]
		Band_5 <= -89 [ 模式: 0 ] => 0
		Band_5 > -89 [ 模式: 1 ] => 1
	Band_3 > 19 [ 模式: 0 ]
		Band_2 <= 0 [ 模式: 1 ]
			Band_6 <= -92 [ 模式: 1 ]
				Band_4 <= -16 [ 模式: 1 ]
					Band_6 <= -97 [ 模式: 1 ]
						Band_1 <= -136.024 [ 模式: 0 ] => 0
						Band_1 > -136.024 [ 模式: 1 ] => 1
					Band_6 > -97 [ 模式: 0 ] => 0
				Band_4 > -16 [ 模式: 1 ] => 1
			Band_6 > -92 [ 模式: 0 ] => 0
		Band_2 > 0 [ 模式: 0 ]
			Band_3 <= 42 [ 模式: 0 ]
				Band_4 <= -19 [ 模式: 0 ]
					Band_5 <= -78 [ 模式: 0 ]
						Band_1 <= -83.944 [ 模式: 0 ] => 0
						Band_1 > -83.944 [ 模式: 1 ]
							Band_2 <= 101 [ 模式: 0 ] => 0
							Band_2 > 101 [ 模式: 1 ]
								Band_4 <= -33 [ 模式: 1 ] => 1
								Band_4 > -33 [ 模式: 1 ]
									Band_1 <= -80.558 [ 模式: 0 ] => 0
									Band_1 > -80.558 [ 模式: 1 ] => 1
					Band_5 > -78 [ 模式: 1 ] => 1
				Band_4 > -19 [ 模式: 0 ] => 0
			Band_3 > 42 [ 模式: 0 ]
				Band_4 <= -20 [ 模式: 0 ]
					Band_6 <= -86 [ 模式: 0 ]
						Band_2 <= 52 [ 模式: 0 ]
							Band_4 <= -34 [ 模式: 0 ] => 0
							Band_4 > -34 [ 模式: 0 ]
								Band_2 <= 43 [ 模式: 0 ]
									Band_1 <= -128.365 [ 模式: 1 ] => 1
									Band_1 > -128.365 [ 模式: 0 ] => 0
								Band_2 > 43 [ 模式: 1 ] => 1
						Band_2 > 52 [ 模式: 0 ] => 0
					Band_6 > -86 [ 模式: 0 ]
						Band_1 <= -79.662 [ 模式: 0 ]
							Band_6 <= -84 [ 模式: 0 ] => 0
							Band_6 > -84 [ 模式: 1 ]
								Band_3 <= 75 [ 模式: 1 ] => 1
								Band_3 > 75 [ 模式: 0 ] => 0
						Band_1 > -79.662 [ 模式: 1 ] => 1
				Band_4 > -20 [ 模式: 0 ] => 0
'''

import itertools
import StringIO



output = StringIO.StringIO()
print >> output, "# -*- coding: gbk -*-"
print >> output, "def f():"
for s in content.strip().split("\n")[1:]:
	s = s.replace(',', '')
	if s.find("=>") != -1:

		print >> output, ''.join(itertools.takewhile(lambda x: x == "\t", s)),
		print >> output, 'if ', ''.join(itertools.takewhile(lambda x: x != "[", s.lstrip())), ': return "', s[
		                                                                                                    s.find(
			                                                                                                    '=>') + 2:].strip(), '"'

	else:

		print >> output, ''.join(itertools.takewhile(lambda x: x == "\t", s)),
		print >> output, 'if ', s.lstrip()[:s.lstrip().find('[')], ":"
open("a.py", 'w').write(output.getvalue())
exec (output.getvalue())
output.close()



codes = {
	'水田': 112,
	'旱地': 122,
	'自然林': 21,
	'灌木林': 22,
	'橡胶林': 24,
	'茶园': 25,
	'绿草': 32,
	'浅草': 33,
	'水域': 41,
	'建筑用地': 51,
	'道路': 53,
	'河漫滩': 55,
	'未利用地': 65,
}

codes = {
	'0': 0,
	'1': 1,
}

import arcpy
import itertools
import numpy as np

path = r'C:/change detect/composite_bands.tif/'

sum_cnt = 0


def TileFactory(raster, tile_size):
	extent = raster.extent
	height = raster.height # no of rows
	width = raster.width # no of columns

	cell_size = raster.meanCellHeight

	x_min = extent.XMin
	y_min = extent.YMax

	x_diff = 0
	y_diff = tile_size

	x_diffs = []
	y_diffs = []

	while True:
		x_diffs.append(x_diff)
		x_diff += tile_size
		if x_diff > width:
			break

	while True:
		y_diffs.append(y_diff)
		y_diff += tile_size
		if y_diff > height:
			y_diffs.append(height)
			break

	global sum_cnt
	sum_cnt = len(x_diffs) * len(y_diff)

	for (x, y) in itertools.product(x_diffs, y_diff):
		ll = arcpy.Point(x_min + x * cell_size, y_min - y * cell_size)
		yield dict(lower_left_corner=ll, ncols=tile_size, nrows=tile_size)


names = ["Band_%d" % x for x in range(1, 7)]

print globals()['f']

def dt(x):
	#print x
	for idx, i in enumerate(names):
		#globals()[i] = round(float(x[idx]), 3)
		globals()[i] = float(x[idx])

	return codes.get(f().strip(), 0)


for (idx, arg) in enumerate(TileFactory(arcpy.Raster(path), 512)):
	print idx, '/', sum_cnt, arg

	bands = [arcpy.RasterToNumPyArray(path + x, **arg) for x in names]

	mat = np.dstack(bands)

	raster_dest = np.zeros((512, 512), dtype=np.int32)

	x_size, y_size = 512, 512

	for i in range(x_size):
		for j in range(y_size):
			#print mat[i, j]
			class_ = dt(mat[i, j])
			raster_dest[i, j] = class_

	newRaster = arcpy.NumPyArrayToRaster(raster_dest,
	                                     x_cell_size=30,
	                                     y_cell_size=30,
	                                     lower_left_corner=arg["lower_left_corner"])

	newRaster.save(r"C:\Users\chenn\Documents\ArcGIS\PercentRaster%s.tif" % idx)


