const webpack = require('webpack');
const path = require('path');

const config = {
  entry: __dirname + '/src/index.js',
  output: {
    path: __dirname + '/dist',
    filename: 'bundle.js',
  },
  resolve: {
    extensions: ['.js', '.jsx', '.css'],
    alias: {
      components: path.resolve(__dirname, 'src/components/'),
      helpers: path.resolve(__dirname, 'src/helpers/'),
      screens: path.resolve(__dirname, 'src/screens/'),
      services: path.resolve(__dirname, 'src/services/'),
    },
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
      {
        test: /\.s[ac]ss$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
    ],
  },
};

module.exports = config;
