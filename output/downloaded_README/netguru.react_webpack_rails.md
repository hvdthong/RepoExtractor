# ReactWebpackRails
[![Travis CI](https://travis-ci.org/netguru/react_webpack_rails.svg?branch=master)](https://travis-ci.org/netguru/react_webpack_rails)

## !! DEPRECATED !!
Consider using [Webpacker](https://github.com/rails/webpacker) instead.

If you are looking for view helpers and/or redux integrations, see:
1) [react-rails](https://github.com/reactjs/react-rails) (currently using webpacker)
2) [react-on-rails](https://github.com/shakacode/react_on_rails) (migration to webpacker in progress, using forked version now)

----

#### Rails - Webpack setup with React integration.
This gem provides easy and convenient way to build modern JavaScript stack on top of Rails applications using [Webpack](http://webpack.github.io/) and [React](https://facebook.github.io/react/).

## Features
* [Install Generator](https://github.com/netguru/react_webpack_rails/blob/master/docs/install_generator.md) for quick [Webpack](http://webpack.github.io/) setup.
* Integrated [react-hot-loader](https://github.com/gaearon/react-hot-loader)
* ES6/7 support with [babeljs](https://babeljs.io/).
* Node.js based [server-side JavaScript execution](https://github.com/netguru/react_webpack_rails/blob/master/docs/server_side_rendering.md).
* [React](https://facebook.github.io/react/) integration with server prerender option.

### Plugins:
* [rwr-alt](https://github.com/netguru/rwr-alt) plugin that makes it possible to populate and share Alt stores between react component located in different parts of rails views.
* [rwr-redux](https://github.com/netguru/rwr-redux) allows to use redux state containers in a rails views.
* [rwr-react_router](https://github.com/netguru/rwr-react_router) react-router integration.
* [rwr-view_helpers](https://github.com/netguru/rwr-view_helpers) handy view helpers.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'react_webpack_rails'
```

Execute:

    $ bundle

Then run installation:

    $ rails g react_webpack_rails:install

*read more about [`install  generator`](https://github.com/netguru/react_webpack_rails/blob/master/docs/install_generator.md)*

### Babel

By default, `react-webpack-rails` uses Babel Stage 1 - Proposal. If you want to change the stage, you can do so in the `.babelrc` file. It is however not recommended to use Stage 0 in a production app, because the features present there can be dropped, which would break your application.

## Usage
##### Check [docs](https://github.com/netguru/react_webpack_rails/tree/master/docs) for detailed api description.
#### to use hot-reloading add partial in your application.html.erb to `<body>`:
(it's not needed when you want to use just webpack in watch mode without hot-reloading)
```erb
<%= render 'layouts/react_hot_assets' %>
```

#### Register component in index.js

```js
import Component from './components/some-component';
RWR.registerComponent('customComponentName', Component);
```

#### Use it in rails view

```erb
<%= react_component('customComponentName', { user: User.last }) %>
```

#### Use it in javascript file

```js
const element = $('#my-element');
RWR.renderComponent('customComponentName', {user_id: 1}, element);
```

#### Render component in controller

```ruby
def action_name
  render react_component: 'customComponentName', props: { user_id: 1 }
end
```

### Development environment
Run webpack in watch mode using script:

    $ npm start

Run webpack in hot-auto-reloading mode using script (to use it you have to add `react_hot_assets` partial as mentioned before):

    $ npm run start-hot-dev

If you are using server side render in components *(it's enabled by default in generated example)*, run node server:

    $ npm run rwr-node-dev-server

### Production environment
Run webpack in production mode before compiling assets using script:

    $ npm run build

If you are using server side render *(it's enabled by default in generated example)*, run node server:

    $ npm run rwr-node-server

#### Deployment
Check [docs/deployment.md](docs/deployment.md)

## Contributing

See the [contribution guide](https://github.com/netguru/react_webpack_rails/blob/master/CONTRIBUTING.md).

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
