# IAAPP.py

import wx
import wx.xrc

import winsound
import rtmidi
import threading

import sys

import queue
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
from scipy.fftpack import fft


# MIC stream open ....
def CaptureMIC():

    global MICSampleRate
    global SoundData
    # global MICSamplePeriod
    global Channels
    global NotesParameters
    #global TempFile

    lastdata = 0

    with sd.InputStream(  # Open MIC stream
                device=Device, channels=max(Channels),
                samplerate=MICSampleRate, callback=audio_callback):

        # print("MIC capture callback in place")
        while True:
            wx.MilliSleep(200)      # sleep a while for main APP to work

            if EnableMICCapture:
                pass
            else:
                print("End MIC capture")
                break

            while True:             # proces the notes we captured. Each notes should be 1/64 note which is 1/16 beat
                try:
                    data = NoteQ.get_nowait()
                    #print('Get ', NoteQ.qsize(), 'units of note',data)
                    #if (data!= lastdata):
                        #TempFile.write('\n')        # save different line for different note

                    #TempFile.write(((NotesParameters[data])[0])[:3]+',')
                    lastdata = data
                except queue.Empty:
                    print('.')
                    break


##
#
# TuningFrame Tuning frame which generate by wxFormBuilder
#
##

class TuningFrame ( wx.Frame ):

    def __init__( self, parent ):
        # Next 2 lines are not generate by wxFormBuilder
        global NotesParameters
        global TuningNoteIndex


        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tuning ......", pos = wx.DefaultPosition,
                            size = wx.Size( 425,225 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizerTuningDialog = wx.BoxSizer( wx.VERTICAL )

        bSizerTuneNote = wx.BoxSizer( wx.HORIZONTAL )

        self.staticTextTuneNote = wx.StaticText( self, wx.ID_ANY, u"Tuning Note:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.staticTextTuneNote.Wrap( -1 )

        bSizerTuneNote.Add( self.staticTextTuneNote, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

        listBoxTuneNoteChoices = [ ]
        # Next for block not generate by wxFormBuilder
        for i in range(len(NotesParameters)):
            str1 = ((NotesParameters[i])[0])[:3] + ' - ' + str((NotesParameters[i])[1]) + 'Hz'
            listBoxTuneNoteChoices.append(str1)
            if (((NotesParameters[i])[0])[:3] == 'A4 '):
                TuningNoteIndex = i

        self.listBoxTuneNote = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,55 ),
                                           listBoxTuneNoteChoices, wx.LB_SINGLE )
        bSizerTuneNote.Add( self.listBoxTuneNote, 0, wx.ALL, 8 )

        self.buttonPlayTuneNote = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                                   wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )

        self.buttonPlayTuneNote.SetBitmap( wx.Bitmap( u"../src/triAngle.bmp", wx.BITMAP_TYPE_ANY ) )
        # remove next 3 lines which generate by wxFormBuild
        # self.buttonPlayTuneNote.SetBitmapDisabled( wx.NullBitmap )
        # self.buttonPlayTuneNote.SetBitmapPressed( wx.NullBitmap )
        # self.buttonPlayTuneNote.SetBitmapCurrent( wx.NullBitmap )
        bSizerTuneNote.Add( self.buttonPlayTuneNote, 0, wx.ALL, 5 )


        bSizerTuningDialog.Add( bSizerTuneNote, 1, wx.EXPAND, 5 )


        bSizerTuningDialog.Add( ( 0, 0), 1, wx.EXPAND, 0 )

        bSizerTuneSound = wx.BoxSizer( wx.HORIZONTAL )

        self.staticTextTuneSound = wx.StaticText(self, wx.ID_ANY, u"Tuning Sound:", wx.DefaultPosition, wx.DefaultSize,
                                                 0)
        self.staticTextTuneSound.Wrap(-1)

        bSizerTuneSound.Add(self.staticTextTuneSound, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.textCtrlTuneSoundFreq = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, -1),
                                                 0)
        bSizerTuneSound.Add(self.textCtrlTuneSoundFreq, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        self.staticTextTuningHz = wx.StaticText(self, wx.ID_ANY, u"Hz ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextTuningHz.Wrap(-1)

        bSizerTuneSound.Add(self.staticTextTuningHz, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        self.textCtrlTuningDN = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        bSizerTuneSound.Add(self.textCtrlTuningDN, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        self.sliderTuneSoundPre = wx.Slider(self, wx.ID_ANY, 0, -100, 100, wx.DefaultPosition, wx.Size( 150,-1 ),
                                            wx.SL_HORIZONTAL|wx.SL_VALUE_LABEL )
        bSizerTuneSound.Add(self.sliderTuneSoundPre, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        self.textCtrlTuningUN = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(40, -1), 0)
        bSizerTuneSound.Add(self.textCtrlTuningUN, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        bSizerTuningDialog.Add(bSizerTuneSound, 1, wx.EXPAND, 0)

        bSizerNote = wx.BoxSizer(wx.HORIZONTAL)

        self.staticTextTSBlank = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(235, -1), 0)
        self.staticTextTSBlank.Wrap(-1)

        bSizerNote.Add(self.staticTextTSBlank, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.textCtrlTuningSoundNote = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1),
                                                   0)
        self.textCtrlTuningSoundNote.SetMaxLength(8)
        bSizerNote.Add(self.textCtrlTuningSoundNote, 0, wx.ALIGN_CENTER | wx.ALL, 3)

        bSizerTuningDialog.Add(bSizerNote, 1, wx.EXPAND, 0)


        self.SetSizer( bSizerTuningDialog )
        self.Layout()
        self.tuningTimer = wx.Timer()
        self.tuningTimer.SetOwner( self, wx.ID_ANY )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.TuningFrameOnClose )
        self.listBoxTuneNote.Bind( wx.EVT_LISTBOX, self.listBoxTuneNoteOnListBox )
        self.buttonPlayTuneNote.Bind( wx.EVT_BUTTON, self.buttonPlayTuneNoteOnButtonClick )
        self.Bind( wx.EVT_TIMER, self.tuningTimerOnTimer, id=wx.ID_ANY )

        # ------------ Add widget program settings
        #print(TuningNoteIndex)
        self.listBoxTuneNote.SetSelection(TuningNoteIndex)  # set default selection item
        self.tuningTimer.Start(TuningTimer_INT)
        # ------------ Call Populates

        self.Show()

        # ------------ Event handlers

    # Virtual event handlers, override them in your derived class
    def TuningFrameOnClose(self, event):
        global TuneEnable
        global EnableMICCapture
        # global TempFile

        TuneEnable = False
        EnableMICCapture = False  # capture MIC data
        print("Tuning closed")
        wx.MilliSleep(300)          # Sleep for MIC capture function to stop then close the file
        self.tuningTimer.Stop()
        #TempFile.close()
        #print('temp file closed')

        #self.Destroy()
        event.Skip()

    def listBoxTuneNoteOnListBox(self, event):
        global TuningNoteIndex

        TuningNoteIndex = self.listBoxTuneNote.GetSelection()
        # print(TuningNoteIndex)
        event.Skip()

    def buttonPlayTuneNoteOnButtonClick(self, event):
        global TuneEnable
        global TickNowMS
        global NoteTickNowMS

        # self.buttonPlayTuneNote.SetBitmapCurrent(wx.Bitmap(u"../src/retangle.bmp", wx.BITMAP_TYPE_ANY))
        if TuneEnable:
            TuneEnable = False
        else:
            TuneEnable = True

        if TuneEnable:
            self.buttonPlayTuneNote.SetBitmap(wx.Bitmap(u"../src/retangle.bmp", wx.BITMAP_TYPE_ANY))
            NoteTickNowMS = TickNowMS = IAStopWatch.Time()
        else:
            self.buttonPlayTuneNote.SetBitmap(wx.Bitmap(u"../src/triangle.bmp", wx.BITMAP_TYPE_ANY))
        event.Skip()

    #
    # Timer event for tuning
    #
    def tuningTimerOnTimer( self, event ):
        global NoteMS
        global SoundData
        global Q
        global MICSampleNum
        global tuneFrame
        global MICSampleCnt
        global NoteTickNowMS
        global NoteTickLastMS
        global MinNotePeriod

        while True:
            try:
                data = Q.get_nowait()
                shift = len(data)
                MICSampleCnt += shift

                #print('length data', shift)
                SoundData = np.roll(SoundData, -shift, axis=0)
                SoundData[-shift:, :] = data


            except queue.Empty:
                break

        # print('Min Note',MinNotePeriod)
        NoteTickLastMS = NoteTickNowMS
        NoteTickNowMS = IAStopWatch.Time()  # Get current stop watch time in ms
        tickDiff = (NoteTickNowMS - NoteTickLastMS)
        NoteMS = NoteMS + tickDiff  # how many ms past after start MIC capture
        #MICSlice = MinNotePeriod * MICSampleRate

        if (EnableMICCapture and (NoteMS >= MinNotePeriod * 16) and MICSampleCnt>0):   # 1/64 note as a unit

            # MICSampleNum = int (MICSampleRate * NoteMS/1000)

            NoteMS = 0

            signalSlice = [0] * MICSampleNum
            #testSFile = open('sound.tmp', "a")
            #testSFile.write('\n================ ' + str(MICSampleCnt) + '\n')
            for i in range(MICSampleCnt):
                signalSlice[i] = SoundData[MICSampleNum-MICSampleCnt-1+i][0]  # convert numpy array to sound data buffer

            #for i in range (MICSampleNum):
            #    testSFile.write(str(signalSlice[i])+'/'+str(i)+';')
            #    if ((i%20) == 0):
            #        testSFile.write('\n')

            #testSFile.close()

            fd = np.linspace(0.0, MICSampleRate, MICSampleNum, endpoint=False)
            #fd = np.fft.fftfreq(MICSampleNum, 1 / MICSampleRate)    # Return the Discrete Fourier Transform sample frequencies.

            #print('num',MICSampleNum,'NoteMS',NoteMS,(NoteTickNowMS - NoteTickLastMS),MICSampleCnt)
            # MICSampleNum = int(MICSampleRate * NoteMS / 1000)
            # print('get ',MICSampleCnt,' sound data.', NoteMS)

            freqSpectrum = fft(signalSlice)
            mag = np.abs(freqSpectrum)  # Magnitude
            # mag = 2 / MICSampleNum * np.abs(freqSpectrum)  # Magnitude

            nextFreq = centerFreq = fd[0]
            nextMag = centerFreqMag = mag[0]
            #testFile = open('test.tmp', "a")
            #testFile.write('================ '+str(MICSampleCnt)+'\n')

            for i in range(int(MICSampleNum / 2)):
                #if (mag[i]>=1):     # check the FFT result which value >= 6
                #    testFile.write('['+str(int(fd[i]))+'/')
                #    testFile.write(str(mag[i])+']')
                if (mag[i] > centerFreqMag):
                    #nextFreq = centerFreq
                    centerFreq = fd[i]
                    #nextMag = centerFreqMag
                    centerFreqMag = mag[i]
                    #indo = i


            #testFile.write('\n+++++++++++++++++ ['+str(centerFreq)+ '/'+str(centerFreqMag)+']\n')
            #testFile.close()
            # MICSampleNum = 0


            if (centerFreqMag >= 0.6):  # accept only magnitude (loudness) more than certain level
                tuneFrame.textCtrlTuneSoundFreq.SetValue(str(centerFreq))
                if (centerFreq < NotesParameters[len(NotesParameters)-1][1] and centerFreq > NotesParameters[0][1]):
                    for i in range(1,len(NotesParameters)):     # linear searh for the note name
                        if( centerFreq <= ((NotesParameters[i])[1])  and centerFreq > ((NotesParameters[i-1])[1])):
                            break
                    #print(i,((NotesParameters[i])[0]),((NotesParameters[i])[1]))

                    du = abs(centerFreq-((NotesParameters[i])[1]))
                    dd = abs(centerFreq-((NotesParameters[i-1])[1]))
                    if (du<=dd):
                        index = i
                        diff = -1*du/(((NotesParameters[index])[1])-((NotesParameters[index-1])[1]))
                    else:
                        index = i-1
                        diff = -1 * dd / (((NotesParameters[index])[1]) - ((NotesParameters[index + 1])[1]))


                    str1 =  ((NotesParameters[index])[0])[:3] + ' / ' + str(int(diff*100)) + 'C'

                    tuneFrame.textCtrlTuningSoundNote.SetValue(str1)    # display the note of the center freq
                    #print(f' Mag. = {centerFreqMag} Center Freq = {centerFreq},index = {indo}, ', str1)
                    if (index>0):   # prevent to access out of the NotesParameters array
                        tuneFrame.textCtrlTuningDN.SetValue(((NotesParameters[index-1])[0])[:3])

                    if (index < (len(NotesParameters)-1)): # prevent to access out of the NotesParameters array
                        tuneFrame.textCtrlTuningUN.SetValue(((NotesParameters[index + 1])[0])[:3])
                    tuneFrame.sliderTuneSoundPre.SetValue(int(diff*100))

                    NoteQ.put(index)  # store the note we captured in Note Queue
                    testFile = open('testfreq.tmp', "w",buffering = MICSampleNum)
                    #print('================')
                    for i in range(MICSampleCnt):
                        testFile.write(str(signalSlice[i]))
                        #if i<10:
                            #print(str(signalSlice[i]))
                    testFile.flush()
                    testFile.close()

                    # print('Primary Frequency = ', centerFreq,index)

            MICSampleCnt = 0

        event.Skip()

class BeatFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Beat ......", pos = wx.DefaultPosition,
                            size = wx.Size( 268,185 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizerBeatDialog = wx.BoxSizer( wx.VERTICAL )

        self.staticTextSetBeat = wx.StaticText( self, wx.ID_ANY, u"Beat Setting....", wx.DefaultPosition,
                                                wx.DefaultSize, 0 )
        self.staticTextSetBeat.Wrap( -1 )

        bSizerBeatDialog.Add( self.staticTextSetBeat, 0, wx.ALL, 5 )

        bSizerBeatSetting = wx.BoxSizer( wx.HORIZONTAL )

        self.staticTextBeatSpeed = wx.StaticText( self, wx.ID_ANY, u"Beat Speed :", wx.DefaultPosition,
                                                  wx.DefaultSize, 0 )
        self.staticTextBeatSpeed.Wrap( -1 )

        bSizerBeatSetting.Add( self.staticTextBeatSpeed, 0, wx.ALL, 5 )

        self.spinCtrlBeatSpeed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                              wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 30, 500, 60 )
        bSizerBeatSetting.Add( self.spinCtrlBeatSpeed, 0, wx.ALL, 3 )


        bSizerBeatDialog.Add( bSizerBeatSetting, 0, wx.EXPAND, 5 )

        bSizerBeatSound = wx.BoxSizer( wx.HORIZONTAL )

        self.staticTextBeatSpeed1 = wx.StaticText( self, wx.ID_ANY, u"Beat Sound :", wx.DefaultPosition,
                                                   wx.DefaultSize, 0 )
        self.staticTextBeatSpeed1.Wrap( -1 )

        bSizerBeatSound.Add( self.staticTextBeatSpeed1, 0, wx.ALL, 5 )

        self.spinCtrlBeatSound = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                              wx.SP_ARROW_KEYS, 27, 87, 62 )
        bSizerBeatSound.Add( self.spinCtrlBeatSound, 0, wx.ALL, 3 )


        bSizerBeatDialog.Add( bSizerBeatSound, 1, wx.EXPAND, 0 )

        bSizerBeatPanel = wx.BoxSizer( wx.VERTICAL )

        self.checkBoxEnableBeat = wx.CheckBox( self, wx.ID_ANY, u"Beat", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.checkBoxEnableBeat.SetValue(True)
        bSizerBeatPanel.Add( self.checkBoxEnableBeat, 0, wx.ALL, 10 )

        self.buttonBeatOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerBeatPanel.Add( self.buttonBeatOK, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizerBeatDialog.Add( bSizerBeatPanel, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizerBeatDialog )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.BeatFrameOnClose )
        self.spinCtrlBeatSpeed.Bind( wx.EVT_SPINCTRL, self.spinCtrlBeatSpeedOnSpinCtrl )
        self.spinCtrlBeatSpeed.Bind( wx.EVT_TEXT_ENTER, self.spinCtrlBeatSpeedOnTextEnter )
        self.spinCtrlBeatSound.Bind( wx.EVT_SPINCTRL, self.spinCtrlBeatSoundOnSpinCtrl )
        self.checkBoxEnableBeat.Bind( wx.EVT_CHECKBOX, self.checkBoxEnableBeatOnCheckBox )
        self.buttonBeatOK.Bind( wx.EVT_BUTTON, self.buttonBeatOKOnButtonClick )

        # ------------ Add widget program settings
        self.spinCtrlBeatSpeed.SetValue(BeatSpeed)
        self.spinCtrlBeatSound.SetValue(BeatMidiNote2)
        self.checkBoxEnableBeat.SetValue(BeatEnable)
        # ------------ Call Populates

        self.Show()

        # ------------ Event handlers

    # Virtual event handlers, override them in your derived class
    def BeatFrameOnClose(self, event):
        event.Skip()

    def spinCtrlBeatSpeedOnSpinCtrl(self, event):
        global BeatSpeed

        BeatSpeed = self.spinCtrlBeatSpeed.GetValue()
        event.Skip()

    def spinCtrlBeatSpeedOnTextEnter(self, event):
        global BeatSpeed

        BeatSpeed = self.spinCtrlBeatSpeed.GetValue()
        event.Skip()

    def spinCtrlBeatSoundOnSpinCtrl(self, event):
        global BeatMidiNote2

        BeatMidiNote2 = self.spinCtrlBeatSound.GetValue()
        event.Skip()

    def checkBoxEnableBeatOnCheckBox(self, event):
        global BeatEnable
        global TickNowMS

        BeatEnable = self.checkBoxEnableBeat.GetValue()
        TickNowMS = IAStopWatch.Time()

        event.Skip()

    def buttonBeatOKOnButtonClick(self, event):
        global BeatEnable
        global BeatSpeed
        global BeatMidiNote2

        BeatEnable = self.checkBoxEnableBeat.GetValue()
        BeatSpeed = self.spinCtrlBeatSpeed.GetValue()
        BeatSound = self.spinCtrlBeatSound.GetValue()

        self.Destroy()
        event.Skip()


class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Instrumentalist Assistance",
                            pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.menubarMain = wx.MenuBar( 0 )
        self.menuFile = wx.Menu()
        self.menuItemFileOpen = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Open"+ u"\t" + u"Ctrl-O", wx.EmptyString,
                                             wx.ITEM_NORMAL )
        self.menuFile.Append( self.menuItemFileOpen )

        self.menuItemFileSave = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl-S", wx.EmptyString,
                                             wx.ITEM_NORMAL )
        self.menuFile.Append( self.menuItemFileSave )

        self.menuItemFileSaveAs = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Save As..."+ u"\t" + u"Ctrl-A",
                                               u"Save current file as a new one", wx.ITEM_NORMAL )
        self.menuFile.Append( self.menuItemFileSaveAs )

        self.menuFile.AppendSeparator()

        self.menuItemFileExit = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.menuFile.Append( self.menuItemFileExit )

        self.menubarMain.Append( self.menuFile, u"File" )

        self.menuTools = wx.Menu()
        self.menuItemToolsBeat = wx.MenuItem( self.menuTools, wx.ID_ANY, u"Beat"+ u"\t" + u"Alt-B",
                                              u"Set beat parameter", wx.ITEM_NORMAL )
        self.menuTools.Append( self.menuItemToolsBeat )

        self.menuItemToolsTuning = wx.MenuItem( self.menuTools, wx.ID_ANY, u"Tuning"+ u"\t" + u"Alt-T",
                                                u"Tuning your instrument", wx.ITEM_NORMAL )
        self.menuTools.Append( self.menuItemToolsTuning )

        self.menubarMain.Append( self.menuTools, u"Tools" )

        self.menuHelp = wx.Menu()
        self.menuItemHelpAbout = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"About"+ u"\t" + u"Alt-A",
                                              u"About the application", wx.ITEM_NORMAL )
        self.menuHelp.Append( self.menuItemHelpAbout )

        self.menubarMain.Append( self.menuHelp, u"Help" )

        self.SetMenuBar( self.menubarMain )

        self.statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        bSizerFrame = wx.BoxSizer( wx.VERTICAL )

        self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizerMainPanel = wx.BoxSizer( wx.VERTICAL )


        self.panelMain.SetSizer( bSizerMainPanel )
        self.panelMain.Layout()
        bSizerMainPanel.Fit( self.panelMain )
        bSizerFrame.Add( self.panelMain, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizerFrame )
        self.Layout()
        self.appTimer = wx.Timer()
        self.appTimer.SetOwner( self, wx.ID_ANY )
        # self.appTimer.Start( 1000 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.menuItemOpenOnMenuSelection, id = self.menuItemFileOpen.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItemSaveOnMenuSelection, id = self.menuItemFileSave.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItemSaveAsOnMenuSelection, id = self.menuItemFileSaveAs.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItemExitOnMenuSelection, id = self.menuItemFileExit.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItemBeatOnMenuSelection, id = self.menuItemToolsBeat.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItemTuningOnMenuSelection, id = self.menuItemToolsTuning.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItemAboutOnMenuSelection, id = self.menuItemHelpAbout.GetId() )
        self.Bind( wx.EVT_TIMER, self.appTimerOnTimer, id=wx.ID_ANY )

        # ------------ Add widget program settings
        self.appTimer.Start(TIMER_INT)  # Set Timer interval

        global IAStopWatch
        global MidiOut

        IAStopWatch.Start(0)  # start stop watch
        midiPort = MidiOut.get_ports()  # Prepare MIDI for beat sound
        print(f"Midi Port {midiPort}")
        if midiPort == 0:
            print('Error:no MIDI port')
        else:
            if MidiOut.open_port(0) == 0:
                print('Error: can not open MIDI port')
            else:
                print('MIDI port open')

        global NotesParameters

        # print('Note:',(NotesParameters[1])[0],(NotesParameters[1])[1],(NotesParameters[1])[2])
        # str1 = ((NotesParameters[1])[0])[:3] + ' - ' + str((NotesParameters[1])[1]) +'Hz'
        # print('Note:',str1 )

        # ------------ Call Populates

        self.Show()

        # ------------ Event handlers

    # Virtual event handlers, override them in your derived class
    def menuItemOpenOnMenuSelection(self, event):

        event.Skip()

    def menuItemSaveOnMenuSelection(self, event):
        event.Skip()

    def menuItemSaveAsOnMenuSelection(self, event):
        event.Skip()

    def menuItemExitOnMenuSelection(self, event):
        MidiOut.close_port()
        MidiOut.delete()
        self.appTimer.Stop()

        event.Skip()

    def menuItemBeatOnMenuSelection(self, event):
        global TuneEnable

        TuneEnable = False
        beatFrame = BeatFrame(self)

        event.Skip()

    def menuItemTuningOnMenuSelection(self, event):
        global BeatEnable
        global EnableMICCapture
        global NoteMS
        global tuneFrame
        global NoteTickNowMS
        #global TempFile

        #TempFile = open('temp.tmp', "w")

        BeatEnable = False  # When enter tuning mode turn off the beat sound

        EnableMICCapture = True  # start MIC capture in background
        NoteTickNowMS = IAStopWatch.Time()
        NoteMS = 0
        t = threading.Thread(target=CaptureMIC)
        t.start()  # MIC capture task start in background

        tuneFrame = TuningFrame(self)

        event.Skip()

    def menuItemAboutOnMenuSelection(self, event):
        event.Skip()

        ##
        #
        #    Timer event, Timer event generate every TIMER_INT (ms) to sound the beat.
        #
        ##

    def appTimerOnTimer(self, event):
        global TickNowMS
        global TickLastMS
        global TickMS
        global BeatSpeed
        global Counter

        TickLastMS = TickNowMS
        TickNowMS = IAStopWatch.Time()  # Get current stop watch time in ms
        tickDiff = (TickNowMS - TickLastMS)
        TickMS = TickMS + tickDiff  # how many ms past after start beat sound

        if (TuneEnable and TickMS > 3000):
            # print(TuningNoteIndex)
            note_on = [0x90, (NotesParameters[TuningNoteIndex])[2],
                       0x7f]  # simulate piano to play the note to tune your instrument
            MidiOut.send_message(note_on)
            TickMS = 0

        if BeatEnable:
            beatTick = (60 / BeatSpeed) * 1000  # The period of each beat in ms

            if (TickMS < (beatTick - (TIMER_INT / 2))):
                return

            if MidiOut:  # If MIDI port open use MIDI to beat

                note_on = [0x99, BeatMidiNote2, 0x7F]  # MIDI message of beat sound
                MidiOut.send_message(note_on)
                Counter += 1
            else:  # If MIDI port can not open use windows Beep to beat
                winsound.Beep(800, 20)  # Windows Beep() function
            # print('Real interval:', TickMS, 'ms,Sets interval: ', beatTick, 'ms')
            TickMS = 0

        event.Skip()

