import React from "react";
import Chart from "../../components/chart/Chart";
import {Container} from "../index/App";
import styled from '@emotion/styled';
import Home from '@material-ui/icons/Home';
import {IconButton} from "@material-ui/core";
import {useHistory} from "react-router-dom";
import Configurator from "../../components/configuration/Configurator";

const HomeIcon = styled(Home)`
    color: white;
`

const ChartContainer = styled("div")`
    display: flex;
    justify-content: center;
`

const chart =
    {
        data: [
            {
                colour: "blue",
                y: 2.6,
                x: 1.3,
                center: true
            },
            {
                colour: "blue",
                y: 2.1,
                x: 1.2
            },
            {
                colour: "blue",
                y: 2.3,
                x: 0.5
            },
            {
                colour: "red",
                y: 5.2,
                x: 5.9
            },
            {
                colour: "red",
                y: 4.7,
                x: 6.4,
                center: true
            }
        ],
        centerRadius: 0.854
    };

function Solve() {
    const history = useHistory();

    const handleBackButtonClick = () => {
        history.push('/')
    }

    return <Container>
        <div>
            <IconButton aria-label="back" onClick={handleBackButtonClick}>
                <HomeIcon fontSize="large"/>
            </IconButton>
        </div>
        <ChartContainer>
            <Configurator width={350} height={455}/>
            <Chart chart={chart} width={350} height={350}/>
        </ChartContainer>
    </Container>
}

export default Solve;