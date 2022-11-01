import pandas as pd
import glob
import os
import logging

// information about the container. Size, seal type, number of units, etc.
logging.basicConfig(filename="Project1_Data/silver_layer/container/newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

files = glob.glob("/Users/natesteckel/Desktop/DEProject_1/Project1_Data/bronze_layer/2018/container/*.csv")

frame = []
for file in files:
     df = pd.read_csv(file)
     frame.append(df)
     logger.info("file read.")

df = pd.concat(frame)

pd.set_option('display.max_columns', None)

new_df1 = df.copy(deep=True)
logger.info("table duplicated!")


new_df1.drop(new_df1.index[new_df1["container_height"] == 0], inplace=True)
new_df1.drop(new_df1.index[new_df1["container_width"] == 0], inplace=True)
new_df1.drop(new_df1.index[new_df1["container_length"] == 0], inplace=True)

new_df1[new_df1["load_status"].str.contains("Empty")==False]


new_df1.drop_duplicates(inplace=True)

new_df1_final = new_df1.assign(year=2018)
new_df1_final = new_df1_final.drop_duplicates( subset = ['identifier'], keep = 'first').reset_index(drop = True)


final_final = new_df1_final.dropna(subset=['identifier'])
final_final = new_df1_final.dropna(subset=['seal_number_1'])
final_final = new_df1_final.dropna(subset=['container_type'])
final_final.reset_index(drop=True, inplace=True)

# new_df1_final.drop(["load_status"], axis=1)

final_final.drop("load_status", axis=1, inplace=True)
final_final.drop("equipment_description_code", axis=1, inplace=True)
# new_df1_final.drop("type_of_service", axis=1, inplace=True)
final_final = final_final.dropna(subset=['container_number'])

final_final.to_csv(r"Project1_Data/silver_layer/container/container_full_2018_sorted.csv", index=False)
logger.debug("CSV written in.")

logger.info(final_final.head(5))

logger.info(len(final_final.index))


print('Operation Complete!')
