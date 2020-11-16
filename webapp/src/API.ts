import axios from 'axios';

let apiURL;
if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
    apiURL = "http://localhost:5000/api/v1"
} else {
    apiURL = `${window.location.hostname}:5000/api/v1`
}

const API = axios.create({
    baseURL: apiURL
});

export default API;