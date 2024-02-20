FROM ubuntu:20.04
WORKDIR /gita-middleware-sensors

COPY ./commands ./commands
COPY ./commands/controle.conf /

#define os arquivos da pasta "commands" como executaveis e adiciona a pasta so PATH
RUN chmod -R a+x /gita-middleware-sensors/commands && \
    echo "export PATH=$PATH:/gita-middleware-sensors/commands" >> /etc/profile

#define o timeZone
RUN ln -snf /usr/share/zoneinfo/$(curl https://ipapi.co/timezone) /etc/localtime

#instala dependencias da aplicacao
RUN apt-get update && apt-get install -y \
    tzdata \
    curl \
    ifupdown \
    iproute2 \
    iptables \
    iputils-ping \
    net-tools \
    openvswitch-switch \
    openvswitch-testcontroller \
    tcpdump \
    x11-xserver-utils \
    systemd \
    xterm \
    mosquitto-clients \
    mininet \
    dnsutils \
    netcat \
    python3-pip

