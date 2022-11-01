import pandas as pd
import logging

// information about the classification of the material in a container (class number, identifier, etc.)

logging.basicConfig(filename="Project1_Data/silver_layer/hazmatclass/newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)


df1 = pd.read_csv("Project1_Data/bronze_layer/2018/hazmatclass/ams__hazmatclass_2018__202001290000_part_0.csv")

pd.set_option('display.max_columns', None)


new_df1 = df1.copy(deep=True)
logger.info("table duplicated!")


new_df1.drop_duplicates(inplace=True)

new_df1_final = new_df1.assign(year=2018)

new_df1_final['hazmat_classification'] = pd.to_numeric(new_df1_final['hazmat_classification'], errors = 'coerce')


new_df1_final = new_df1_final.drop_duplicates(subset=['identifier'], keep = 'first').reset_index(drop = True)

for x in new_df1_final.index:
  if new_df1_final.loc[x, "hazmat_classification"] > 9:
    new_df1_final.drop(x, inplace = True)


final_final = new_df1_final.dropna(subset=['hazmat_classification'])

final_final.reset_index(drop=True, inplace=True)


final_final.to_csv(r"Project1_Data/silver_layer/hazmatclass/hazmatclass_with_log_2018_sorted.csv")
logger.debug("CSV written to...")
logger.info(" ")
logger.info(final_final.head(5))

logger.info(len(final_final.index))
