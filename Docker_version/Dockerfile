FROM ubuntu
MAINTAINER DMITRY SHKIRMANTSEV <Shkirmantsev@gmail.com>
ARG LC_ALL
ARG USER
ENV USER=${USER}
RUN apt-get update &&\ 
apt-get install ffmpeg xclip ca-certificates -y &&\
apt-get autoremove -y &&\
apt-get clean -y &&\
rm -rf /var/lib/apt/list/*
#apt-get install python3-pip -y pip3 install pyinstaller && pip3 install --uprade pyinstaller &&\
#apt-get install unicode
#apt-get autoremove -y &&\
# apt-get install ttf-ancient-fonts
RUN export lang=UTF_8
ARG LANG=C.UTF-8
ENV LANG=${LANG}
RUN mkdir /loader &&\
mkdir /loader/tmp_download
WORKDIR /loader
COPY Py_loader_executable_for_LINUX/ .
ENV LANG C.UTF-8
ARG USER
ENV USER=${USER}
ARG DISPLAY
ENV DISPLAY=${DISPLAY}
#ENTRYPOINT [ "/bin/bash" ]
ENTRYPOINT ["./GUI_Download_Start"]