// This file is automatically compiled by Webpack, along with any other files
// present in this directory. You're encouraged to place your actual application logic in
// a relevant structure within app/webpack and only use these pack files to reference
// that code so it'll be compiled.

import 'unpoly/dist/unpoly'

let webpackContext = require.context('../javascript/blocks', true, /\.js$/)
for(let key of webpackContext.keys()) { webpackContext(key) }


import 'bootstrap/scss/bootstrap.scss'

import '../stylesheets/application.sass'

require.context('../stylesheets/blocks', true, /\.sass$/)
