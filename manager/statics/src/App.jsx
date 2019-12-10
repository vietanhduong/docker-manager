import React, { Fragment, useEffect, useState } from 'react';
import { containerService } from './services/container';
import { MenuList, MenuItem, Button, Grow, IconButton } from '@material-ui/core';
import SettingsBackupRestoreOutlinedIcon from '@material-ui/icons/SettingsBackupRestoreOutlined';
import PauseCircleOutlineOutlinedIcon from '@material-ui/icons/PauseCircleOutlineOutlined';
import HighlightOffOutlinedIcon from '@material-ui/icons/HighlightOffOutlined';

import './App.scss';
import './Custom.scss';

const App = () => {
  console.log(123);
  const [containers, setContainers] = useState([]);
  const [isShow, setIsShow] = useState(0);

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
            <MenuItem key={item.id}>
              <div className='flex-1'>{item.name}</div>
              <div>
                <IconButton>
                  <SettingsBackupRestoreOutlinedIcon fontSize='small' color='error' />
                </IconButton>
                <IconButton>
                  <PauseCircleOutlineOutlinedIcon fontSize='small' color='primary' />
                </IconButton>
                <IconButton>
                  <HighlightOffOutlinedIcon fontSize='small' color='secondary' />
                </IconButton>
              </div>
            </MenuItem>
          ))}
        </MenuList>
      </div>
    </Fragment>
  );
};

export default App;
