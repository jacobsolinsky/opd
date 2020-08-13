const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')
module.exports = {
  entry: './src/index.js',
  mode:'development',
  output: {
    filename: 'main.js',
    path: "/usr/local/var/www/assets",
    publicPath: "/assets/"
  },
  module: {
    rules: [
      { test: /\.js$/, use: {
        loader: 'babel-loader',
        options: {
          plugins: [
            "@babel/plugin-syntax-dynamic-import",
          ],
        },
        }
      },
      { test: /\.vue$/, use: 'vue-loader' },
      { test: /\.css$/,use: [
          'vue-style-loader', 'css-loader'
        ],
      },
      // AND `<style lang="scss">` blocks in `.vue` files
      {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader',
        ]
      },
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
  ]
};
