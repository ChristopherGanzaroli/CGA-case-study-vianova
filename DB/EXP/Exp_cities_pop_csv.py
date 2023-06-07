import csv
import sys
sys.path.append("../..")
from Class.GetData import GetAPIData

cities_pop = GetAPIData("https://public.opendatasoft.com/api/records/1.0/search/?dataset=geonames-all-cities-with-a-population-1000&q=&rows=-1&facet=feature_code&facet=cou_name_en&facet=timezone").json_data()


    
    
with open("/Users//ganza/OneDrive/Bureau/gitripo/tests/vianova/Data" + '/cities_pop.csv', 'w', newline='', encoding='utf-8') as file:
    #Ecrire dans le ficher avec les noms de colonnes
    writer = csv.writer(file,delimiter=',')
    #on crée les colonnes du fichier
    writer.writerow(['geoname_id', 'name', 'ascii_name','alternate_names','feature_class','feature_code','country_code','cou_name_en','admin1_code','admin2_code','admin3_code','admin4_code','population','elevation','dem','timezone','modification_date','label_en','Coordinates'])

    for i in range(len(cities_pop['records'])):
            try :
                geoname_id = cities_pop['records'][i]['fields']['geoname_id']
            except:
                geoname_id = 'Null'
                
            try :
                name = cities_pop['records'][i]['fields']['name']
            except:
                name = 'Null'   
                  
            try :
                ascii_name = cities_pop['records'][i]['fields']['ascii_name']
            except:
                ascii_name = 'Null' 
                
            try :
                alternate_names = cities_pop['records'][i]['fields']['alternate_names']
            except:
                alternate_names = 'Null'  
                    
            try :
                feature_class = cities_pop['records'][i]['fields']['feature_class']
            except:
                feature_class = 'Null'   
                
            try :
                feature_code = cities_pop['records'][i]['fields']['feature_code']
            except:
                feature_code = 'Null'   
                 
            try :
                country_code = cities_pop['records'][i]['fields']['country_code']
            except:
                country_code = 'Null'     
                
            try :
                cou_name_en = cities_pop['records'][i]['fields']['cou_name_en']
            except:
                cou_name_en = 'Null' 
                   
            try :
                admin1_code = cities_pop['records'][i]['fields']['admin1_code']
            except:
                admin1_code = 'Null'  

            try :
                admin2_code = cities_pop['records'][i]['fields']['admin2_code']
            except:
                admin2_code = 'Null'
                                    
            try :
                admin3_code = cities_pop['records'][i]['fields']['admin3_code']
            except:
                admin3_code = 'Null' 
                
            try :
                admin4_code = cities_pop['records'][i]['fields']['admin4_code']
            except:
                admin4_code = 'Null' 
                
            try :
                population = cities_pop['records'][i]['fields']['population']
            except:
                population = 'Null'    

            try :
                dem = cities_pop['records'][i]['fields']['dem']
            except:
                dem = 'Null'  
                
            try :
                timezone = cities_pop['records'][i]['fields']['timezone']
            except:
                timezone = 'Null'   
                 
            try :
                modification_date = cities_pop['records'][i]['fields']['modification_date']
            except:
                modification_date = 'Null'                                
             
            try :
                label_en = cities_pop['records'][i]['fields']['label_en']
            except:
                label_en = 'Null'                                
 
            try :
                Coordinates = cities_pop['records'][i]['fields']['Coordinates']
            except:
                Coordinates = 'Null'                                                                  
            writer.writerow([geoname_id,name,ascii_name,alternate_names,feature_class,feature_code,country_code,cou_name_en,admin1_code,admin2_code,admin3_code,admin4_code,population,dem,timezone,modification_date,label_en,Coordinates])
