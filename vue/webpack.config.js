const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')
module.exports = {
  entry: './src/index.js',
  mode:'development',
  output: {
    filename: 'main.js',
    path: "/usr/local/var/www/assets"
  },
  module: {
    rules: [
      { test: /\.js$/, use: 'babel-loader' },
      { test: /\.vue$/, use: 'vue-loader' },
      {test: /\.css$/,use: ['vue-style-loader','css-loader']
}
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
  ]
};
