# --------------------------------------------------------------------
# -- Python Script File
# -- Created on 2022-04-26 17:38:03
# -- Author: username
# -- Comment: automatically open all four channels in separate views
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
dd.View.Sheets.RemoveAll() 
tn = []
for oMyChnGrp in oMyChannelGroups: 
    tn.append(oMyChnGrp.Properties("name").Value)

print('fill view with:', tn)

layoutfilename = 'I:\\HG\\Lab\\07 ELLAB\\PROJEKTE\\117-xx_(Ladesteuerung_C3)\\Highvolt_DC450kV\\11_Problematik_Einschaltstrom\\Messungen_Oszi\\FourCHlayout.TDV'
#dd.View.LoadLayout(layoutfilename)

CHnames = ["Time", "I-fuse", "Schuetz", "Freigabe", "I-Soll"]

for gn in tn:
    dd.Data.Root.ChannelGroups(gn).Activate()
    oMySheet = dd.View.Sheets.Add(gn)
    #oMySheet = dd.View.Sheets(gn).Areas("Area : 1").DisplayObj.YScaling = "n systems [phys.]"
    oMySheet.ActiveArea.DisplayObjType = "CurveChart2D" 
    for CH in CHnames[1:]:
        oMySheet.ActiveArea.DisplayObj.Curves2D.Add(gn + '/' + 'Time' , gn + '/' + CH) 
