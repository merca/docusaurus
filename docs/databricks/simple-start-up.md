---
sidebar_position: 1
---

# Spark startup

:::note Cloud

All my docs are related to developing in Azure if nothing stated othervise, since this is my main cloud.

:::

First step in spark is usually loading in some data and here is simple setup for doing that.

:::info

Download [Full notebook](../../downloadble_files/notebooks/easy_startup.py)

:::

I always include following imports in my notebooks when I start developing. After I'm done with a feature, I clean up and include only used imports.

```python
from pyspark.sql.functions import *
from pyspark.sql.types import *
```

I also like to have a function to create a dataframe from a list of tuples. I use this function a lot when I'm testing my code.

```python
def create_df_from_tuples(tuples, schema):
    return spark.createDataFrame(tuples, schema)
```

I also like to have a function to read data from Azure Blob Storage. I use this function a lot when I'm testing my code.

```python
def read_from_blob_storage(path, format):
    return spark.read.format(format).load(path)
```
