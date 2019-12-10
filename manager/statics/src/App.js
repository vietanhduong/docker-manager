import React from 'react';
import { Router, Route, Switch } from 'react-router-dom';
import { browserHistory } from 'helpers/history';
import Layout from 'components/Layout';
import Menu from 'components/Menu';
import './App.scss';
import './Custom.scss';

const App = () => {
  return (
    <Router history={browserHistory}>
      <Switch>
        <Route path='/' component={Layout} />
      </Switch>
    </Router>
  );
};

export default App;
