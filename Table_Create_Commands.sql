CREATE TABLE IF NOT EXISTS public.cargodesc
(
    identifier bigint NOT NULL,
    container_number text COLLATE pg_catalog."default" NOT NULL,
    piece_count numeric,
    new_description text COLLATE pg_catalog."default",
    year integer,
    CONSTRAINT cargodesc_pkey PRIMARY KEY (identifier)
)


CREATE TABLE IF NOT EXISTS public.container
(
    identifier bigint NOT NULL,
    container_number text COLLATE pg_catalog."default" NOT NULL,
    seal_number_1 text COLLATE pg_catalog."default",
    seal_number_2 text COLLATE pg_catalog."default",
    container_length bigint NOT NULL,
    container_height bigint NOT NULL,
    container_width bigint NOT NULL,
    container_type text COLLATE pg_catalog."default",
    type_of_service text COLLATE pg_catalog."default",
    year integer,
    CONSTRAINT container_pkey PRIMARY KEY (identifier)
)


CREATE TABLE IF NOT EXISTS public.generalhead
(
    identifier bigint NOT NULL,
    carrier_code text COLLATE pg_catalog."default" NOT NULL,
    vessel_country_code text COLLATE pg_catalog."default",
    new_vessel_name text COLLATE pg_catalog."default",
    new_port_unlading text COLLATE pg_catalog."default",
    new_foreign_port_lading text COLLATE pg_catalog."default",
    secondary_notify_party_1 text COLLATE pg_catalog."default",
    secondary_notify_party_2 text COLLATE pg_catalog."default",
    estimated_arrival_date date,
    actual_arrival_date date,
    year integer,
    CONSTRAINT generalhead_pkey PRIMARY KEY (identifier)
)


CREATE TABLE IF NOT EXISTS public.hazmat
(
    identifier bigint NOT NULL,
    container_number text COLLATE pg_catalog."default" NOT NULL,
    hazmat_sequence_number integer,
    hazmat_code text COLLATE pg_catalog."default",
    hazmat_class numeric NOT NULL,
    hazmat_code_qualifier character(1) COLLATE pg_catalog."default",
    hazmat_contact text COLLATE pg_catalog."default",
    hazmat_page_number text COLLATE pg_catalog."default",
    hazmat_flash_point_temperature numeric,
    hazmat_flash_point_temperature_negative_ind character(1) COLLATE pg_catalog."default",
    hazmat_flash_point_temperature_unit character(2) COLLATE pg_catalog."default",
    hazmat_description text COLLATE pg_catalog."default",
    year integer,
    CONSTRAINT hazmat_pkey PRIMARY KEY (identifier)
)


CREATE TABLE IF NOT EXISTS public.hazmatclass
(
    identifier bigint NOT NULL,
    container_number text COLLATE pg_catalog."default",
    hazmat_sequence_number integer,
    hazmat_classification numeric,
    year integer,
    CONSTRAINT hazmatclass_pkey PRIMARY KEY (identifier)
)