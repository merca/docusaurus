# Databricks notebook source
# DBTITLE 1,Imports
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------
# DBTITLE 1,Global Variables

# COMMAND ----------
# DBTITLE 1,Read dataframe from blob storage

def read_df_from_blob_storage(account_name, container_name, file_name, file_type):
    df = (
        spark.read.format(file_type)
        .load("abfss://" + container_name + "@" + account_name + ".blob.core.windows.net/" + file_name)
    )
    return df

# COMMAND ----------
# DBTITLE 1,Use this function to get data from blob storage
df = read_df_from_blob_storage("account_name", "container_name", "file_name", "file_type")

# COMMAND ----------
# DBTITLE 1,Write dataframe to blob storage as delta table and register in metastore

df.write.saveAsTable(name="table_name",path="abfss://container_name@account_name.blob.core.windows.net/folder")

# COMMAND ----------
# DBTITLE 1,Read dataframe from metastore
df = spark.table("table_name")