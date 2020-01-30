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

git clone https://github.com/confluentinc/examples
cd examples
git checkout 5.4.0-post
cd cp-all-in-one/
docker-compose up -d --build
docker-compose ps

- Connect here:

http://localhost:9021/
