# --------------------------------------------------------------------
# -- Python Script File
# -- Created on 2020-08-31 20:28:30
# -- Author: username
# -- Comment: .
# --------------------------------------------------------------------
from DIAdem import Application as dd

if False:
    import DIAdem_CodeCompletion as dd

import time;  # This is required to include time module.

ticks = time.time()
print("======  Number of ticks since 12:00am, January 1, 1970:", ticks)

Groups = dd.Data.Root.ChannelGroups.Count
print(Groups)

for i in range(Groups):
    i +=1
    CHname = dd.Data.Root.ChannelGroups(i).Channels(1).Properties("name").Value
    maxi = dd.Data.Root.ChannelGroups(i).Channels(1).maximum
    mini = dd.Data.Root.ChannelGroups(i).Channels(1).Minimum
    print(CHname, mini, maxi)
    
# --------------------------------------------------------------------
# -- Beginning of user code --
import itertools
for values in itertools.permutations([1,2,3]):
    print (values)