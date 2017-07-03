import csv
from itertools import groupby

import glob, os
os.chdir("geojson")
for file in glob.glob("*.geojson"):
    print('"'+file+'"'+','),

# for key, rows in groupby(csv.reader(open("Ins_list.csv")),
#                          lambda row: row[3]):
#     with open("assets/%s.csv" % key, "w") as output:
#         output.write("inst name, eiin, inst_type, district, thana, mauza, long, lat, serial,isUnique" + "\n")
#         for row in rows:
#             output.write(",".join(row) + "\n")