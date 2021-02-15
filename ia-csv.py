# Dumps JSON to textfile for items within an IA collection

import internetarchive
import sys
import os
import pandas as pd
import json
from tempfile import NamedTemporaryFile

argv = sys.argv
collection = argv[1] # Collection name to scrape
output_file = argv[2] # Name of outfile for CSV dump

search_collection = internetarchive.search_items('collection:' + argv[1])

print str(search_collection.num_found) + " items in collection"

with NamedTemporaryFile(delete=False) as outfile:
  outfile.write('{"collection_items" : [')
  for result in search_collection:
    item_identifier = result['identifier']
    item = internetarchive.get_item(item_identifier)

    print "Downloading " + item_identifier + " ..."

    jdata = item.item_metadata['metadata']
    json_record = json.dumps(jdata)

    outfile.write(str(json_record) + ",")
  outfile.seek(-1, os.SEEK_END)
  outfile.truncate()
  outfile.write(']}')

with open(outfile.name, 'r') as f:
  data = json.load(f)
  df = pd.DataFrame(data['collection_items'])
  df.to_csv(output_file, index=False, encoding="UTF-8")

os.remove(outfile.name)
# Dumps JSON to textfile for items within an IA collection

import internetarchive
import sys
import os
import pandas as pd
import json
from tempfile import NamedTemporaryFile

argv = sys.argv
collection = argv[1] # Collection name to scrape
output_file = argv[2] # Name of outfile for CSV dump

search_collection = internetarchive.search_items('collection:' + argv[1])

print(str(search_collection.num_found) + " items in collection")

with NamedTemporaryFile(mode="wb", delete=False) as outfile:
  outfile.write(bytes('{"collection_items" : [', 'ascii'))
  for result in search_collection:
    item_identifier = result['identifier']
    item = internetarchive.get_item(item_identifier)

    print("Downloading " + item_identifier + " ...")

    jdata = item.item_metadata['metadata']
    json_record = json.dumps(jdata)

    outfile.write(bytes(str(json_record) + ",", 'ascii'))
  outfile.seek(-1, os.SEEK_END)
  outfile.truncate()
  outfile.write(bytes(']}', 'ascii'))

with open(outfile.name, 'r') as f:
  data = json.load(f)
  df = pd.DataFrame(data['collection_items'])
  df.to_csv(output_file, index=False, encoding="UTF-8")

os.remove(outfile.name)
