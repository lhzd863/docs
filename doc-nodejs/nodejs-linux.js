#
wget https://nodejs.org/dist/v12.8.0/node-v12.8.0-linux-x64.tar.xz
xz -d node-v12.8.0-linux-x64.tar.xz
mv node-v12.8.0-linux-x64 nodejs
mv nodejs /usr/local/
ln -s /usr/local/nodejs/bin/node /usr/local/bin
ln -s /usr/local/nodejs/bin/npm /usr/local/bin
