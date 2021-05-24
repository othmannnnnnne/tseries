import pandas as pd
from wwo_hist import retrieve_hist_data
import os

hist_weather_data = pd.DataFrame()


frequency=24
start_date = '01-JAN-2017'
end_date = '20-MAY-2021'
api_key = '5a5a055b8f36462bb2c132317212503'
location_list = ['Casablanca']

hist_weather_data = retrieve_hist_data(api_key,
                                        location_list,
                                        start_date,
                                        end_date,
                                        frequency,
                                        location_label = False,
                                        export_csv = False,
                                        store_df = True)


