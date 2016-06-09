from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 10000000
NODES = 100
NODES2 = 101
LOG_NODE = 7
MAX_POWER = 32
PARTITION = MAX_POWER - LOG_NODE


def _hash(value):
    k = md5(str(value)).digest()
    ha = unpack_from(">I", k)[0]
    return ha

ring = []
part2node = {}
part2node2 = {}

for part in range(2 ** LOG_NODE):
    ring.append(part)
    part2node[part] = part % NODES
    part2node2[part] = part % NODES2

change = 0
for item in range(ITEMS):
    h = _hash(item) >> PARTITION
    p = bisect_left(ring, h)
    p2 = bisect_left(ring, h)
    n = part2node[p] % NODES
    n2 = part2node2[p] % NODES2
    if n2 != n:
        change += 1

print("Change: %d\t(%0.2f%%)" % (change, change * 100.0 / ITEMS))