def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)

    # if EnableMICCapture:            # When Tunning or listen the player play then capture the sound from MIC

    Q.put(indata)
    #print('capture:',len(indata))
    # print('.')

# main()
#
if __name__ == "__main__":
    # The first note that MIDI can generate is C0, Frequency is 16.35Hz,
    # each note times 1.0594 will be next note Freq
    # Frequency less than 20Hz Human should could not hear it.
    #
    NotesParameters = (  # [Note Name , Frequency , MIDI Byte2]     # non changeable list using tuples
        ['C0 ', 16.35, 12],  # C0             0
        ['C#0', 17.32, 13],  # C#0/Db0        1
        ['D0 ', 18.35, 14],  # D0             2
        ['D#0', 19.45, 15],  # D#0/Eb0        3
        ['E0 ', 20.60, 16],  # E0             4
        ['F0 ', 21.83, 17],  # F0             5
        ['F#0', 23.12, 18],  # F#0/Gb0        6
        ['G0 ', 24.50, 19],  # G0             7
        ['G#0', 25.96, 20],  # G#0/Ab0
        ['A0 ', 27.50, 21],  # A0
        ['A#0', 29.14, 22],  # A#0/Bb0
        ['B0 ', 30.87, 23],  # B0
        ['C1 ', 32.70, 24],  # C1
        ['C#1', 34.65, 25],  # C#1/Db1
        ['D1 ', 36.71, 26],  # D1
        ['D#1', 38.89, 27],  # D#1/Eb1
        ['E1 ', 41.20, 28],  # E1
        ['F1 ', 43.65, 29],  # F1
        ['F#1', 46.25, 30],  # F#1/Gb1
        ['G1 ', 49.00, 31],  # G1
        ['G#1', 51.91, 32],  # G#1/Ab1
        ['A1 ', 55.00, 33],  # A1
        ['A#1', 58.27, 34],  # A#1/Bb1
        ['B1 ', 61.74, 35],  # B1
        ['C2 ', 65.41, 36],  # C2
        ['C#2', 69.30, 37],  # C#2/Db2
        ['D2 ', 73.42, 38],  # D2
        ['D#2', 77.78, 39],  # D#2/Eb2
        ['E2 ', 82.41, 40],  # E2
        ['F2 ', 87.31, 41],  # F2
        ['F#2', 92.50, 42],  # F#2/Gb2
        ['G2 ', 98.00, 43],  # G2
        ['G#2', 103.83, 44],  # G#2/Ab2
        ['A2 ', 110.00, 45],  # A2
        ['A#2', 116.54, 46],  # A#2/Bb2
        ['B2 ', 123.47, 47],  # B2
        ['C3 ', 130.81, 48],  # C3
        ['C#3', 138.59, 49],  # C#3/Db3
        ['D3 ', 146.83, 50],  # D3
        ['D#3', 155.56, 51],  # D#3/Eb3
        ['E3 ', 164.81, 52],  # E3
        ['F3 ', 174.61, 53],  # F3
        ['F#3', 185.00, 54],  # F#3/Gb3
        ['G3 ', 196.00, 55],  # G3
        ['G#3', 207.65, 56],  # G#3/Ab3
        ['A3 ', 220.00, 57],  # A3
        ['A#3', 233.08, 58],  # A#3/Bb3
        ['B3 ', 246.94, 59],  # B3
        ['C4 ', 261.63, 60],  # C4
        ['C#4', 277.18, 61],  # C#4/Db4
        ['D4 ', 293.66, 62],  # D4
        ['D#4', 311.13, 63],  # D#4/Eb4
        ['E4 ', 329.63, 64],  # E4
        ['F4 ', 349.23, 65],  # F4
        ['F#4', 369.99, 66],  # F#4/Gb4
        ['G4 ', 392.00, 67],  # G4
        ['G#4', 415.30, 68],  # G#4/Ab4
        ['A4 ', 440.00, 69],  # A4
        ['A#4', 466.16, 70],  # A#4/Bb4
        ['B4 ', 493.88, 71],  # B4
        ['C5 ', 523.25, 72],  # C5
        ['C#5', 554.37, 73],  # C#5/Db5
        ['D5 ', 587.33, 74],  # D5
        ['D#5', 622.25, 75],  # D#6/Eb6
        ['E5 ', 659.25, 76],  # E5
        ['F5 ', 698.46, 77],  # F5
        ['F#5', 739.99, 78],  # F#5/Gb5
        ['G5 ', 783.99, 79],  # G5
        ['G#5', 830.61, 80],  # G#5/Ab5
        ['A5 ', 880.00, 81],  # A5
        ['A#5', 932.33, 82],  # A#5/Bb5
        ['B5 ', 987.77, 83],  # B5
        ['C6 ', 1046.50, 84],  # C6
        ['C#6', 1108.73, 85],  # C#6/Db6
        ['D6 ', 1174.66, 86],  # D6
        ['D#6', 1244.51, 87],  # D#6/Eb6
        ['E6 ', 1318.51, 88],  # E6
        ['F6 ', 1396.91, 89],  # F6
        ['F#6', 1479.98, 90],  # F#6/Gb6
        ['G6 ', 1567.98, 91],  # G6
        ['G#6', 1661.22, 92],  # G#6/Ab6
        ['A6 ', 1760.00, 93],  # A6
        ['A#6', 1864.66, 94],  # A#6/Bb6
        ['B6 ', 1975.53, 95],  # B6
        ['C7 ', 2093.00, 96],  # C7
        ['C#7', 2217.46, 97],  # C#7/Db7
        ['D7 ', 2349.32, 98],  # D7
        ['D#7', 2489.02, 99],  # D#7/Eb7
        ['E7 ', 2637.02, 100],  # E7
        ['F7 ', 2793.83, 101],  # F7
        ['F#7', 2959.96, 102],  # F#7/Gb7
        ['G7 ', 3135.96, 103],  # G7
        ['G#7', 3322.44, 104],  # G#7/Ab7
        ['A7 ', 3520.00, 105],  # A7
        ['A#7', 3729.31, 106],  # A#7/Bb7
        ['B7 ', 3951.07, 107],  # B7
        ['C8 ', 4186.01, 108],  # C8
        ['C#8', 4434.92, 109],  # C#8/Db8
        ['D8 ', 4698.63, 110],  # D8
        ['D#8', 4978.03, 111],  # D#8/Eb8
        ['E8 ', 5274.04, 112],  # E8
        ['F8 ', 5587.65, 113],  # F8
        ['F#8', 5919.91, 114],  # F#8/Gb8
        ['G8 ', 6271.93, 115],  # G8
        ['G#8', 6644.88, 116],  # G#8/Ab8
        ['A8 ', 7040.00, 117],  # A8
        ['A#8', 7458.62, 118],  # A#8/Bb8
        ['B8 ', 7902.13, 119]  # B8

    )
    BeatEnable = False
    TuneEnable = False
    BeatSpeed = 120  # The tempo, 1 min has 120 beats
    BeatMidiNote2 = 62
    TIMER_ID = 1000
    TIMER_INT = 50  # timer event interval --> 50ms
    TuningTimer_INT = 10
    TickNowMS = 0
    TickLastMS = 0
    TickMS = 0
    Counter = 0
    IAStopWatch = wx.StopWatch()
    MidiOut = rtmidi.MidiOut()
    TuningNoteIndex = 57  # A4

    MICSamplePeriod = 1# sample 0.5 sec
    MICSampleRate = 44100  # sampling rate
    MICSampleNum = 0
    MICSampleCnt = 0
    NoteTickNowMS = 0
    NoteTickLastMS = 0
    NoteMS = 0  # tick for counting note
    Channels = [1]

    Device = None
    EnableMICCapture = False  # start to capture MIC sound
    MinNotePeriod = ((60 / BeatSpeed)) / 64  # 240 beats per min. and 1/64 note.  1/256 note which is 1/64 beat(1/4 note is one beat) in ms
    NoteFreq = 440  # note frequency
    # tuneFrame = None
    Q = queue.Queue()  # create an unlimited FIFO
    NoteQ = queue.Queue() # create an unlimited FIFO for Note

    device_info = sd.query_devices(Device, 'input')  # Prepare sound device for capture sound

    MICSampleRate = device_info['default_samplerate']

    MICSampleNum = length = int(MICSamplePeriod * MICSampleRate)
    #MICSampleNum = length = int(MinNotePeriod * MICSampleRate*100)

    print(f'Min note period:{MinNotePeriod}s; Sampple Rate:{MICSampleRate};Sample Num.:{MICSampleNum}')
    SoundData = np.zeros((length, len(Channels)))

    app = wx.App(False)
    frame = MainFrame(None)
    app.MainLoop()
