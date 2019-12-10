import { client } from 'services/client';

const api = '/api/containers';

export const containerService = {
  getContainers: () => client.get(`${api}`),
};
