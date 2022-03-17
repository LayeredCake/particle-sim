
from System import *
from View import *

 
view = View();
s = System(view, 3, Gravity=True, Electric=False, C=0.01, vrange=(0, 0)\
, rrange=(20, 30), Drange=(0.001, 0.001))

s.run()