import axios from 'axios';

let apiURL;
if (!process.env.NODE_ENV || process.env.NODE_ENV === 'development') {
    apiURL = "http://localhost:5000/api/v1"
} else if (/((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}/.test(window.location.hostname)) {
    apiURL = `${window.location.origin}/api/v1`
} else if (window.location.hostname === "localhost") {
    apiURL = `${window.location.origin}/api/v1`
} else {
    apiURL = `https://${window.location.hostname}/api/v1`
}

const API = axios.create({
    baseURL: apiURL
});

export default API;