# Internet Archive File and Metadata Management 

This repository contains scripts and commands used by XFR Collective to administer files and metadata on Internet Archive.  

## Dependencies

These scripts were written for Unix, specifically MAC/Terminal. Install programs in the order they are listed: 

- homebrew https://brew.sh/, or, if already installed `brew upgrade` 
- python `brew install python`
- pip `brew install pip`
- pandas `pip install pandas`
- internetarchive `pip install internetarchive`

Before running the scripts or commands below, be sure to log into your internet archive account using `ia config`. 

## Bulk Export Metadata 

The ia-csv.py script in this repository exports all metadata from an Internet Archive collection as a .csv file. The file can then be edited and uploaded back into internet archive by following the Bulk Edit Metadata script below. The ia-csv.py script was adapted from the ia-json.py script created by Github user pwallace: https://github.com/pwallace/metadata-processing. 

To run the script: 

1. Copy ia-csv.py script and save to your computer
2. Run `ia config [internet archive login]`
3. Run `python ia-csv.py [collection name] [output file]` 

## Bulk Edit Metadata

Once the .csv file has been exported, it can be edited and the new data re-imported into Internet Archive. 

1. Export the .csv file using the instructions above
2. Edit .csv file in Excel or another spreadsheet program. Do not change the name of any header field.  
3. Save edited .csv file AS a .csv file
4. Run `ia config [internet archive login]`
5. Run `ia metadata --spreadsheet="[filename].csv"`

## Bulk File Import 

Coming Soon

## Single File Import

Coming Soon

## Single Edit Metadata

Coming Soon

## Contributors

- Kelly Haydon
- Spencer Portée 
- Nıck Krabbenhöft 


