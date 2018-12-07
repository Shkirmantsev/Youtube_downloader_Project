Based on ubuntu18.06.

project in GitHub (with "env.list" file, you need for step 2): 
https://github.com/Shkirmantsev/Youtube_downloader.git

step1 in terminal:

#:xhost +

step2 in terminal (in workdirectory):

#:docker run --name = youtubedownloader --net=host -it --env-file ./env.list -v "$HOME/.Xauthority:/root/.Xauthority:rw" -v "$PWD/tmp_download:/loader/tmp_download:rw" -v" $PWD:/loader/my_computer:rw "shkirmantsev/youtubedownloader
