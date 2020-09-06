# -----------------------------------------------------------------------------
# -- Python-Script-File
# -- Name         : ---
# -- Author       : National Instruments Ireland Resources Limited
# -- Comment      : 
# -----------------------------------------------------------------------------

import DIAdem
dd=DIAdem.Application

if False:
    import DIAdem_CodeCompletion as dd

sPathDocuments = dd.ProgramDrv + "Examples\\Documents\\"
sPathData      = dd.ProgramDrv + "Examples\\Data\\"
# -------------------------------------------------------------------------------

dd.Data.Root.Clear()
dd.DataFileLoad(sPathData + "Resampling.tdm", "TDM", "Load|ChnXYRelation")

oSource = dd.Data.GetChannel("[1]/Signal")

dd.FFTIntervPara[2] = oSource.Size
dd.ChnFFT1("", oSource)

oGroup = dd.Data.Root.ChannelGroups.Add("Result-Resampling")
oGroup.Activate()
oGroupChns = oGroup.Channels

oChnRS200 = oGroupChns.Add("Resampled_200", dd.DataTypeChnFloat64)
oChnRS200.Properties.Add("Sampling_rate_in_Hz", 200, dd.DataTypeFloat64)

oChnRS100 = oGroupChns.Add("Resampled_100", dd.DataTypeChnFloat64)
oChnRS100.Properties.Add("Sampling_rate_in_Hz", 100, dd.DataTypeFloat64)

oChnRS50  = oGroupChns.Add("Resampled_50", dd.DataTypeChnFloat64)
oChnRS50.Properties.Add("Sampling_rate_in_Hz", 50, dd.DataTypeFloat64)

oChnRS10  = oGroupChns.Add("Resampled_10", dd.DataTypeChnFloat64)
oChnRS10.Properties.Add("Sampling_rate_in_Hz", 10, dd.DataTypeFloat64)

for iLoop in range(1,5):
    dd.ChnResampleFreqBased("", oSource, oGroupChns(iLoop), oGroupChns(iLoop).Properties("Sampling_rate_in_Hz").Value, "Automatic", 0, 0)


iResampleChnCount = oGroupChns.Count

for iLoop in range(1, iResampleChnCount + 1):
    oCurrChn = oGroupChns(iLoop)
    dd.FFTIntervPara[2] = oCurrChn.Size
    dd.FFTAmplType      = "Ampl.Peak"
    dd.ChnFFT1("", oCurrChn)
    dd.Data.GetChannel("/AmplitudePeak").Name = oCurrChn.Name + "_AmplitudePeak"

dd.Report.LoadLayout(sPathDocuments + "Resampling")
dd.Report.Refresh()

oGroup = dd.Data.Root.ChannelGroups.Add("Result-Resampling_filtered")
oGroup.Activate()
oGroupChns = oGroup.Channels

oChnRS200 = oGroupChns.Add("Resampled_200", dd.DataTypeChnFloat64)
oChnRS200.Properties.Add("Sampling_rate_in_Hz", 200, dd.DataTypeFloat64)

oChnRS100 = oGroupChns.Add("Resampled_100", dd.DataTypeChnFloat64)
oChnRS100.Properties.Add("Sampling_rate_in_Hz", 100, dd.DataTypeFloat64)

oChnRS50  = oGroupChns.Add("Resampled_50", dd.DataTypeChnFloat64)
oChnRS50.Properties.Add("Sampling_rate_in_Hz", 50, dd.DataTypeFloat64)

oChnRS10  = oGroupChns.Add("Resampled_10", dd.DataTypeChnFloat64)
oChnRS10.Properties.Add("Sampling_rate_in_Hz", 10, dd.DataTypeFloat64)

for iLoop in range(1,5):
    dd.ChnResampleFreqBased("", oSource, oGroupChns(iLoop), oGroupChns(iLoop).Properties("Sampling_rate_in_Hz").Value, "Automatic", 1, 0)

