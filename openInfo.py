import pandas as pd
import glob
import os
import logging
logging.basicConfig(filename="Project1_Data/silver_layer/header/newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

files = glob.glob("/Users/natesteckel/Desktop/DEProject_1/Project1_Data/bronze_layer/2018/header/*.csv")

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

new_df1_final = new_df1.assign(year=2018)

new_df1_final.drop(["secondary_notify_party_3", "secondary_notify_party_4", "secondary_notify_party_5",
                    "secondary_notify_party_6", "secondary_notify_party_7", "secondary_notify_party_8",
                    "secondary_notify_party_9", "secondary_notify_party_10", "weight", "weight_unit",
                    "measurement", "measurement_unit", "conveyance_id_qualifier", "in_bond_entry_type",
                    "conveyance_id", "mode_of_transportation", "foreign_port_of_lading_qualifier",
                    "foreign_port_of_destination", "foreign_port_of_destination_qualifier",
                    "port_of_destination", "manifest_unit", "place_of_receipt"], axis=1, inplace=True)


new_df1_final.drop(new_df1_final.index[new_df1_final["record_status_indicator"] == "Deleted"], inplace=True)
new_df1_final.drop(new_df1_final.index[new_df1_final["manifest_quantity"] == 0], inplace=True)

new_df1_final.drop(["record_status_indicator", "manifest_quantity"], axis=1, inplace=True)

final_final = new_df1_final.dropna(subset=["port_of_unlading"])
final_final = final_final.dropna(subset=["foreign_port_of_lading"])
final_final = final_final.dropna(subset=["actual_arrival_date"])

final_final = final_final.drop_duplicates( subset = ['identifier'], keep = 'first').reset_index(drop = True)

final_final["new_vessel_name"] = final_final["vessel_name"].str.replace('[^\w\s\d]',' ')
logger.warning("default value of regex is being changed from true to false")

final_final["new_port_unlading"] = final_final["port_of_unlading"].str.replace('[^\w\s\d]',' ')
logger.warning("default value of regex is being changed from true to false")

final_final["new_foreign_port_lading"] = final_final["foreign_port_of_lading"].str.replace('[^\w\s\d]',' ')
logger.warning("default value of regex is being changed from true to false")

final_final.drop(["vessel_name", "port_of_unlading", "foreign_port_of_lading"], axis=1, inplace=True)


final_final_new = final_final.loc[:, ['identifier', 'carrier_code', 'vessel_country_code', 'new_vessel_name',
                                      'new_port_unlading', 'new_foreign_port_lading', 'secondary_notify_party_1',
                                      'secondary_notify_party_2', 'estimated_arrival_date',
                                      'actual_arrival_date', 'year']]

logger.info("FInal Columns reordered.")

final_final_new = final_final_new.dropna(subset=['carrier_code'])

final_final_new.reset_index(drop=True, inplace=True)


final_final_new.to_csv(r"Project1_Data/silver_layer/header/header_full_2018_sorted.csv", index=False)
logger.debug("CSV written in.")

logger.info(final_final.head(5))

logger.info(len(final_final.index))


print('Operation complete.')
