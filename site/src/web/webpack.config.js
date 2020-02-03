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
        path: path.join(process.env.VAR_DIR, 'static')
    },
    resolveLoader: {
        modules: [process.env.UI_NODE_MODULES_DIR],
    },
    resolve: {
        modules: [
            '.',
            process.env.UI_NODE_MODULES_DIR,
        ],
        extensions: ['.ts', '.js', '.scss', '.css']
    },
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.tsx?$/i,
                use: {
                    loader: 'ts-loader',
                    options: {
                        onlyCompileBundledFiles: true,
                        compilerOptions: {
                            "outDir": process.env.WEBPACK_OUTPUT_DIR,
                            "target": "ES6",
                            "moduleResolution": "node",
                            "sourceMap": true,
                            "allowJs": true,
                            "baseUrl": ".",
                            "typeRoots": [
                                path.join(process.env.UI_NODE_MODULES_DIR, "@types"),
                                path.join(process.env.TEST_NODE_MODULES_DIR, "@types"),
                            ],
                            "paths": {
                                "*": [
                                    "*",
                                    path.join(process.env.UI_NODE_MODULES_DIR, "*"),
                                    path.join(process.env.TEST_NODE_MODULES_DIR, "*"),
                                ]
                            }
                        }
                    }
                }

            },
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
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
