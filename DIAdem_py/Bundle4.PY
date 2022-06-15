# --------------------------------------------------------------------
# -- Python Script File
# -- Created on 2022-04-28 16:49:49
# -- Author: username
# -- Comment: analysing the group names much better
# --------------------------------------------------------------------
import sys
if 'DIAdem' in sys.modules:
    from DIAdem import Application as dd

    if dd.AppEnableScriptDebugger:
        import debugpy
        debugpy.configure(python = sys.prefix + '\\python.exe')
        if not debugpy.is_client_connected():
            try:
                debugpy.listen(5678)
            except:
                pass
            debugpy.wait_for_client()

# --------------------------------------------------------------------
# -- Beginning of user code --
#layoutfilename = 'I:\\HG\\Lab\\07 ELLAB\\PROJEKTE\\117-xx_(Ladesteuerung_C3)\\Highvolt_DC450kV\\11_Problematik_Einschaltstrom\\Messungen_Oszi\\FourCHlayout.TDV'
#dd.View.LoadLayout(layoutfilename)
alltn = []
oMyChannelGroups = dd.Data.GetChannelgroups("*On-I_*") # Get all channelgroup names
for oMyChnGrp in oMyChannelGroups: 
    alltn.append(oMyChnGrp.Properties("name").Value)
    
# create new shot groups for each C1
C1tn = []
oMyChannelGroups = dd.Data.GetChannelgroups("C1 On-I_*") # Get all channelgroup names for channel 1
for oMyChnGrp in oMyChannelGroups: 
    C1tn.append(oMyChnGrp.Properties("name").Value)

print(C1tn)

# create now new channelgroups, one for each shot, named with the 5-digit number
C1index = []
targetindex = {}
for gn in C1tn:
    C1index.append(alltn.index(gn)+1)
    CH, On = gn.split()
    CH = int(CH.split('C')[1])
    devnull, shot = On.split('_')
    dd.Data.Root.ChannelGroups.Add(shot).Activate()
    target = dd.Data.Root.ActiveChannelGroup.Properties("index").Value
    targetindex[shot] = target 

print('len targetindex: ', len(targetindex))
print(targetindex)
print(C1index)

# rename Amplitude channel with proper name
# enventually transform data into waveform, if problem with spreadsheet time axes can be resolved
# (non-equidistant error due to numeric problems with real reprensentation in CSV format)
CHnames = ["Time", "I-fuse", "Schuetz", "Freigabe", "I-Soll"]
# names equal to:   C1        C2         C3          C4 in gn (group name)

for gn in alltn:
    dd.Data.Root.ChannelGroups(gn).Activate()
    index = dd.Data.Root.ActiveChannelGroup.Properties("index").Value
    CH, On = gn.split()
    CH = int(CH.split('C')[1])
    devnull, shot = On.split('_')
    
    try:
        dd.Data.Root.ChannelGroups(gn).Channels("Ampl").XRelation = dd.Data.Root.ChannelGroups(gn).Channels("Time")
        dd.Data.Root.ChannelGroups(gn).Channels("Ampl").Name = CHnames[CH] # assignment of channel name from CHnames list
        #dd.Data.Root.ChannelGroups(gn).Channels.Remove("Time")
        # here would go some code to convert into waveform - if source data is always equidistant
    except:
        pass # do nothing if channel cannot be found

# move the channel data now to the freshly created target groups
# start with C1 and collect all other channels subsequently

for CH in range(1, 5):
    channel = 'C' + str(CH) + ' On-I_*'
    oMyChannelGroups = dd.Data.GetChannelgroups(channel) # Get all channelgroup names
    tn = []
    for oMyChnGrp in oMyChannelGroups:
        tn.append(oMyChnGrp.Properties("name").Value)

    for gn in tn:
        dd.Data.Root.ChannelGroups(gn).Activate()
        source = dd.Data.Root.ActiveChannelGroup.Properties("index").Value # get source index
        CH, On = gn.split()
        CH = int(CH.split('C')[1])
        devnull, shot = On.split('_')
        target = targetindex[shot] # get data portal group index from dict targetindex
        dd.Data.Move(dd.Data.Root.ChannelGroups(source).Channels(CHnames[CH]),dd.Data.Root.ChannelGroups(target).Channels,1,True)

# remove all groups with C in name
for gn in alltn:
    if gn.startswith('C'):
        try:
            dd.Data.Root.ChannelGroups.Remove(gn)
        except:
            pass
    

print('----')
print('len alltn: ',len(alltn))

print('number of channel groups: ', len(tn))
