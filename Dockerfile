FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    socat \
    build-essential \
    python \
    python-pip

RUN pip install pwntools
RUN useradd -ms /bin/bash simulator
COPY --chown=simulator setup /opt/sim/setup
RUN chmod +x -R /opt/sim/setup

#RUN touch /home/simulator/flag
#RUN echo -n "FLAG{`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1`}" > /home/simulator/flag
#RUN chmod a-w /home/simulator/flag
#RUN chown simulator:simulator /home/simulator/flag
#ADD crontab /etc/cron.d/token-cron
#RUN chmod 0644 /etc/cron.d/token-cron
#RUN cron
