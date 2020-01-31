FROM confluentinc/cp-kafka-connect:5.3.1

ARG PLUGIN_BASE=/tmp/kafka-connect

# datagen config
#ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components,/kafka-connect/plugins"
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:0.1.0

# Create plugin directory
RUN mkdir -p $PLUGIN_BASE/jars
RUN mkdir -p $PLUGIN_BASE/jdbc

# Add Snowflake connector4 jar
RUN wget -q -O $PLUGIN_BASE/jars/snowflake-kafka-connector-0.5.5.jar https://repo1.maven.org/maven2/com/snowflake/snowflake-kafka-connector/0.5.5/snowflake-kafka-connector-0.5.5.jar

#Get bouncy
#RUN wget -q -O /tmp/bcprov-jdk15on-164.jar https://www.bouncycastle.org/download/bcprov-jdk15on-164.jar
#RUN wget -q -O /tmp/bcprov-ext-jdk15on-164.jar https://www.bouncycastle.org/download/bcprov-ext-jdk15on-164.jar
RUN wget -q -O $PLUGIN_BASE/jars/bc-fips-1.0.2.jar https://downloads.bouncycastle.org/fips-java/bc-fips-1.0.2.jar
RUN wget -q -O $PLUGIN_BASE/jars/bcpkix-jdk15on-164.jar https://www.bouncycastle.org/download/bcpkix-jdk15on-164.jar

# Add Snowflake JDBC connector jar
RUN curl -sSL "https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.9.2/snowflake-jdbc-3.9.2.jar" -o $PLUGIN_BASE/jdbc/snowflake-jdbc-connector-3.9.2.jar


# copy the properties file
# COPY datagen-users.json /tmp/
COPY snowflake-connector-kafkapoc.json /tmp
RUN ls -alrtR /etc/kafka-connect/ > /tmp/chrisinfo
