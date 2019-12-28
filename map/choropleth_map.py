import folium
import pandas as pd

from map.directory import create_not_existing_directory


def get_mapping_country_name_to_id():
    """ Get mapping of country name to id based on data/country_to_id.txt.

    Returns
    -------
    dict
        dictionary where key is country name and corresponding value is country id
    """
    country_name_to_id = {}

    with open("data/country_to_id.txt") as f:
        for line in f:
            (country_name, country_id) = line.strip().split(',')
            country_name_to_id[country_name] = country_id
    return country_name_to_id


def replace_country_name_with_id(agents_per_step: pd.DataFrame):
    """ Replace country name with id in 'Country' column in given data frame.

    Arguments
    ----------
    agents_per_step : pd.DataFrame
        Data frame containing "Country" column with values like in data/country_to_id.txt before separator

    Returns
    -------
    pd.DataFrame
        Data frame containing ids instead of country names is "Country" column
    """
    mapping_country_id = get_mapping_country_name_to_id()
    agents_per_step.replace({"Country": mapping_country_id}, inplace=True)


def save_map_in_each_step(agents_per_step: pd.DataFrame, coordinates_path: str):
    """ Save html representations of choropleth map for each step using librosa.

    Arguments
    ----------
    agents_per_step : pd.DataFrame
        Data frame containing number of agents in each country in each step.
    coordinates_path : str
        Path to file containing coordinates for each country in data frame

    Returns
    -------
    str
       Path to html files
    """
    replace_country_name_with_id(agents_per_step)
    steps = len(agents_per_step.loc[0]) - 1
    html_files_dir = 'results/map/html/'
    create_not_existing_directory(html_files_dir)

    for step in range(steps):
        EU_map = folium.Map(location=[52, 12], zoom_start=4)

        folium.Choropleth(
            geo_data=coordinates_path,
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
        EU_map.save(f'{html_files_dir}step_{step}.html')
    return html_files_dir
