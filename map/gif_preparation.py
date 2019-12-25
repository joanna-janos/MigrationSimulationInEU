import imageio
import glob

def prepare_gif(png_files_dir):
    paths_to_imgs = sorted(glob.glob(f"{png_files_dir}*.png"), key=lambda x: int(''.join(filter(str.isdigit, x))))
    with imageio.get_writer('../results/map/animation.gif', mode='I', fps=1) as writer:
        for file_path in paths_to_imgs:
            image = imageio.imread(file_path)
            writer.append_data(image)