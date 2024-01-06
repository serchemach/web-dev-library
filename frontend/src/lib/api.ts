import { createApiClient } from '../openapi_clients';

const API_BASE_PATH = "/"
const apiClient = createApiClient(API_BASE_PATH);
console.log("Exported");

export default apiClient;
