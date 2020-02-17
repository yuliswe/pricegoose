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
        path: process.env.STATIC_FILES_DIR
    },
    resolveLoader: {
        modules: [process.env.UI_NODE_MODULES_DIR],
    },
    resolve: {
        modules: [
            '.',
            process.env.UI_NODE_MODULES_DIR,
        ],
        extensions: ['.ts', '.js']
    },
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.tsx?$/i,
                use: {
                    loader: 'ts-loader',
                    options: {
                        configFile: 'tsconfig.webpack.json',
                        onlyCompileBundledFiles: true,
                        compilerOptions: {
                            "target": "ES6",
                            "moduleResolution": "node",
                            "sourceMap": true,
                            "allowJs": true,
                            "baseUrl": ".",
                            "outDir": process.env.STATIC_FILES_DIR,
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
                test: /\.(woff(2)?|ttf|eot|svg|gif|jpg|png)(\?v=\d+\.\d+\.\d+)?$/,
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
    }
}
