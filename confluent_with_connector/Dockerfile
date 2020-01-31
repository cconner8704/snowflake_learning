FROM confluentinc/cp-kafka-connect:5.3.1

# Create plugin directory
RUN mkdir -p /kafka-connect/snowflake
RUN mkdir -p /kafka-connect/jdbc

# Add Snowflake connector4 jar
#RUN curl -sSL "http://central.maven.org/maven2/com/snowflake/snowflake-kafka-connector/0.4.0/snowflake-kafka-connector-0.4.0.jar" -o /tmp/snowflake-kafka-connector-0.4.0.jar
RUN wget -q -O /tmp/snowflake-kafka-connector-0.5.5.jar https://repo1.maven.org/maven2/com/snowflake/snowflake-kafka-connector/0.5.5/snowflake-kafka-connector-0.5.5.jar


# Add Snowflake JDBC connector jar
RUN curl -sSL "https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.9.2/snowflake-jdbc-3.9.2.jar" -o /tmp/snowflake-jdbc-connector-3.9.2.jar


# copy the properties file
# COPY datagen-users.json /tmp/
COPY snowflake-connector-kafkapoc.json /tmp


# datagen config
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"
#ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components,/kafka-connect/snowflake"
RUN /bin/cp -f /tmp/snowflake-kafka-connector-0.5.5.jar /etc/kafka-connect/snowflake && /bin/cp -f /tmp/snowflake-jdbc-connector-3.9.2.jar /kafka-connect/jdbc && ls -alrt /kafka-connect/snowflake > /tmp/chrisinfo &&  confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:0.1.0
