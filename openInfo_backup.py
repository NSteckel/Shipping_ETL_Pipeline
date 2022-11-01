import pandas as pd
import logging

// Information about the hazardous material in specific shipments. Material type, flashpoint, etc.

logging.basicConfig(filename="Project1_Data/silver_layer/hazmat/newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

df1 = pd.read_csv("Project1_Data/bronze_layer/2018/hazmat/ams__hazmat_2018__202001290000_part_0.csv")

pd.set_option('display.max_columns', None)


new_df1 = df1.copy(deep=True)
logger.info("table duplicated!")

new_df1.drop_duplicates(inplace=True)
new_df1_final = new_df1.assign(year=2018)


new_df1_final = new_df1_final.drop_duplicates( subset = ['identifier'], keep = 'first').reset_index(drop = True)

new_df1_final['hazmat_flash_point_temperature'] = pd.to_numeric(new_df1_final['hazmat_flash_point_temperature'], errors='coerce')
new_df1_final['hazmat_class'] = pd.to_numeric(new_df1_final['hazmat_class'], errors='coerce')
logger.debug("Two tables converted and coerced to numeric")

final_final = new_df1_final.dropna(subset=["hazmat_flash_point_temperature_unit"])
final_final = final_final.dropna(subset=["hazmat_class"])
final_final = final_final.dropna(thresh=9)

final_final.reset_index(drop=True, inplace=True)


final_final.to_csv(r"Project1_Data/silver_layer/hazmat/hazmat_part_0_2018_sorted.csv", index=False)
logger.debug("CSV written to...")
logger.info(" ")
logger.info(final_final.head(5))

logger.info(len(final_final.index))


print('Operation Complete!')


