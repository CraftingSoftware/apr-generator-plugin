import csv

""""This file, when put into `SheetShuttle/plugins`, can be run to display the contents of the sheet."""
from sheetshuttle import sheet_collector
import pandas as pd
#from sheetshuttle import Sheet

# File containing authentication information. DON'T PUSH `new_key.json` TO GITHUB!!!
key_file='new_key.json'
# Directory containing config information for our google sheet
sources_dir='config/sheet_sources'

def run(sheets_keys_file, sheets_config_directory, **kwargs):
     """Example run function. Collect and display info from google sheet."""
     # Create SheetCollector object named `my_collector`
     #   Created with args `key_file` and `sources_dir`
     my_collector = sheet_collector.SheetCollector(key_file, sources_dir)
     my_collector.collect_files()
     # Display contents of the sheet

     #my_collector.print_contents()

     # print((type(my_collector.sheets_data)))
     # print(my_collector.sheets_data.values)

     #my_sheet = sheet_collector.Sheet()

     #     for key, s in my_collector.sheets_data.items():
     #          print(key,s.regions)


     #     #my_collector.sheets_data["APR-Generator-Config"].regions["Students_Info"].print_region()
     #     for key, value in my_collector.sheets_data["APR-Generator-Config"].regions:
     #           print(key,value) 

     # for region_id, region in my_collector.sheets_data["APR-Generator-Config"].regions["Sheet1_Students_Info"]:
     #        print(f"******\t {region_id} \t ******")
     #        region.print_region()
     #        print("*********************************")


     my_data = my_collector.sheets_data["APR-Generator-Config"].regions["Sheet1_Students_Info"].data  
     print(my_data)
     print(type(my_data))
     print('\n\n\n')

     csv_data = my_data.to_csv()
     print(csv_data)
     print(type(csv_data))

     # for region in my_collector.sheets_data["APR-Generator-Config"].regions:
     #      print(region)

     #for fuckyou in my_collector.sheets_data["APR-Generator-Config"].regions:
     #my_collector.print_contents()
     