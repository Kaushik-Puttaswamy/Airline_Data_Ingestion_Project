import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node airports_codes_dim
airports_codes_dim_node1738620725241 = glueContext.create_dynamic_frame.from_catalog(database="airline", table_name="dev_airlines_dim_airport_codes", redshift_tmp_dir="s3://redshift-remporary-data-storage",additional_options={"aws_iam_role": "arn:aws:iam::203918882713:role/service-role/AmazonRedshift-CommandsAccessRole-20250113T164521"}, transformation_ctx="airports_codes_dim_node1738620725241")

# Script generated for node daily_flights_raw_from_s3
daily_flights_raw_from_s3_node1738620932134 = glueContext.create_dynamic_frame.from_catalog(database="airline", table_name="flights_raw", redshift_tmp_dir="s3://redshift-remporary-data-storage",additional_options={"aws_iam_role": "arn:aws:iam::203918882713:role/service-role/AmazonRedshift-CommandsAccessRole-20250113T164521"}, transformation_ctx="daily_flights_raw_from_s3_node1738620932134")

# Script generated for node Join_for_departure_details
Join_for_departure_details_node1738621033304 = Join.apply(frame1=daily_flights_raw_from_s3_node1738620932134, frame2=airports_codes_dim_node1738620725241, keys1=["originairportid"], keys2=["airport_id"], transformation_ctx="Join_for_departure_details_node1738621033304")

# Script generated for node Schema_changes_for_departure_details
Schema_changes_for_departure_details_node1738621301760 = ApplyMapping.apply(frame=Join_for_departure_details_node1738621033304, mappings=[("carrier", "string", "carrier", "string"), ("destairportid", "long", "destairportid", "long"), ("depdelay", "long", "dep_delay", "long"), ("arrdelay", "long", "arr_delay", "long"), ("city", "string", "dep_city", "string"), ("name", "string", "dep_airport", "string"), ("state", "string", "dep_state", "string")], transformation_ctx="Schema_changes_for_departure_details_node1738621301760")

# Script generated for node Join_for_arrival_details
Join_for_arrival_details_node1738621587696 = Join.apply(frame1=Schema_changes_for_departure_details_node1738621301760, frame2=airports_codes_dim_node1738620725241, keys1=["destairportid"], keys2=["airport_id"], transformation_ctx="Join_for_arrival_details_node1738621587696")

# Script generated for node Schema_Changes_for_arrival_details
Schema_Changes_for_arrival_details_node1738621680534 = ApplyMapping.apply(frame=Join_for_arrival_details_node1738621587696, mappings=[("carrier", "string", "carrier", "string"), ("dep_delay", "long", "dep_delay", "long"), ("arr_delay", "long", "arr_delay", "long"), ("dep_city", "string", "dep_city", "string"), ("dep_airport", "string", "dep_airport", "string"), ("dep_state", "string", "dep_state", "string"), ("city", "string", "arr_city", "string"), ("name", "string", "arr_airport", "string"), ("state", "string", "arr_state", "string")], transformation_ctx="Schema_Changes_for_arrival_details_node1738621680534")

# Script generated for node Write_in_target_redshift_table
Write_in_target_redshift_table_node1738621852443 = glueContext.write_dynamic_frame.from_catalog(frame=Schema_Changes_for_arrival_details_node1738621680534, database="airline", table_name="dev_airlines_daily_flights_processed", redshift_tmp_dir="s3://redshift-remporary-data-storage",additional_options={"aws_iam_role": "arn:aws:iam::203918882713:role/service-role/AmazonRedshift-CommandsAccessRole-20250113T164521"}, transformation_ctx="Write_in_target_redshift_table_node1738621852443")

job.commit()