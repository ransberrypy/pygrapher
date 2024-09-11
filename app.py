from gifgraphy import create_gif
from moviegraphy import create_video

image_paths = ['inputs/img1.jpg', 'inputs/img2.jpg', 'inputs/img3.jpg','inputs/img4.jpg'
            ,'inputs/img5.jpg','inputs/img6.jpg','inputs/img7.jpg'
            ]  

output_path_vid = 'output/output_video.mp4'
output_path = 'output/output.gif'

create_gif(image_paths, output_path, duration=500) 
create_video(image_paths, output_path_vid, fps=1)

