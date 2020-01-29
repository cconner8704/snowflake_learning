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
