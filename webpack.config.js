const path = require('path');
const webpack = require('webpack');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
    entry: {
        "index":'./app/static/js/src/index.jsx'
    },
    output: {
        path: path.join(__dirname, '/app/static/js/dist'),
        filename: '[name].min.js'
    },
    module: {
        rules: [
            {
                test: /\.jsx$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets:['@babel/react']
                    }
                }
            }
        ]
    },
    plugins: [
        new webpack.DefinePlugin({
          'process.env.NODE_ENV': JSON.stringify('development')
        }),
        new UglifyJSPlugin({
            test: /\.js(\?.*)?$/i,
            sourceMap: true,
            cache: false    
        })
    ]
};