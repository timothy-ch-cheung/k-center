import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './pages/index/App';
import {StylesProvider} from '@material-ui/core/styles';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Solve from "./pages/solve/Solve";

ReactDOM.render(
    <React.StrictMode>
        <StylesProvider injectFirst>
            <Router>
                <Switch>
                    <Route exact path='/' component={App}/>
                    <Route exact path='/solve' component={Solve}/>
                </Switch>
            </Router>
        </StylesProvider>
    </React.StrictMode>,
    document.getElementById('root')
);
