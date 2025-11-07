#create a program using moviepy that takes at least 3 images and 1 audio file as a input generate a slideshow video 
#where each image shown for 3 sec with background music. export the final video as slideshow.mp4 at 24 fps
from moviepy.editor import*

# audio1 = AudioFileClip("extract.mp3") 

# clip1= ImageClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\video image audio editing\butterfly.jpg") 
# clip1= clip1.set_duration(5)

# clip2= ImageClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\video image audio editing\diksha.jpg") 
# clip2= clip2.set_duration(5)

# clip3= ImageClip(r"C:\Users\Diksha Kolhe\OneDrive\Desktop\Python Advance\text.jpg") 
# clip3= clip3.set_duration(5)

# v=concatenate_videoclips([clip1,clip2,clip3],method="compose")

# audio2=v.set_audio(audio1)
# audio2.write_videofile("D.mp4",fps=24)

#create a python program using movie py that takes 2 video clips as input. display the before videoclip and after videoclip 
#in layout apply black and white effect to 2nd clip and add text label as before and after on respective video clip
#a video clip start with fadein and end with fadout effect 
# export final video as before after.mp4 at 24 fps



c1=VideoFileClip("video image audio editing/vdo3.mp4").subclip(0,10)
c2=VideoFileClip("video image audio editing/vdo4.mp4").subclip(0,10)
black_white=c2.fx(vfx.blackwhite)

from moviepy.config import change_settings
change_settings({
    "IMAGEMAGICK_BINARY":"C:\\Program Files\\ImageMagick-7.1.2-Q16-HDRI\\magick.exe"
})

txt1=TextClip("Before",fontsize=50,color="White")
txt=txt1.set_position((200,300)).set_duration(5)
v1=CompositeVideoClip([c1,txt])


txt2=TextClip("After",fontsize=50,color="White")
txt=txt2.set_position((200,300)).set_duration(5)
v2=CompositeVideoClip([black_white,txt])

layout=clips_array([[v1,v2]])
slow=layout.fx(vfx.fadeout,4).fx(vfx.fadein,4)
slow.write_videofile("DK.mp4",fps=24)

# create a python program using moviepy that takes videoclip a program should create a yt short style video
# apply fadein and fadeout effect to the videoclip and export the final video as short_video.mp4 at fps 30 with a
# resolution 1080*1920

before=VideoFileClip("DK.mp4")
from PIL import Image
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS
resized=before.resize((1080,1920))
resized.write_videofile("short_video.mp4",fps=30)



