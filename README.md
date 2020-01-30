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
    
    
COMING SOON:    
    
- Docker kafka    
https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.nonbrand_tp.prs_tgt.kafka_mt.mbm_rgn.namer_lng.eng_dv.all&utm_term=%2Bkafka%20%2Bdocker&creative=&device=c&placement=&gclid=CjwKCAiA98TxBRBtEiwAVRLqu7MWSo_TyCUmpY__KpK5QEkLBg_QV9XfCW0-PRgc4S7SUDFpixdj5hoCgjQQAvD_BwE    
https://medium.com/@koen.vantomme/confluent-docker-kafka-using-snowflake-sink-and-snowflake-source-af6b19c88302    
https://docs.snowflake.net/manuals/user-guide/kafka-connector.html    
https://docs.snowflake.net/manuals/user-guide/kafka-connector.html#using-key-pair-authentication    
    
#####OLD#######    
git clone https://github.com/confluentinc/examples    
cd examples    
git checkout 5.4.0-post    
cd cp-all-in-one/    
docker-compose up -d --build    
docker-compose ps    
    
###CURRENT####    
cd snowflake_learning/confluent_with_connector    
openssl genrsa -out rsa_key.pem 2048    
#This will ask for password, enter one and use in following 2 commands    
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8    
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub    
openssl rsa -in rsa_key.p8 -out rsa_key.priv    
    
#The public key needs to be added manually to Snowflake the database and the .p8 file needs to be added to the sink connector definition, “snowflake.private.key”:”xx”,Important: remove new lines and also the header and footer from the key.    
    
#Tools to make life cool  
brew cask install xquartz  
brew install xclip  
brew install gnu-sed  
  
#Create the key string for Snowflake:  
grep -v KEY rsa_key.pub | tr -d \\n  
  
#Go to Snowflake editor and update key for your user with the generated public key:    
use role securityadmin;
alter user jsmith set rsa_public_key_2='JERUEHtcve…';    
    
cp snowflake-connector-kafkapoc.json.example snowflake-connector-kafkapoc.json  
gsed -i "s*\"xx\",*\"$(grep -v KEY rsa_key.p8 | tr -d \\n)\",*g" snowflake-connector-kafkapoc.json  
#UPDATE snowflake-connector-kafkapoc.json with correct info these properties:    
#    "snowflake.url.name":"koen.eu-central-1.snowflakecomputing.com",    
#    "snowflake.user.name":"koen@koen.io",    
#    "snowflake.private.key":"xx",    
#    "snowflake.private.key.passphrase":"koen",    
#    "snowflake.database.name":"sandbox",    
#    "snowflake.schema.name":"kafka_target",    
docker-compose up -d --build    
docker-compose ps    
    
- Connect here:    
    
http://localhost:9021/    
