# Use of mypy to check data types

def myfunction(myparameter: int) -> str:
    return f"{myparameter + 10}"

def otherfunction(otherparameter:str):
    print(otherparameter)

test = 20 
# otherfunction(myfunction(20))


## Testing Type Hinting with Spark Dataframe
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


def reduce_dataframe(df_source: DataFrame, column_name: str) -> DataFrame:
    return df_source.select(f"{column_name}")

def write_csv(df_source: DataFrame):
    df_source.write.csv('test.csv')

spark = SparkSession.builder.appName("Create DataFrame").getOrCreate()

data = [("John", 25), ("Mary", 30), ("Mike", 35)]

schema = StructType([
  StructField("name", StringType()),
  StructField("age", IntegerType())
])

df = spark.createDataFrame(data, schema)

df_read = spark.read.csv('test.csv')

# reduce_dataframe("test", "_c0").show()

print(type(df_read.collect()))