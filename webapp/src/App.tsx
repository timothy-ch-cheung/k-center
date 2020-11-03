import React from 'react';
import './App.css';
import Chart from "./components/Chart";

const data = [
    {
        colour: "BLUE",
        y: 2.6,
        x: 1.3,
        center: true
    },
    {
        colour: "BLUE",
        y: 2.1,
        x: 1.2
    },
    {
        colour: "BLUE",
        y: 2.3,
        x: 0.5
    },
    {
        colour: "RED",
        y: 5.2,
        x: 5.9
    },
    {
        colour: "RED",
        y: 4.7,
        x: 6.4,
        center: true
    }
];

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <p>
                    Colorful K-Center Clustering
                </p>
                <Chart chart={{data: data, centerRadius:0.854}} width={350} height={350}/>
            </header>
        </div>
    );
}

export default App;
