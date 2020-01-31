FROM confluentinc/cp-kafka-connect:5.3.1

# Create plugin directory
RUN mkdir -p /etc/kafka-connect/jars
RUN mkdir -p /etc/kafka-connect/jdbc

# Add Snowflake connector4 jar
#RUN curl -sSL "http://central.maven.org/maven2/com/snowflake/snowflake-kafka-connector/0.4.0/snowflake-kafka-connector-0.4.0.jar" -o /tmp/snowflake-kafka-connector-0.4.0.jar
RUN wget -q -O /tmp/snowflake-kafka-connector-0.5.5.jar https://repo1.maven.org/maven2/com/snowflake/snowflake-kafka-connector/0.5.5/snowflake-kafka-connector-0.5.5.jar


# Add Snowflake connector5 jar
# RUN curl -sSL "http://central.maven.org/maven2/com/snowflake/snowflake-kafka-connector/0.5.0/snowflake-kafka-connector-0.5.0.jar" -o /usr/share/java/plugins/snowflake-kafka-connector-0.5.0.jar
# copy custom connector for 5
# COPY snowflake-kafka-connector-0.5.0.jar /usr/share/java/plugins/


# Add Snowflake JDBC connector jar
RUN curl -sSL "https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.9.2/snowflake-jdbc-3.9.2.jar" -o /tmp/snowflake-jdbc-connector-3.9.2.jar


# copy the properties file
# COPY datagen-users.json /tmp/
COPY snowflake-connector-kafkapoc.json /tmp


# datagen config
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components,/etc/kafka-connect/jars"
RUN /bin/cp -f /tmp/snowflake-kafka-connector-0.5.5.jar /etc/kafka-connect/jars && /bin/cp -f /tmp/snowflake-jdbc-connector-3.9.2.jar /etc/kafka-connect/jdbc && ls -alrt /etc/kafka-connect/jars > /tmp/chrisinfo &&  confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:0.1.0
