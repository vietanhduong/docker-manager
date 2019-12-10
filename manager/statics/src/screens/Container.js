import React from 'react';
import { withRouter } from 'react-router-dom';
import { browserHistory } from 'helpers/history';

const Container = (props) => {
  console.log(props);
  return <div>Container</div>;
};

export default withRouter(Container);
