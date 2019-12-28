from pathlib import Path

import selenium.webdriver

from map.directory import create_not_existing_directory


def prepare_png_from_html(html_files_dir: str):
    """ Save each html file as png in directory created next to directory with html files.

    Arguments
    ----------
    html_files_dir : str
        Path to html files

    Returns
    -------
    str
        Path to png files
    """
    try:
        png_files_dir = html_files_dir + '../img/'
        create_not_existing_directory(png_files_dir)
        driver = selenium.webdriver.Chrome(executable_path=r'chromedriver/chromedriver')
        steps = 20
        current_working_directory = Path.cwd()
        for step in range(steps):
            driver.get(f'file:{current_working_directory}/{html_files_dir}step_{step}.html')
            driver.save_screenshot(f'{png_files_dir}step_{step}.png')
        driver.close()
        return png_files_dir
    except selenium.common.exceptions.InvalidArgumentException as _:
        driver.close()
