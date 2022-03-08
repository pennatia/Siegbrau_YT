# siegbrau_yt
Youtube comment analysis to replace the dislike button.

The current project was initiated as a reactionary measure to YouTube's removal of the dislike button. In its grandest ambitions, the project aims to perform sentiment analysis on a YouTube video's comment section, combining it with its other metadata to provide an estimate of the video's dislike count. 

In its current form, the application is capable of taking in any YouTube Link, and return a positivity, negativity and neutrality score for the comment section. 

# Requirements
Requirements can be found in the requirements.txt file, and installed as follows:
```
pip install -r requirements.txt

```
Currently, the App requires a Google API Developer Key, which can be inserted in the "YT_Call.py" file in the program's dependencies folder. 
Once an API key is inserted, the program will function for any YouTube URL (with extra parameters pruned). 

The app offers a very simplistic tkinter UI:

![alt text](https://github.com/pennatia/Siegbrau_YT/blob/master/dependencies/images/screengrab.png)

More updates to come!

