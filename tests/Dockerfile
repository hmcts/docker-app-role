FROM centos/systemd

ENV DOCKER_VERSION 1.13.0
ENV DOCKER_COMPOSE_VERSION 1.10.1

# Install EPEL repository and basic tools
RUN yum -y update; yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all

# Mount additional resource controllers at launch time
RUN yum -y install libcgroup-tools; yum clean all; systemctl enable cgconfig.service
RUN echo 'mount {cpu = /sys/fs/cgroup/cpu;}' >> /etc/cgconfig.conf

# Install docker engine and docker compose tool
RUN yum-config-manager --add-repo https://docs.docker.com/engine/installation/linux/repo_files/centos/docker.repo
RUN yum -y install docker-engine-${DOCKER_VERSION}; yum clean all; systemctl enable docker.service
RUN pip --no-cache-dir install docker-compose==${DOCKER_COMPOSE_VERSION}

CMD ["/usr/sbin/init"]
