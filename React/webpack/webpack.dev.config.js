var webpack = require('webpack');
var path = require('path');

var parentDirectory = path.join(__dirname, '../');

module.exports = {
    entry: [
        path.join(parentDirectory, 'index.js')
    ],
    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader'
        },{
            test: /\.css$/,
            loaders: ["style-loader", "css-loader", "less-loader"]
        }]
    },
    output: {
        path: parentDirectory + '/dist',
        filename: 'bundle.js'
    },
    devServer: {
        contentBase: parentDirectory,
        historyApiFallback: true
    }
}