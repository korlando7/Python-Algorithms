# Uses python3
import sys
from collections import namedtuple
from operator import itemgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
	points = []

	while len(segments) > 0:
		x = min(segments, key=itemgetter(1))
		min_end = x.end
		
		for s in segments:
			if min_end > s.start:
				print (s)
				segments.remove(s)
			else:
				
	return points   

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    # print(len(points))
    # for p in points:
    #     print(p, end=' ')
    print (points)