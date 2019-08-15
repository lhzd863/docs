#
wget https://nodejs.org/dist/v12.8.0/node-v12.8.0-linux-x64.tar.xz
xz -d node-v12.8.0-linux-x64.tar.xz
mv node-v12.8.0-linux-x64 nodejs
mv nodejs /usr/local/
ln -s /usr/local/nodejs/bin/node /usr/local/bin
ln -s /usr/local/nodejs/bin/npm /usr/local/bin

#config
npm config set registry https://registry.npm.taobao.org --global
npm config set disturl https://npm.taobao.org/dist --global
#react install
--save-dev 表示在 package.json 文件的 devDependencies 节点下添加包的引用
--save 表示在 package.json 文件的 dependencies 节点下添加包的引用
npm install react react-dom --save-dev
npm install webpack webpack-dev-server --save-dev
#支持符合 ES6 规范的脚本文件（.js 或 .jsx）
npm install babel-core --save-dev
npm install babel-loader --save-dev
npm install babel-preset-es2015 --save-dev
npm install babel-preset-react --save-dev

