import pandas as pd
import glob
import os
import logging

// information about the container (container number, cargo description, etc.)
logging.basicConfig(filename="Project1_Data/silver_layer/cargodesc/newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)


files = glob.glob("/Users/natesteckel/Desktop/DEProject_1/Project1_Data/bronze_layer/2018/cargodesc/*.csv")

frame = []
for file in files:
    df = pd.read_csv(file)
    frame.append(df)
    logger.info("file read.")

df = pd.concat(frame)

pd.set_option('display.max_columns', None)

new_df1 = df.copy(deep=True)
logger.info("table duplicated!")


new_df1.drop_duplicates(inplace=True)


new_df1_final = new_df1.drop_duplicates(subset=['identifier'], keep='first').reset_index(drop=True)


final_final = new_df1_final.dropna(subset=['piece_count'])
final_final = final_final.dropna(subset=['container_number'])


final_final["new_description"] = final_final["description_text"].str.replace('[^\w\s\d]','')
logger.warning("default value of regex is being changed from true to false")


final_final.drop("description_sequence_number", axis=1, inplace=True)
final_final.drop("description_text", axis=1, inplace=True)


# final_final = final_final.assign(year=2018)
final_final.reset_index(drop=True, inplace=True)

final_final.to_csv(r"Project1_Data/silver_layer/cargodesc/cargodesc_full_2018_sorted.csv", index=False)
logger.debug("CSV written in.")

logger.info(final_final.head(5))

logger.info(len(final_final.index))


