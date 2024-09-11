from moviepy.editor import ImageSequenceClip

def create_video(image_paths, output_path, fps=1):
    clip = ImageSequenceClip(image_paths, fps=fps)
    clip = clip.set_duration(10)  # Set total duration to 10 seconds
    clip.write_videofile(output_path, fps=fps,codec='mpeg4')
