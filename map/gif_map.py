import selenium.webdriver
from pathlib import Path
from directory import create_not_existing_directory

def prepare_png_from_html(html_files_dir):
    try:
        png_files_dir = html_files_dir + '../img/'
        create_not_existing_directory(png_files_dir)
        driver = selenium.webdriver.Chrome(executable_path=r'../chromedriver/chromedriver')
        steps = 20
        current_working_directory = Path.cwd()
        for step in range(steps):
            driver.get(f'file:{current_working_directory}/{html_files_dir}step_{step}.html')
            # You may need to add time.sleep(seconds) here
            driver.save_screenshot(f'{png_files_dir}step_{step}.png')
        driver.close()
        return png_files_dir
    except selenium.common.exceptions.InvalidArgumentException as e:
        driver.close()
