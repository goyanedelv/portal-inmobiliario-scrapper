import pandas as pd
import numpy as np
import datetime
import os
import yaml

with open("parametros.yaml", 'r') as stream:
    try:
        parameters = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
db = []

arr = os.listdir("data/raw_output/")

arr = list(filter(lambda k: ".txt" in k, arr))

UF_CLP = float(parameters['UF'])

cols = ['price', 'address', 'surface']

for i in arr:
    with open(f"data/raw_output/{i}", encoding="utf-8") as f:

        lines = f.readlines()

        lenn = len(lines)
        print(i)
        j = 1

        precio_1 = None
        metraje_1 = None
        address_1 = None

        for line in lines:
            if ("undefined" in line) | ("pesos" in line):
                
                if((precio_1 != None) & (address_1 != None)):
                    db .append([precio_1, address_1, metraje_1])
                    precio_1 = None
                    metraje_1 = None
                    address_1 = None
                
                line = line.replace(",","")

                if ("undefined" in line):

                    if "con" in line:
                        pos_con = line.find(" con")

                        precio_1 = int(line[:pos_con].replace(" undefined","").replace("\n",""))
                    else:
                        precio_1 = int(line.replace(" undefined","").replace("\n",""))
                else:
                    precio_pre = int(line.replace(" pesos","").replace("\n","")) / UF_CLP
                    precio_1 = precio_pre
            
            if ("útiles" in line):
                line = line.replace(",","")
                pos = line.find("-")

                if pos > 0:

                    surface = float(line[:pos-1])
                    metraje_1 = surface
                else:
                    metraje_1 = float(line.replace(" m² útiles",""))

            if (("Departamento en venta" in line) | ("Casa en venta" in line)):
                address_1 = lines[j].replace(",","")

            j += 1
        j = 0
        

df = pd.DataFrame(db, columns = cols)

ct = datetime.datetime.now()
time_tag = str(ct).replace(":","").replace(" ","-")[:17]

post_tag = i.replace("_raw.txt","")
df = df.drop_duplicates()
df.to_excel(f"data/db_output/{time_tag}_pi_{post_tag}.xlsx", index = False)



