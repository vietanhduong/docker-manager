import React, { Fragment, useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { containerService } from 'services/container';
import { MenuList, MenuItem, Button, Grow, IconButton } from '@material-ui/core';
import SettingsBackupRestoreOutlinedIcon from '@material-ui/icons/SettingsBackupRestoreOutlined';
import PauseCircleOutlineOutlinedIcon from '@material-ui/icons/PauseCircleOutlineOutlined';
import HighlightOffOutlinedIcon from '@material-ui/icons/HighlightOffOutlined';

const Menu = () => {
  const [containers, setContainers] = useState([]);
  const [isShow, setIsShow] = useState(0);

  useEffect(() => {
    containerService.getContainers().then((response) => {
      const { data } = response;
      setContainers(data.map((item) => ({ ...item, id: item.id.slice(0, 12) })));
    });
  }, []);

  return (
    <MenuList className='app-menu'>
      {containers.map((item) => (
        <Link to={`/${item.id}`} key={item.id}>
          <MenuItem>
            <div>{item.name}</div>
            <div className='menu-item-icons'>
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
        </Link>
      ))}
    </MenuList>
  );
};

export default Menu;
