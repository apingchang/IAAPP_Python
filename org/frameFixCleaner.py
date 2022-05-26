# frameFixCleaner.py
#
# By Daryl Williams
# www.fandangleproductions.com
#
# modify this code form above.
# When create multiple frames the main frame should put in the last.
#

import os

def cleanFrame(fmcode):    
    cleancode = fmcode.replace('\t','    ')
    cleancode = cleancode.replace('m_','')
    cleancode = cleancode.replace('    # Virtual event handlers, overide them in your derived class','')
    return cleancode   
    
def fixFrame(prjDir,filename):
    fmcode=""
    srcFile = os.path.join(prjDir+'\org',filename+'.py')
    f=open(srcFile,'r')
    for line in f:
        if line.startswith(('# -*- coding: utf-8 -*-')):
            fmcode = fmcode + "# %s.py" % filename
        elif line.startswith(('import wx.xrc')):
            pass
        elif line.startswith(('##')):
            pass
        elif line.startswith(('class')):
            lineSp = line.split(' ')
            frameName = lineSp[1]
            fmcode = fmcode + line
        #elif line.startswith(('	def __init__( self, parent ):')):
            #fmcode = fmcode + '	def __init__( self ):\n'
        #elif line.startswith(('		wx.Frame.__init__')):
            #line = line.replace('parent','None')
            #fmcode = fmcode + line
        elif line.startswith(('	def __del__( self ):')):
            pass
        elif line.startswith(('		pass')):
            fmcode = fmcode + '        # ------------ Add widget program settings\n\n'
            fmcode = fmcode + '        # ------------ Call Populates\n\n'
            fmcode = fmcode + '        self.Show()\n\n'
            fmcode = fmcode + '        # ------------ Event handlers'
        else:
            fmcode = fmcode + line

    # ----- add main loop
    fmcode = fmcode + 'if __name__ == "__main__":\n'
    fmcode = fmcode + '    app = wx.App(False)\n'
    fmcode = fmcode + '    frame = %s(None)\n' % frameName
    #fmcode = fmcode + '    frame.Show()\n'
    fmcode = fmcode + '    app.MainLoop()\n'

    #print fmcode
    f.close()
    cleancode = cleanFrame(fmcode)   
    outFile = os.path.join(prjDir+'\src',filename+'BK.py')
    f=open(outFile,'w')
    f.write(cleancode)
    f.close()


prjDir = r"C:\MyProjects\IAPython"
filename = "IAAPP"

print('Cleaning orginal file: %s' % (filename+'BK.py'))

outStat = fixFrame(prjDir,filename)

print('Clean orininal file and save in src folder as:',(filename+'BK.py'))