COPY cargodesc(identifier, container_number, piece_count, new_description, year)
FROM '/DEProject_1/Project1_Data/silver_layer/cargodesc/cargodesc_full_2018_sorted.csv'
DELIMITER ','
CSV HEADER;


COPY container(identifier, container_number, seal_number_1, seal_number_2, container_length, container_height, container_width, container_type, type_of_service, year)
FROM '/DEProject_1/Project1_Data/silver_layer/container/container_full_2018_sorted.csv'
DELIMITER ','
CSV HEADER;


COPY generalhead(identifier, carrier_code, vessel_country_code, new_vessel_name, new_port_unlading, new_foreign_port_lading, secondary_notify_party_1, secondary_notify_party_2, estimated_arrival_date, actual_arrival_date year)
FROM '/DEProject_1/Project1_Data/silver_layer/header/header_full_2018_sorted.csv'
DELIMITER ','
CSV HEADER;


COPY hazmat(identifier, container_number, hazmat_sequence_number, hazmat_code, hazmat_class, hazmat_code_qualifier, hazmat_contact, hazmat_page_number, hazmat_flash_point_temperature, hazmat_flash_point_temperature_negative_ind, hazmat_flash_point_temperature_unit, hazmat_description, year)
FROM '/DEProject_1/Project1_Data/silver_layer/hazmat/hazmat_part_0_2018_sorted.csv'
DELIMITER ','
CSV HEADER;


COPY hazmatclass(identifier, container_number, hazmat_sequence_number, hazmat_classification, year)
FROM '/DEProject_1/Project1_Data/silver_layer/hazmatclass/hazmatclass_part_0_2018_sorted.csv'
DELIMITER ','
CSV HEADER;