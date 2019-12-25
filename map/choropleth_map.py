import pandas as pd
import folium
import pathlib
from map.directory import create_not_existing_directory

def get_mapping_country_name_to_id():
    country_name_to_id = {}

    with open("data/country_to_id.txt") as f:
        for line in f:
            (country_name, country_id) = line.strip().split(',')
            country_name_to_id[country_name] = country_id
    return country_name_to_id


def replace_country_name_with_id(agents_per_step):
    mapping_country_id = get_mapping_country_name_to_id()
    agents_per_step.replace({"Country": mapping_country_id}, inplace=True)


def save_map_in_each_step(agents_per_step, coordinates):
    replace_country_name_with_id(agents_per_step)
    steps = len(agents_per_step.loc[0]) - 1
    html_files_dir = 'results/map/html/'

    for step in range(steps):
        EU_map = folium.Map(location=[52, 12], zoom_start=4)

        folium.Choropleth(
            geo_data=coordinates,
            name='choropleth',
            data=agents_per_step,
            columns=['Country', str(step)],
            key_on='feature.id',
            fill_color='OrRd',
            fill_opacity=0.8,
            line_opacity=0.5,
            legend_name='Population',
        ).add_to(EU_map)

        folium.LayerControl().add_to(EU_map)
        create_not_existing_directory(html_files_dir)
        EU_map.save(f'{html_files_dir}step_{step}.html')
    return html_files_dir
