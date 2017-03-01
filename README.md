# flowerpowerparrot
script to download data of parrot flower power sensors using 'powerpot' API
Runs best in Anaconda using Spyder interface.
To run, set working directory to where the scripts are; for now the output is written to subfolders in that folder
Input_file.xls is used to set parameters (which flowerpower account, which sensors, which dates and other switches)
Output with 15-minute data go to a folder indicating date/time/account and within that folder a folder per sensor
An overall raw-data file is produced. 
After retrieving data from the cloud, standardisation and/or dataprocessing takes place and some graphs are created.
These are written in the folder ./processed and in a subfolder indicating the date/time/account.
Within that subfolder a subfolder is created with 15-minute data and grahps and with daily data and graphs, both with subfolders per sensor. In 'daily data'  overall output per trait for all sensors with averaged, or processed, daily data is written.
