# Shipping_ETL_Pipeline

- Description of each file below -

Planned and developed an extract, transform, load pipeline that takes shipping data from 2018, cleans it, and than logs and reloads the data into 
csv files to be queried in PostgreSQL. 

Developed a data engineering pipeline to extract, transform, and load several data files from the AWS marketplace (Enigma AMS shipments 2018-2020) 
Cleaned the data and created a log of all operations being performed on the dataset. Also wrote queries to show meaningful aggregations of that data.

This project deals specifically with data about any containers carrying hazardous materials

!! Please Note !!
The original data files for one year total about 40 Gigabytes of data, so they are not provided in this project's files. It interested in obtaining these files for a project, the original data can be obtained here: 
https://aws.amazon.com/marketplace/pp/prodview-stk4wn3mbhx24?sr=0-16&ref_=beagle&applicationId=AWSMPContessa#similarProducts

The 'Copy_Commands' and 'Table_Create_Commands' sql files are used to create the sql tables and then copy data into them after the data has been processed in Pandas. The code written here is specific to my file system (as the code here is hosted locally on my computer) and so use of these files is not recommended without significant adjustment to the file paths.

There are 5 python files that read the data in and clean it. Each file is specific to a different table of data that I wanted to use in my final product / ER Diagram.

1. openInfo.py: general information about shipments (destination, origin, duration, container type, etc.)
2. openInfo_backup.py: information about the hazardous material in specific shipments. (Material type, flashpoint, etc.)
3. openInfo_container.py: information about the container. (Size, seal type, number of units, etc.)
4. openInfo_descc.py: information about the container (container number, cargo description, etc.)
5. openInfo_hazmatclass.py: information about the classification of the material in a container (class number, identifier, etc.)
