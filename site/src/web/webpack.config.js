const path = require('path')

module.exports = {
  entry: {
    home: 'home/webpack.ts',
    lib: 'lib/index.ts',
  },
  devtool: 'inline-source-map',
  output: {
    library: 'app',
    libraryTarget: 'window',
    filename: '[name].js',
    path: '/root/var/static'
  },
  resolveLoader: {
    modules: [ process.env.UI_NODE_PATH ],
  },
  resolve: {
    modules: [
      '.',
      process.env.UI_NODE_PATH,
    ],
    extensions: [ '.ts', '.js', '.scss', '.css' ]
  },
  mode: 'development',
  watch: true,
  module: {
    rules: [
      {
        test: /\.tsx?$/i,
        use: 'ts-loader',
      },
      {
        test: /\.css$/i,
        use: [ 'style-loader', 'css-loader' ],
      },
      {
        test: /\.scss$/i,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader',
        ],
      },
      {
        test: /\.(woff(2)?|ttf|eot|svg|jpg|png|gif)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'assets',
              publicPath: 'static/assets',
            }
          }
        ]
      }
    ],
  },
  plugins: [
  ]
}
