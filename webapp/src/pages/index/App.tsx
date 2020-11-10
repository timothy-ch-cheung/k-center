import React from 'react';
import './App.css';
import styled from '@emotion/styled';
import Button from '@material-ui/core/Button';
import {useHistory} from "react-router-dom";

const Heading = styled("h1")`
    text-align: center;
`

const PaddedButton = styled(Button)`
    margin: 5px;
`

export const Container = styled("div")`
    background-color: #282c34;
    display: flex;
    justify-content: flex-start;
    align-items: stretch;
    flex-direction: column;
    height: 100vh;
`

function App() {
    const history = useHistory();

    const handleSolveButtonClick = () => {
        history.push('/solve')
    }

    return (
        <Container>
            <header className="App-header">
                <Heading>Colorful K-Center Clustering </Heading>
                <PaddedButton
                    variant="contained"
                    color="primary"
                    size="large"
                    onClick={handleSolveButtonClick}>
                    Solve a graph
                </PaddedButton>
                <PaddedButton
                    variant="contained"
                    size="large">
                    Visualise steps to a solution
                </PaddedButton>
            </header>
        </Container>
    );
}

export default App;
