import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './pages/index/App';
import {StylesProvider} from '@material-ui/core/styles';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Solve from "./pages/solve/Solve";
import Steps from "./pages/steps/Steps";
import Learn from "./pages/k_center/Learn";

ReactDOM.render(
    <React.StrictMode>
        <StylesProvider injectFirst>
            <Router>
                <Switch>
                    <Route exact path='/' component={App}/>
                    <Route exact path='/solve' component={Solve}/>
                    <Route exact path='/steps' component={Steps}/>
                    <Route exact path='/learn' component={Learn}/>
                </Switch>
            </Router>
        </StylesProvider>
    </React.StrictMode>,
    document.getElementById('root')
);
