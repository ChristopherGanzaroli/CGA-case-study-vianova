import sys
sys.path.append("..")
from Class.GetData import GetAPIData

cities_pop = GetAPIData("https://public.opendatasoft.com/api/records/1.0/search/?dataset=geonames-all-cities-with-a-population-1000&q=&rows=-1&facet=feature_code&facet=cou_name_en&facet=timezone").json_data()

print(cities_pop)
