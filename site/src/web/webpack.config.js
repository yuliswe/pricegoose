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
    path: '/root/var/static/webpack'
  },
  resolveLoader: {
    modules: [ '/root/var/node_modules' ],
  },
  resolve: {
    modules: [
      '.',
      '/root/var/node_modules',
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
              publicPath: 'static/webpack/assets',
            }
          }
        ]
      }
    ],
  },
  plugins: [
  ]
}
