#上传文件:http://espeak.sourceforge.net/data/zh_listx.zip 到目录dictsource
apt-get install gcc
apt-get install make autoconf automake libtool pkg-config
tar -zxvf espeak-ng-1.50.tgz
cd espeak-ng
./autogen.sh
./configure --prefix=/usr --with-extdict-zh=yes
make LIBDIR=/usr/lib/x86_64-linux-gnu install

#test
espeak-ng -vcmn  "你好" -w tt.wav

