nohup hive --service metastore  > hive-metastore.log 2>&1 &
nohup hive --service hiveserver2 > hive-hiveserver2.log 2>&1 &
