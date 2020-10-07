Scrape data and store in SQLite. Use Datasette to present data and deploy.

## Install 
Set up a virtualenv and:


`pip install -r requirements.txt`

## Scrape data

Uncomment the registers needed in `scraper.py`. Run `python scrape.py` to get
 the data in the `data` folder.
 

## Clean data

1. Make a function in `cleaned_data.csv` for each file that needs cleaning
2. Run `clean_data.py` and pipe the output to `cleaned_data.csv` 

## Geocode

1. Get a copy of ONSPD
2. Make it smaller by doing:
    `cat [path/to/onspd]/Data
/ONSPD_FEB_2020_UK.csv |  csvcut -c 3,43,44 > onspd_small.csv`
3. Join with scraped files to geocode them: 
    ```
   csvjoin --left -c 5,1 cleaned_dat.csv onspd_small.csv
     > cleaned_with_points.csv
   ```
## Datasette

4. Make in to a SQLite database: `csvs-to-sqlite cleaned_with_points.csv eps.sqlite`
5. Run Datasette on the database: `datasette --load-extension=/usr/lib/x86_64-linux-gnu/mod_spatialite.so eps.sqlite --metadata metadata.json`
6. Publish: `datasette publish cloudrun --spatialite  eps.sqlite --service
 environmental-permits -m metadata.json --install=datasette-cluster-map --install=datasette-vega`

