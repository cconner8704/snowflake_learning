First entry:      
      
- Install python3      
      
brew install python3      
      
- Update path:      
      
cat >> ~/.zprofile << EOF  #or .profile if you're not using zsh      
export PATH=/usr/local/bin:/usr/local/Cellar/python/3.7.6_1/libexec/bin/pip:\$PATH      
EOF      
      
source ~/.zprofile      
      
- Install snowflake connector:      
      
/usr/local/Cellar/python/3.7.6_1/libexec/bin/pip install snowflake-connector-python      
      
- Export env vars:      
      
export PASSWORD=      
export USER=      
export ACCOUNT=      
export WAREHOUSE=      
export DATABASE=      
export ROLE=      
      
- Run the script:      
      
python3 test_connection.py      
      
KAFKA CONNECTOR:  
      
- Docker kafka      
https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.kafka_mt.mbm_rgn.namer_lng.eng_dv.all&utm_term=%2Bkafka%20%2Bdocker&creative=&device=c&placement=&gclid=CjwKCAiA98TxBRBtEiwAVRLqu7MWSo_TyCUmpY__KpK5QEkLBg_QV9XfCW0-PRgc4S7SUDFpixdj5hoCgjQQAvD_BwE      
https://medium.com/@koen.vantomme/confluent-docker-kafka-using-snowflake-sink-and-snowflake-source-af6b19c88302      
https://docs.snowflake.net/manuals/user-guide/kafka-connector.html      
https://docs.snowflake.net/manuals/user-guide/kafka-connector.html#using-key-pair-authentication      
      
#Tools to make life cool    
brew cask install xquartz    
brew install xclip    
brew install gnu-sed    
    
###CURRENT####      
cd snowflake_learning/confluent_with_connector      
openssl genrsa -out rsa_key.pem 2048      
#This will ask for password, enter one and use in following 2 commands      
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8      
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub      
openssl rsa -in rsa_key.p8 -out rsa_key.priv      
      
#The public key needs to be added manually to Snowflake the database and the .p8 file needs to be added to the sink connector definition, “snowflake.private.key”:”xx”,Important: remove new lines and also the header and footer from the key.      
  
#Create the key string for Snowflake:    
grep -v KEY rsa_key.pub | tr -d \\n    
    
#Go to Snowflake editor and update key for your user with the generated public key:      
use role securityadmin;  
alter user <user_changeme> set rsa_public_key_2='XXXXXXXX…';      

#This is the snowflake connector config, we will update the json key from
#rsa_key.p8 and inject with gsed    
cp snowflake-connector-kafkapoc.json.example snowflake-connector-kafkapoc.json    
gsed -i "s*\"xx\",*\"$(grep -v KEY rsa_key.p8 | tr -d \\n)\",*g" snowflake-connector-kafkapoc.json    

#UPDATE snowflake-connector-kafkapoc.json with correct info these properties:      
#    "snowflake.url.name":"<url_changeme>.snowflakecomputing.com",
#    "snowflake.user.name":"<user_changeme>",
#    "snowflake.private.key.passphrase":"<keypass_changeme>",
#    "snowflake.database.name":"kafka_<user_changeme>_db",
#    "snowflake.schema.name":"kafka_<user_changeme>_schema",

#This will build the image and start
docker-compose up -d --build      

#This will show running processes:
docker-compose ps      

#These commands validate things started:

# We expect empty response []:  
curl localhost:8083/connectors  
  
#Should have snowflake sink:  
curl localhost:8083/connector-plugins  
      
#This is the UI, but we don't need to access it:
      
http://localhost:9021/      
  

#This is SQL side setup
 
#Create databases and schema 
use role <dbadmin_or_whatever>;
create database kafka_<user_changeme>_db;  
use kafka_<user_changeme>_db;  
create schema kafka_<user_changeme>_schema;  
use kafka_<user_changeme>_schema;  

#Now we do grants
#Use a role that can create and manage roles and privileges:  
use role securityadmin;  
  
#Create a Snowflake role with the privileges to work with the connector  
create role kafka_connector_role_<user_changeme>;  
  
#Grant privileges on the database:  
grant usage on database kafka_<user_changeme>_db to role kafka_connector_role_<user_changeme>;  
  
#Grant privileges on the schema:  
grant usage on schema kafka_<user_changeme>_db.kafka_<user_changeme>_schema to role kafka_connector_role_<user_changeme>;  
grant create table on schema kafka_<user_changeme>_db.kafka_<user_changeme>_schema to role kafka_connector_role_<user_changeme>;  
grant create stage on schema kafka_<user_changeme>_db.kafka_<user_changeme>_schema to role kafka_connector_role_<user_changeme>;  
grant create pipe on schema kafka_<user_changeme>_db.kafka_<user_changeme>_schema to role kafka_connector_role_<user_changeme>;  
  
#Grant the custom role to an existing user:  
grant role kafka_connector_role_<user_changeme> to user <user_changeme>;  
  

#Start data generator  
  
curl -X POST -H "Content-Type: application/json" --data '{"name": "datagen-clickstream", "config": {"connector.class": "io.confluent.kafka.connect.datagen.DatagenConnector",  
    "name":"datagen-clickstream",  
    "kafka.topic": "CLICKSTREAM_TOPIC",  
    "quickstart": "clickstream",  
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",  
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",  
    "value.converter.schemas.enable": "false",  
    "max.interval": 1000,  
    "iterations": 10000000,  
    "tasks.max": "1" }}' http://localhost:8083/connectors  
  
  
#Check data generator  
  
curl localhost:8083/connectors/datagen-clickstream/status/  
  
#Start Snowflake Sink:  
docker exec -it connect curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @/tmp/snowflake-connector-kafkapoc.json  
  
#Check snowflake sink status  
curl localhost:8083/connectors/SnowflakeSinkConnector/status/  
  
  
COMMANDS of NOTE:  
  
docker stop $(docker ps -a -q)  
docker rm $(docker ps -a -q)  
docker image ls -a  
docker rmi xxx  
docker-compose build  
docker-compose up  



#####Notes for later####  
docker exec -it connect curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{ "name": "jdbc_source_snowflake_v1", "config": { "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector", "connection.url": "jdbc:snowflake://xxxxx.snowflakecomputing.com:443/?warehouse=<user>_wh", "connection.user": "<user>", "connection.password": "pass", "topic.prefix": "pockafka", "mode":"bulk", "max.interval": 1000, "iterations": 10000000, "tasks.max": "1", "table.whitelist" : "SANDBOX.KAFKA_ORIG.CUSTOMER_DEMOGRAPHICS,SANDBOX.KAFKA_ORIG.CUSTOMER,SANDBOX.KAFKA_ORIG.CATALOG_SALES", "key.converter":"org.apache.kafka.connect.storage.StringConverter", "value.converter": "org.apache.kafka.connect.json.JsonConverter", "value.converter.schemas.enable": "false" } }'  
