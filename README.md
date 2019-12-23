# Internet Archive Repo Management

This repository contains scripts and commands used by XFR Collective to administer files and metadata on Internet Archive. These scripts were written for Unix. Many thanks to Spencer Portée and Nıck Krabbenhöft for their contributions. 

## Dependencies

Installing the programs below is all very easy with Homebrew, so install that first if you can: https://brew.sh/. Install in the order listed. 

- python [brew install python]
- pip [brew install pip] 
- pandas [pip install pandas] 
- internetarchive [pip install internetarchive] 

Before running any of the scripts below, be sure to log into your internet archive account using `ia config`

## Export Metadata 

The ia-csv.py script exports all metadata in an internet archive collection as a .csv file. The file can then be edited and uploaded back into internet archive using the command `ia metadata --spreadsheet="xfrcollective.csv`.  

To run the script

1. Install all dependencies
2. Copy ia-csv.py script
3. Run `ia config [internet archive login]`
4. Run `python ia-csv.py [collection name] [output file]` 

## Edit and Upload Metadata

Once the .csv file has been exported, it can be edited and the new data re-imported into Internet Archive. 

1. Export .csv file using the instructions above
2. Edit .csv file in Excel or another spreadsheet program. Do not change the name of any header field.  
3. Save edited .csv file AS a .csv file
4. Run `ia config [internet archive login]`
5. Run `ia metadata --spreadsheet="uploading.csv"`
