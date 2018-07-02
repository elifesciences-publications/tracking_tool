#before running this script make sure you have moviepy installed

#Enter the ID of the ant here:
#(the quotation marks are important)
Ant_ID='Ant_ID'
#Enter the video nome here:
#(quotation marks are still important)
video='sample'
#now press F5

import moviepy

import os
##################################
from moviepy.editor import *
folder=video+'_frames'
if not os.path.exists(folder):
    os.makedirs(folder) 
    vid_name=video+'.mp4'
    clip = VideoFileClip(vid_name)
    print(clip.duration)
    time=0
    while time<clip.duration:
        str_time=str(time)
        while len(str_time)<5:
            str_time='0'+str_time
        file_name=folder+'/'+video+'_'+str_time+'.jpeg'
        print(file_name)
        clip.save_frame(file_name, t=time)
        
        time=time+1 
####################################

import tkinter
from PIL import Image, ImageTk
global count
global location_list
location_list=[]

def goforward(event):
    global count
    global location_list
    print("Added:", count, event.x, event.y)
    location_list.append([count,event.x,event.y])
    event.widget.quit()
    count=count
    
def goback(event):
    global count
    global location_list
    print("Removed: click number",count-1)
    location_list.pop()
    event.widget.quit()
    count=count-2
    
root = tkinter.Toplevel()
root.bind("<Button-1>", goforward)
root.bind('<MouseWheel>', goforward)#Button-4 in linux
root.bind("<Button-3>", goback)
root.bind("<Button-5>", goback)
#root.bind("<Return>", save)
root.geometry('+%d+%d' % (300,300))
root.configure(background='black')
dirlist = os.listdir(folder)
dirlist=sorted(dirlist)
old_label_image = None

count=0
while count<len(dirlist):
#    print(count)
    f=folder+'/'+dirlist[count]
    #f=dirlist[count]
    count=count+1
#    try:
    image1 = Image.open(f)
    root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
    tkpi = ImageTk.PhotoImage(image1)
    label_image = tkinter.Label(root, image=tkpi)
    label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])
    root.title(f)
    if old_label_image is not None:
        #print('destroy')
        old_label_image.destroy()
    old_label_image = label_image
    root.mainloop() # wait until user clicks the window
#    except:
#        print('exception')
#        pass
root.destroy()
ant_folder=Ant_ID+'_location_lists'
if not os.path.exists(ant_folder):
    os.makedirs(ant_folder) 
    
    
f=open(ant_folder+'/'+video+'_'+Ant_ID+'.txt','w')
for row in location_list:
    f.write(str(row[0])+','+str(row[1])+','+str(row[2])+'\n')
f.close() 


