from dependencies.yt_call import YT_Call
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tkinter as tk
from PIL import ImageTk, Image

# Initialize parameters
pages_to_iterate = 40
comment_order = 'time'


# Initialise & Style GUI
root = tk.Tk()

#root.wm_iconbitmap(True,'dependencies/images/siegbrau.ico')
root.wm_title('Siegbrau YT')

canvas1 = tk.Canvas(root, bg='black', width = 400, height = 400)
canvas1.pack()

entry1 = tk.Entry(root, fg = 'black', font = ("Garamond"), bg = '#d8bfa2')
canvas1.create_window(200,150, window = entry1, width = 300)

tag1 = tk.Label(root, text = "Please enter the URL to any YouTube video:",
fg = '#d8bfa2', bg = 'black', font = ("Garamond"))
canvas1.create_window(200,120,window = tag1)

title_1 = tk.Label(root, text = 'Siegbrau YT', fg = '#d8bfa2', bg = 'black')
title_1.configure(font = ("Garamond", 20, "bold"))
canvas1.create_window(200,80, window = title_1)

sieg_op = Image.open('dependencies/images/siegbrau.png')
sieg_op = sieg_op.resize((40,44))
sieg_1 = ImageTk.PhotoImage(sieg_op)
#sieg_tk = tk.Label(root, image=sieg_1, height = 40, width = 40)
canvas1.create_image(200,50, image = sieg_1)


def get_ratings():

    video_id_tk = entry1.get()

    if 'v=' in video_id_tk:
        v_id = video_id_tk.split('v=')[1]
    elif 'youtu.be' in video_id_tk:
        v_id = video_id_tk.split('.be/')[1]
    else:
        label = tk.Label(root, text = 'Please enter a valid url.', font = ("Garamond"), fg = '#d8bfa2', bg = 'black')
        canvas1.create_window(200,220, window = label)
        return None
        
    dataset = YT_Call.call(video_id = v_id, priority = comment_order, n_pages = pages_to_iterate)
    comments = []
    comment_ids = []
    like_count = []

    for i in range(len(dataset)):
        for c in dataset[i]['items']:
            comments += [c['snippet']['topLevelComment']['snippet']['textDisplay']]
            comment_ids += [c['snippet']['topLevelComment']['id']]
            like_count += [c['snippet']['topLevelComment']['snippet']['likeCount']]


    pos_score = []
    neg_score = []
    neu_score = []

    for i in range(len(comments)):
        SIA = SentimentIntensityAnalyzer()
        pos_score += [SIA.polarity_scores(comments[i])["pos"]]
        neg_score += [SIA.polarity_scores(comments[i])["neg"]]
        neu_score += [SIA.polarity_scores(comments[i])["neu"]]

    pc_pos = round(np.mean(pos_score)*100,3)
    pc_neg = round(np.mean(neg_score)*100,3)
    pc_neu = round(np.mean(neu_score)*100,3)
    label = tk.Label(root, font = ('Garamond'), fg = '#d8bfa2', bg = 'black',
    text = f" The comment section displayed the following attributes: \n Positivity: {str(pc_pos) + '%' }; \n Negativity: {str(pc_neg)+'%'}; \n Neutral: {str(pc_neu) + '%'}." )
    canvas1.create_window(200,260, window = label)

button1= tk.Button(text = 'Extract Ratings', command = get_ratings, font = ("Garamond"),
bg = '#d8bfa2')
canvas1.create_window(200,190,window = button1)
root.mainloop()
