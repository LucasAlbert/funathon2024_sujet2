import pandas as pd
import geopandas as gpd
import plotly.express as px
from plotnine import ggplot, geom_line, aes
import matplotlib.pyplot as plt
from src.figures import plot_airport_line
from src.divers_functions import create_dataframe_input, summary_stat_airport
from great_tables import GT

import src.import_data as sid
from src.create_data_list import create_data_list

YEARS_LIST = [str(year) for year in range(2018, 2023)]
MONTHS_LIST = list(range(1, 13))
year = 2019
month = 1

# Load data ----------------------------------
urls = create_data_list('./funathon2024_sujet2/sources.yml')


pax_apt_all = sid.import_airport_data(urls['airports'].values())
pax_cie_all = sid.import_airport_data(urls['compagnies'].values())
pax_lsn_all = sid.import_airport_data(urls['liaisons'].values())


airports_location = gpd.read_file(
    urls['geojson']['airport']
)


liste_aeroports = pax_apt_all['apt'].unique()
default_airport = liste_aeroports[0]

pax_apt_all['traffic'] = pax_apt_all['apt_pax_dep'] + pax_apt_all['apt_pax_tr'] + pax_apt_all['apt_pax_arr']

pax_apt_all['date'] = pd.to_datetime(pax_apt_all['an'] + pax_apt_all['mois'] + '01', format='%Y%m%d')

stats_aeroports = summary_stat_airport(pax_apt_all)
stats_aeroports['name_clean'] = stats_aeroports['apt_nom'].str.title() + " _(" + stats_aeroports['apt'] + ")_"
stats_aeroports = stats_aeroports[ ['name_clean'] + [col for col in stats_aeroports.columns if col != 'name_clean']]

#trafic_date = create_dataframe_input(pax_apt_all, year, month)
#print(trafic_date)
