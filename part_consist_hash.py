from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 10000000
NODES = 100
LOG_NODE = 7
MAX_POWER = 32
PARTITION = MAX_POWER - LOG_NODE
node_stat = [0 for i in range(NODES)]


def _hash(value):
    k = md5(str(value)).digest()
    ha = unpack_from(">I", k)[0]
    return ha

ring = []
part2node = {}

for part in range(2 ** LOG_NODE):
    ring.append(part)
    part2node[part] = part % NODES

for item in range(ITEMS):
    h = _hash(item) >> PARTITION
    part = bisect_left(ring, h)
    n = part % NODES
    node_stat[n] += 1

_ave = ITEMS / NODES
_max = max(node_stat)
_min = min(node_stat)

print("Ave: %d" % _ave)
print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))
