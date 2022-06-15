# --------------------------------------------------------------------
# -- Python Script File
# -- Created on 2022-04-26 15:19:27
# -- Author: username
# -- Comment: first attempt - don't use it!
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

oMyChannelGroups = dd.Data.GetChannelgroups("*") # Get all channelgroup names

tn = []
print('==== Check Sequence of Test Numbers ====')

for oMyChnGrp in oMyChannelGroups: 
    tn.append(oMyChnGrp.Properties("name").Value)
    
print(tn)

'''
CHnames = ["Time", "I-fuse", "Schuetz", "Freigabe", "I-Soll"]
# names equal to:   C1        C2         C3          C4 in gn (group name)

for gn in tn:
    dd.Data.Root.ChannelGroups(gn).Activate()
    index = dd.Data.Root.ActiveChannelGroup.Properties("index").Value
    CH, On = gn.split()
    CH = int(CH.split('C')[1])
    devnull, shot = On.split('_')
    
    try:
        dd.Data.Root.ChannelGroups(gn).Channels("Ampl").XRelation = dd.Data.Root.ChannelGroups(gn).Channels("Time")
        dd.Data.Root.ChannelGroups(gn).Channels("Ampl").Name = CHnames[CH]
        #dd.Data.Root.ChannelGroups(gn).Channels.Remove("Time")
    except:
        pass
'''
print('found TNs:', len(tn)) # length of tn is also index of highest group
# add new groups to the end

'''
for gn in tn:
    dd.Data.Root.ChannelGroups(gn).Activate()
    dd.MsgBoxDisp('activated group:')
    print(gn)
    index = dd.Data.Root.ActiveChannelGroup.Properties("index").Value
    CH, On = gn.split()
    CH = int(CH.split('C')[1])
    devnull, shot = On.split('_')
    print(index, shot, CH, gn)
    if CH == 1:
        dd.Data.Root.ChannelGroups.Add(shot).Activate()
        target = dd.Data.Root.ActiveChannelGroup.Properties("index").Value
        print('active group:', target)
        print('moving group:', gn, ' to target:', target)
        dd.Data.Move(dd.Data.Root.ChannelGroups(index).Channels("I-fuse")    ,dd.Data.Root.ChannelGroups(target).Channels) #,1,True)
        dd.Data.Move(dd.Data.Root.ChannelGroups(index+1).Channels("Schuetz") ,dd.Data.Root.ChannelGroups(target).Channels) #,3,True)
        dd.Data.Move(dd.Data.Root.ChannelGroups(index+2).Channels("Freigabe"),dd.Data.Root.ChannelGroups(target).Channels) #,5,True)
        dd.Data.Move(dd.Data.Root.ChannelGroups(index+3).Channels("I-Soll")  ,dd.Data.Root.ChannelGroups(target).Channels) #,7,True)
        
# re-read all data groups into tn
oMyChannelGroups = dd.Data.GetChannelgroups("*") # Get all channelgroup names
tn = []

for oMyChnGrp in oMyChannelGroups: 
    tn.append(oMyChnGrp.Properties("name").Value)

print('third part:', tn)

for gn in tn:
    if gn.startswith('C'):
        try:
            dd.Data.Root.ChannelGroups.Remove(gn)
        except:
            pass

oMyChannelGroups = dd.Data.GetChannelgroups("*") # Get all channelgroup names
dd.View.Sheets.RemoveAll() 
tn = []
for oMyChnGrp in oMyChannelGroups: 
    tn.append(oMyChnGrp.Properties("name").Value)

print('fill view with:', tn)

layoutfilename = 'I:\\HG\\Lab\\07 ELLAB\\PROJEKTE\\117-xx_(Ladesteuerung_C3)\\Highvolt_DC450kV\\11_Problematik_Einschaltstrom\\Messungen_Oszi\\FourCHlayout.TDV'
#dd.View.LoadLayout(layoutfilename)

#CHnames = ["Time", "I-fuse", "Schuetz", "Freigabe", "I-Soll"]

for gn in tn:
    dd.Data.Root.ChannelGroups(gn).Activate()
    oMySheet = dd.View.Sheets.Add(gn)
    #oMySheet = dd.View.Sheets(gn).Areas("Area : 1").DisplayObj.YScaling = "n systems [phys.]"
    oMySheet.ActiveArea.DisplayObjType = "CurveChart2D" 
    for CH in CHnames[1:]:
        oMySheet.ActiveArea.DisplayObj.Curves2D.Add(gn + '/' + 'Time' , gn + '/' + CH) 
'''