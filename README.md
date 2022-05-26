# IAAPP_Python

##Functions

	###Motivation,
	Since when play my violin always need to tune it first and during the practice need to have accurate speed of the music. 
	To buy a beating and tuning tool cost me extra dollar so to develop an APP which can start with these function on PC or mobile phone is an good idea.
	
	###Beat
	Use MIDI as beat sound then it got more real time. Use 0x99,0x3C,0x7F as the MIDI message for the beat sound.
	Windows Beep() function not as expect could be used. Since when google somebody said it is not synchronized should use WAV as sound to play.
	Try to play .wav as beep.  Set an data array to from the WAV, it sounds synchronized but each sound play need at least around 480ms.
	Test Beep() it seems ok. So using Beep as the beat sound function.
	
	Try timer event to have precision time period of sound. Time event still can not provide the precision time period the event will depend on the events occurs in the Windows may be will delay.  It seems it will take 5~15ms longer than what I set for timer event!
	
	
	wxSound even play a very short sound (0.1s) will take about 480ms so the beat speed can only implement as 120 at this moment. Need to find a real time sound play library to implement the beat function. 
	Use Audacity APP to generate a 0.1 sec. sound in .wav file, build the sound in memory for paling as the beat sound.
	The .WAV format as below:
	
	Functions of Beat:
	Enable beat 
	Set beat speed (tempo) : 10 ~ 500.
	First beat sound (Emphasize the first beat of each measure)
	
	Use dialog to implement the setting of above parameter. When process more event the beep become uncontrolled.
	
	
	
	
	###Instrument tuning
		○ The frequency of each note could be found in this link. To tune the instrument we need to get the sound from microphone and then analyze it and transfer to be the frequency value.
		○ To transfer to frequency after I search the internet I found it will need FTT function to do it. I found some web page which has the demonstration about this. Check this page for simulation the data and get the output & this page for get audio data from microphone and do the FFT.
		
	###Read music score
		○ Open file
			§ PDF
			§ Music file
			§ MIDI
		○ Play and display the sheet
		○ Listen and display the sheet
	###Compose music score
		○ Edit (manual generate)
		○ Listen and generate
		○ Save file
![image](https://user-images.githubusercontent.com/7997322/170422642-ca912a7d-83a8-49e8-8ea9-964c912fa999.png)
