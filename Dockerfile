
#
# matterhorn Dockerfile
#
 
# Pull base image.
FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive 

RUN apt-get update

# install deps
RUN apt-get install -y wget git build-essential openjdk-7-jdk maven2 gstreamer0.10-plugins-base gstreamer0.10-plugins-good libglib2.0-dev

RUN useradd -m -d /opt/matterhorn -r matterhorn
USER matterhorn
WORKDIR /opt/matterhorn

RUN wget http://bitbucket.org/opencast-community/matterhorn/get/1.4.4.tar.gz
RUN tar zxvf 1.4.4.tar.gz
RUN mv opencast-community-matterhorn-* 1.4.4
RUN ln -s 1.4.4 felix

WORKDIR /opt/matterhorn/felix
RUN MAVEN_OPTS='-Xms256m -Xmx960m -XX:PermSize=64m -XX:MaxPermSize=256m' mvn clean install -DdeployTo=/opt/matterhorn/1.4.4

EXPOSE 8080 

ENV M2_REPO /opt/matterhorn/.m2/repository
ENV FELIX_HOME /opt/matterhorn/1.4.4
ENV JAVA_OPTS -Xms1024m -Xmx1024m -XX:MaxPermSize=256m

CMD /opt/matterhorn/1.4.4/bin/start_matterhorn.sh
