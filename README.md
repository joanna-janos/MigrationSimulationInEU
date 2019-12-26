<h1 align="center"><b><i>Migration simulation in EU</i></b></h1>
<p align=center>
    <a><img alt="mesa" src="https://img.shields.io/badge/agent based modeling framework-mesa-blue.svg"></a>
    <a><img alt="librosa" src="https://img.shields.io/badge/visualisation-librosa-blue.svg"></a><br>
    <a><img alt="Python" src="https://img.shields.io/badge/python-3.8-blue.svg"></a>
    <a><img alt="pandas" src="https://img.shields.io/badge/pandas-0.25.3-blue.svg"></a>
    <a><img alt="seaborn" src="https://img.shields.io/badge/seaborn-0.9.0-blue.svg"></a>
    <a><img alt="matplotlib" src="https://img.shields.io/badge/matplotlib-3.1.1-blue.svg"></a>
</p>

<p align=center><img src="results/map/animation.gif" width="600" height="400" /></p>

<h2> :bulb: Purpose </h2>
Migration simulation of people in EU based on data gathered especially from EU reports.

<h2> :file_folder: Content </h2>

- [<b>data_analysis.ipynb</b>](https://github.com/joanna-janos/Migration-simulation-in-EU/blob/master/data_analysis.ipynb) - data analysis and selection of the most important features <br>
- [<b>migration_simulation.ipynb</b>](https://github.com/joanna-janos/Migration-simulation-in-EU/blob/master/migration_simulation.ipynb) - core part of project where agents are created and simulation is run <br>
- [<b>map.py</b>](https://github.com/joanna-janos/Migration-simulation-in-EU/blob/master/map.py) - preparation of animated map <br>
- [<b>results_analysis.ipynb</b>](https://github.com/joanna-janos/Migration-simulation-in-EU/blob/master/results_analysis.ipynb) - analysis of results (e.g. how religious denomination affects on changing a country)


<h2> :round_pushpin: Agents attributes </h2>

- origin and current country
- religious denomination
- race
- level of being likely to travel
- happiness level

Agent can migrate only to neighbouring country within one step.

<h2> :round_pushpin: Attributes assigned to all people in countries </h2>

- level of being comfortable with a White/Black/Asian people in their country
- level of being comfortable with a Jew/Christian/Muslim in their country
- level of being comfortable with people from different country in social relations
- level of being comfortable with integration with people from other countries
- level of being likely to move to another country within the next 10 years

<h2> :sparkles: Results </h2>

Results were prepared as:
1. [animation](https://github.com/joanna-janos/Migration-simulation-in-EU/blob/master/results/map/animation.gif) - same as at beginning of README
2. [bar graph](https://github.com/joanna-janos/Migration-simulation-in-EU/blob/master/results/agents_in_countries_in_each_step.mp4) - as an MP4 file (results for last step can be observed in [<i>migration_simulation.ipynb</i>](https://github.com/joanna-janos/Migration-simulation-in-EU/blob/master/migration_simulation.ipynb))
