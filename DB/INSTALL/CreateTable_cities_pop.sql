CREATE TABLE IF NOT EXISTS cities_pop(
    geoname_id              TEXT,
    name                    TEXT,
    ascii_name              TEXT,
    alternate_names         TEXT,
    feature_class           TEXT,
    feature_code            TEXT,
    country_code            TEXT,
    cou_name_en             TEXT,
    --country_code_2          TEXT, 3 values
    admin1_code             TEXT,
    admin2_code             TEXT,
    admin3_code             TEXT,
    admin4_code             TEXT,
    population              INTEGER,
    elevation               TEXT,
    dem                     INTEGER,
    timezone                TEXT,
    modification_date       TEXT, -- FORMAT YYYY-MM-DD
    label_en                TEXT,
    Coordinates             
) 

