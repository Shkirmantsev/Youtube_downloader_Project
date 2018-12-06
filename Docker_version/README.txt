На основе ubuntu18.06.

проекта в GitHub (с файлом «env.list», вам нужно выполнить шаг 2): 
https://github.com/Shkirmantsev/Youtube_downloader.git

step1 в терминале:

#: xhost +

step2 в терминале (в рабочем каталоге):

#: docker run --name = youtubedownloader --net = host -it --env-file ./env.list -v "$ HOME / .Xauthority: /root/.Xauthority: rw" -v "$ PWD / tmp_download : / loader / tmp_download: rw "-v" $ PWD: / loader / my_computer: rw "shkirmantsev / youtubedownloader