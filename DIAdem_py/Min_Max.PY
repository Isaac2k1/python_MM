# --------------------------------------------------------------------
# -- Python Script File
# -- Created on 2022-04-26 17:38:03
# -- Author: username
# -- Comment: calculate two extrma curves for I-fuse
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
dd.Data.Root.ChannelGroups.Exists("Min_Max")
dd.Data.Root.ChannelGroups.Add("Min_Max").Activate()
dd.Data.Root.ChannelGroups("Min_Max").Channels.Add("maxima",dd.DataTypeFloat64,1)
dd.Data.Root.ChannelGroups("Min_Max").Channels.Add("minima",dd.DataTypeFloat64,2)
oMyMaxima = dd.Data.Root.ActiveChannelGroup.Channels("maxima")
oMyMinima = dd.Data.Root.ActiveChannelGroup.Channels("minima")

tn = []
for oMyChnGrp in oMyChannelGroups: 
    tn.append(oMyChnGrp.Properties("name").Value)

print('analyze these tn:', tn)

resultfilename = 'I:\\HG\\Lab\\07 ELLAB\\PROJEKTE\\117-xx_(Ladesteuerung_C3)\\Highvolt_DC450kV\\11_Problematik_Einschaltstrom\\Messungen_Oszi\\max_min.txt'

CHnames = ["Time", "I-fuse", "Schuetz", "Freigabe", "I-Soll"]
minima = []
maxima = []

for gn in tn:
    minima.append(dd.Data.Root.ChannelGroups(gn).Channels("I-fuse").Minimum)
    maxima.append(dd.Data.Root.ChannelGroups(gn).Channels("I-fuse").Maximum)

oMyMinima.SetValuesBlock(minima, 1, dd.eValueBlockValueOverwrite) 
oMyMaxima.SetValuesBlock(maxima, 1, dd.eValueBlockValueOverwrite) 

#dd.MsgBoxDisp(gn)
