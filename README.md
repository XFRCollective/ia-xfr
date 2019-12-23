# internetarchive

Scripts we use to administer the XFR Collective collection using Internet Archive's python libraries. 

--

## Install Dependencies

python
pandas
pip
internetarchive

before running any of the scripts below, be sure to log into your internet archive account using `ia config`

--

## ia-csv.py

This script exports all metadata in an internet archive collection as a .csv file. The file can then be edited and uploaded back into internet archive using the command `ia metadata --spreadsheet="xfrcollective.csv`.  

To run the script

1. Install all dependencies
2. Copy ia-csv.py script
3. Run `ia config [internet archive login]`
4. Run `python ia-csv.py [collection name] [output file]`
