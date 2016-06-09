from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 10000000
NODES = 100
VNODES = 1000
node_stat = [0 for i in range(NODES)]


def _hash(value):
    k = md5(str(value)).digest()
    ha = unpack_from(">I", k)[0]
    return ha

ring = []
hash2node = {}

for n in range(NODES):
    for v in range(VNODES):
        h = _hash(str(n) + str(v))
        ring.append(h)
        hash2node[h] = n
ring.sort()

for item in range(ITEMS):
    h = _hash(str(item))
    n = bisect_left(ring, h) % (NODES*VNODES)
    node_stat[hash2node[ring[n]]] += 1

print sum(node_stat), node_stat

_ave = ITEMS / NODES
_max = max(node_stat)
_min = min(node_stat)

print("Ave: %d" % _ave)
print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))
