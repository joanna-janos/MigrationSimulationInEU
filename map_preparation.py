import pandas as pd

from map.choropleth_map import save_map_in_each_step
from map.data_preparation import prepare_png_from_html
from map.gif_map import prepare_gif

if __name__ == "__main__":
    agents_per_step = pd.read_csv('results/agents_per_step.csv', sep=';')
    coordinates_path = 'data/coordinates.json'
    html_files_dir = save_map_in_each_step(agents_per_step, coordinates_path)
    png_files_dir = prepare_png_from_html(html_files_dir)
    prepare_gif(png_files_dir)
