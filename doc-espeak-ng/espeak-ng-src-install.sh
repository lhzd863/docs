apt-get install gcc
apt-get install make autoconf automake libtool pkg-config
tar -zxvf espeak-ng-1.50.tgz
上传文件:http://espeak.sourceforge.net/data/zh_listx.zip 到目录dictsource
./autogen.sh
./configure --prefix=/usr --with-extdict-zh=yes
make LIBDIR=/usr/lib/x86_64-linux-gnu install
