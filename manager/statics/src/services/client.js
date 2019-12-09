import axios from 'axios';
import Qs from 'qs';
import Hs from 'humps';

const baseURL = 'http://localhost:5000';
const client = axios.create({
  baseURL,
  transformRequest: [(data) => Hs.decamelizeKeys(data), ...axios.defaults.transformRequest],
  transformResponse: [...axios.defaults.transformResponse, (data) => Hs.camelizeKeys(data)],
  paramsSerializer: (params) => Qs.stringify(Hs.decamelizeKeys(params), { arrayFormat: 'brackets' }),
});

export { client };
