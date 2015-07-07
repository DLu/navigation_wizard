
import sys
import rosbag
import collections

bag = rosbag.Bag(sys.argv[1])
S = collections.defaultdict(set)

for topic, msg, t in bag.read_messages():
    S[msg._type].add(topic)
    if 'Odom' in msg._type:
        print topic, msg
        print
bag.close()

S2 = {}
for a,b in S.iteritems():
    S2[a] = list(b)

print S2

