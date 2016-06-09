from hashlib import md5
from struct import unpack_from

ITEMS = 10000000
NODES = 100

node_stat = [0 for i in range(NODES)]

for item in range(ITEMS):
    k = md5(str(item)).digest()
    h = unpack_from(">I", k)[0]
    n = h % NODES
    node_stat[n] += 1

_ave = ITEMS / NODES
_max = max(node_stat)
_min = min(node_stat)

print("Ave: %d" % _ave)
print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))
