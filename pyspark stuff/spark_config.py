"""Launch a SparkSession using a particular configuration.
"""

import pyspark

def start_spark(session_name: str,
                settings: str = 'low') -> pyspark.sql.session.SparkSession:
    """ 'low' = good 'default' settings
    """
    #XXX removed SMLTS setting
    spark = (
        pyspark.sql.SparkSession.builder.appName(session_name)
        .config('spark.executor.memory', '45g')
        .config('spark.executor.cores', 5)
        .config('spark.dynamicAllocation.maxExecutors', 5)
        .config('spark.dynamicAllocation.enabled', 'true')
        .config('spark.default.parallelism', 25)
        .config('spark.sql.shuffle.partitions', 25)
        .config('spark.python.worker.memory', '1g')
        .config('spark.executor.memoryOverhead', '10g')
        .config('spark.sql.broadcastTimeout', 900)
        .getOrCreate()
        )
    
    return spark
    
        