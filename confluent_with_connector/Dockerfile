FROM confluentinc/cp-kafka-connect:5.3.1

# Create plugin directory
RUN mkdir -p /etc/kafka-connect/jars
RUN mkdir -p /etc/kafka-connect/jdbc


# Add Snowflake connector4 jar
RUN curl -sSL "http://central.maven.org/maven2/com/snowflake/snowflake-kafka-connector/0.4.0/snowflake-kafka-connector-0.4.0.jar" -o /etc/kafka-connect/jars/snowflake-kafka-connector-0.4.0.jar


# Add Snowflake connector5 jar
# RUN curl -sSL "http://central.maven.org/maven2/com/snowflake/snowflake-kafka-connector/0.5.0/snowflake-kafka-connector-0.5.0.jar" -o /usr/share/java/plugins/snowflake-kafka-connector-0.5.0.jar
# copy custom connector for 5
# COPY snowflake-kafka-connector-0.5.0.jar /usr/share/java/plugins/


# Add Snowflake JDBC connector jar
RUN curl -sSL "https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.9.2/snowflake-jdbc-3.9.2.jar" -o /etc/kafka-connect/jdbc/snowflake-jdbc-connector-3.9.2.jar


# copy the properties file
# COPY datagen-users.json /tmp/
COPY snowflake-connector-kafkapoc.json /tmp


# datagen config
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components,/etc/kafka-connect/jars"
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:0.1.0
