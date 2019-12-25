from choropleth_map import save_map_in_each_step
from gif_map import prepare_png_from_html
from gif_preparation import prepare_gif
import pandas as pd

if __name__ == "__main__":
    agents_per_step = pd.read_csv('../results/agents_per_step.csv', sep=';')
    coordinates = f'../data/coordinates.json'
    html_files_dir = save_map_in_each_step(agents_per_step, coordinates)
    png_files_dir = prepare_png_from_html(html_files_dir)
    prepare_gif(png_files_dir)
