from PIL import Image

def create_gif(image_paths, output_path, duration=500):
    images = [Image.open(img_path) for img_path in image_paths]
    images[0].save(output_path, save_all=True, append_images=images[1:], duration=duration, loop=0)
