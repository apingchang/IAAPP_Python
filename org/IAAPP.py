# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.0-4761b0c)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class TuningFrame
###########################################################################

class TuningFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tuning ......", pos = wx.DefaultPosition, size = wx.Size( 394,225 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerTuningDialog = wx.BoxSizer( wx.VERTICAL )

		bSizerTuneNote = wx.BoxSizer( wx.HORIZONTAL )

		self.staticTextTuneNote = wx.StaticText( self, wx.ID_ANY, u"Tuning Note:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.staticTextTuneNote.Wrap( -1 )

		bSizerTuneNote.Add( self.staticTextTuneNote, 0, wx.ALIGN_CENTER|wx.ALL, 10 )

		listBoxTuneNoteChoices = [ u"A4-440Hz", u"D1-550Hz", wx.EmptyString ]
		self.listBoxTuneNote = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,55 ), listBoxTuneNoteChoices, wx.LB_SINGLE )
		bSizerTuneNote.Add( self.listBoxTuneNote, 0, wx.ALL, 8 )

		self.buttonPlayTuneNote = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )

		self.buttonPlayTuneNote.SetBitmap( wx.Bitmap( u"../src/triAngle.bmp", wx.BITMAP_TYPE_ANY ) )
		self.buttonPlayTuneNote.SetBitmapDisabled( wx.NullBitmap )
		self.buttonPlayTuneNote.SetBitmapPressed( wx.NullBitmap )
		self.buttonPlayTuneNote.SetBitmapCurrent( wx.NullBitmap )
		bSizerTuneNote.Add( self.buttonPlayTuneNote, 0, wx.ALL, 5 )


		bSizerTuningDialog.Add( bSizerTuneNote, 1, wx.EXPAND, 5 )


		bSizerTuningDialog.Add( ( 0, 0), 1, wx.EXPAND, 0 )

		bSizerTuneSound = wx.BoxSizer( wx.HORIZONTAL )

		self.staticTextTuneSound = wx.StaticText( self, wx.ID_ANY, u"Tuning Sound:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextTuneSound.Wrap( -1 )

		bSizerTuneSound.Add( self.staticTextTuneSound, 0, wx.ALL, 10 )

		self.textCtrlTuneSoundFreq = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		bSizerTuneSound.Add( self.textCtrlTuneSoundFreq, 0, wx.ALL, 5 )

		self.staticTextTuningHz = wx.StaticText( self, wx.ID_ANY, u"Hz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextTuningHz.Wrap( -1 )

		bSizerTuneSound.Add( self.staticTextTuningHz, 0, wx.ALL, 7 )

		self.sliderTuneSoundPre = wx.Slider( self, wx.ID_ANY, 0, -100, 100, wx.DefaultPosition, wx.Size( 200,-1 ), wx.SL_HORIZONTAL )
		bSizerTuneSound.Add( self.sliderTuneSoundPre, 0, wx.ALL, 5 )


		bSizerTuningDialog.Add( bSizerTuneSound, 1, wx.EXPAND, 0 )

		bSizerNote = wx.BoxSizer( wx.HORIZONTAL )

		self.staticTextTSBlank = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,-1 ), 0 )
		self.staticTextTSBlank.Wrap( -1 )

		bSizerNote.Add( self.staticTextTSBlank, 0, wx.ALL, 5 )

		self.textCtrlTuningSoundNote = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.textCtrlTuningSoundNote.SetMaxLength( 8 )
		bSizerNote.Add( self.textCtrlTuningSoundNote, 0, wx.ALL, 3 )


		bSizerTuningDialog.Add( bSizerNote, 1, wx.EXPAND, 0 )


		self.SetSizer( bSizerTuningDialog )
		self.Layout()
		self.tuningTimer = wx.Timer()
		self.tuningTimer.SetOwner( self, wx.ID_ANY )
		self.tuningTimer.Start( 5 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.TuningFrameOnClose )
		self.listBoxTuneNote.Bind( wx.EVT_LISTBOX, self.listBoxTuneNoteOnListBox )
		self.buttonPlayTuneNote.Bind( wx.EVT_BUTTON, self.buttonPlayTuneNoteOnButtonClick )
		self.Bind( wx.EVT_TIMER, self.tuningTimerOnTimer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def TuningFrameOnClose( self, event ):
		event.Skip()

	def listBoxTuneNoteOnListBox( self, event ):
		event.Skip()

	def buttonPlayTuneNoteOnButtonClick( self, event ):
		event.Skip()

	def tuningTimerOnTimer( self, event ):
		event.Skip()


###########################################################################
## Class BeatFrame
###########################################################################

class BeatFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Beat ......", pos = wx.DefaultPosition, size = wx.Size( 268,185 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerBeatDialog = wx.BoxSizer( wx.VERTICAL )

		self.staticTextSetBeat = wx.StaticText( self, wx.ID_ANY, u"Beat Setting....", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextSetBeat.Wrap( -1 )

		bSizerBeatDialog.Add( self.staticTextSetBeat, 0, wx.ALL, 5 )

		bSizerBeatSetting = wx.BoxSizer( wx.HORIZONTAL )

		self.staticTextBeatSpeed = wx.StaticText( self, wx.ID_ANY, u"Beat Speed :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextBeatSpeed.Wrap( -1 )

		bSizerBeatSetting.Add( self.staticTextBeatSpeed, 0, wx.ALL, 5 )

		self.spinCtrlBeatSpeed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.TE_PROCESS_ENTER, 30, 500, 60 )
		bSizerBeatSetting.Add( self.spinCtrlBeatSpeed, 0, wx.ALL, 3 )


		bSizerBeatDialog.Add( bSizerBeatSetting, 0, wx.EXPAND, 5 )

		bSizerBeatSound = wx.BoxSizer( wx.HORIZONTAL )

		self.staticTextBeatSpeed1 = wx.StaticText( self, wx.ID_ANY, u"Beat Sound :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticTextBeatSpeed1.Wrap( -1 )

		bSizerBeatSound.Add( self.staticTextBeatSpeed1, 0, wx.ALL, 5 )

		self.spinCtrlBeatSound = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 27, 87, 62 )
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

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def BeatFrameOnClose( self, event ):
		event.Skip()

	def spinCtrlBeatSpeedOnSpinCtrl( self, event ):
		event.Skip()

	def spinCtrlBeatSpeedOnTextEnter( self, event ):
		event.Skip()

	def spinCtrlBeatSoundOnSpinCtrl( self, event ):
		event.Skip()

	def checkBoxEnableBeatOnCheckBox( self, event ):
		event.Skip()

	def buttonBeatOKOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Instrumentalist Assistance", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.menubarMain = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.menuItemFileOpen = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Open"+ u"\t" + u"Ctrl-O", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileOpen )

		self.menuItemFileSave = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Save"+ u"\t" + u"Ctrl-S", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileSave )

		self.m_menuItemFileSaveAs = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Save As..."+ u"\t" + u"Ctrl-A", u"Save current file as a new one", wx.ITEM_NORMAL )
		self.menuFile.Append( self.m_menuItemFileSaveAs )

		self.menuFile.AppendSeparator()

		self.menuItemFileExit = wx.MenuItem( self.menuFile, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileExit )

		self.menubarMain.Append( self.menuFile, u"File" )

		self.menuTools = wx.Menu()
		self.menuItemToolsBeat = wx.MenuItem( self.menuTools, wx.ID_ANY, u"Beat"+ u"\t" + u"Alt-B", u"Set beat parameter", wx.ITEM_NORMAL )
		self.menuTools.Append( self.menuItemToolsBeat )

		self.menuItemToolsTuning = wx.MenuItem( self.menuTools, wx.ID_ANY, u"Tuning"+ u"\t" + u"Alt-T", u"Tuning your instrument", wx.ITEM_NORMAL )
		self.menuTools.Append( self.menuItemToolsTuning )

		self.menubarMain.Append( self.menuTools, u"Tools" )

		self.menuHelp = wx.Menu()
		self.menuItemHelpAbout = wx.MenuItem( self.menuHelp, wx.ID_ANY, u"About"+ u"\t" + u"Alt-A", u"About the application", wx.ITEM_NORMAL )
		self.menuHelp.Append( self.menuItemHelpAbout )

		self.menubarMain.Append( self.menuHelp, u"Help" )

		self.SetMenuBar( self.menubarMain )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
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
		self.appTimer.Start( 1000 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuItemOpenOnMenuSelection, id = self.menuItemFileOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemSaveOnMenuSelection, id = self.menuItemFileSave.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemSaveAsOnMenuSelection, id = self.m_menuItemFileSaveAs.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemExitOnMenuSelection, id = self.menuItemFileExit.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemBeatOnMenuSelection, id = self.menuItemToolsBeat.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemTuningOnMenuSelection, id = self.menuItemToolsTuning.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemAboutOnMenuSelection, id = self.menuItemHelpAbout.GetId() )
		self.Bind( wx.EVT_TIMER, self.appTimerOnTimer, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def m_menuItemOpenOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItemSaveOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItemSaveAsOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItemExitOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItemBeatOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItemTuningOnMenuSelection( self, event ):
		event.Skip()

	def m_menuItemAboutOnMenuSelection( self, event ):
		event.Skip()

	def appTimerOnTimer( self, event ):
		event.Skip()


