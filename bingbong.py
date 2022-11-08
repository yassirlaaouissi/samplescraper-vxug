import os
import sys
import time
import hashlib
from mwdblib import MWDB

print("""
                                                    ███████╗ █████╗ ███╗   ███╗██████╗ ██╗     ███████╗ 
                                                    ██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝ 
                                                    ███████╗███████║██╔████╔██║██████╔╝██║     █████╗   
                                                    ╚════██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝   
                                                    ███████║██║  ██║██║ ╚═╝ ██║██║     ███████╗███████╗ 
                                                    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝ 
                                                                                                        
                                                ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
                                                ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                                                ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
                                                ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
                                                ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
                                                ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                        
                                                            ██╗   ██╗██╗  ██╗██╗   ██╗ ██████╗          
                                                            ██║   ██║╚██╗██╔╝██║   ██║██╔════╝          
                                                            ██║   ██║ ╚███╔╝ ██║   ██║██║  ███╗         
                                                            ╚██╗ ██╔╝ ██╔██╗ ██║   ██║██║   ██║         
                                                             ╚████╔╝ ██╔╝ ██╗╚██████╔╝╚██████╔╝         
                                                              ╚═══╝  ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    

""")

apikey = input("Whats the API key: ")

mwdb = MWDB(api_url="https://virus.exchange/api",api_key=apikey)

results = mwdb.search_files('upload_time:[2021-10-01 TO *]')

for sample in results:
    with open("malware_samples/" + sample.file_name, "wb") as f:
        f.write(sample.download())
    print("Downloaded {}".format(sample.file_name))
    time.sleep(1) # leave this in, otherwise I will yeet your API Key to Uzbekistan