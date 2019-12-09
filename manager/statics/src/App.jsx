import React, { Fragment, useEffect, useState } from 'react';
import { containerService } from './services/container';
import { MenuList, MenuItem } from '@material-ui/core';
import './App.scss';

const App = () => {
  const [containers, setContainers] = useState([]);
  useEffect(() => {
    containerService.getContainers().then((response) => {
      const { data } = response;
      setContainers(data);
    });
  }, []);

  return (
    <Fragment>
      <div className='d-flex'>
        <MenuList className='app-menu'>
          {containers.map((item) => (
            <MenuItem key={item.id}>{item.name}</MenuItem>
          ))}
        </MenuList>
      </div>
    </Fragment>
  );
};

export default App;
