import ast
p = "{'tpch': ['connector.name=tpch'],'jmx':['connector.name=jmx'],'mongodb':['connector.name=mongodb','mongodb.seeds=10.254.100.139:20000'],'hive':['connector.name=hive-hadoop2','hive.metastore.uri=thrift://10.151.139.105:9083','hive.config.resources=/etc/hadoop/conf/core-site.xml,/etc/hadoop/conf/hdfs-site.xml']}"
# print p

past = ast.literal_eval(p)
print past
for l in past:
    print l
    # print past[l]
    for i in past[l]:
        print i