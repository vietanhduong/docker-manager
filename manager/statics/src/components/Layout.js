import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Menu from 'components/Menu';
import Home from 'screens/Home';
import Container from 'screens/Container';

const Layout = () => {
  return (
    <div className='app-layout'>
      <Menu />
      <Switch>
        <Route exact path='/' component={Home} />
        <Route exact path='/:id' component={Container} />
      </Switch>
    </div>
  );
};

export default Layout;
