import axios from 'axios';
import Qs from 'qs';
import Hs from 'humps';

const baseURL = 'http://35.247.190.151:8991';
const client = axios.create({
  baseURL,
  transformRequest: [(data) => Hs.decamelizeKeys(data), ...axios.defaults.transformRequest],
  transformResponse: [...axios.defaults.transformResponse, (data) => Hs.camelizeKeys(data)],
  paramsSerializer: (params) => Qs.stringify(Hs.decamelizeKeys(params), { arrayFormat: 'brackets' }),
});

export { client };
