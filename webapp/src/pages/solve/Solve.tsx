import React, {useState} from "react";
import Chart, {ChartData} from "../../components/chart/Chart";
import {Container} from "../index/App";
import styled from '@emotion/styled';
import Home from '@material-ui/icons/Home';
import {IconButton} from "@material-ui/core";
import {useHistory} from "react-router-dom";
import Configurator from "../../components/configuration/Configurator";
import InstanceStats from "../../components/stats/optimal/InstanceStats";

const HomeIcon = styled(Home)`
    color: white;
`

const ChartContainer = styled("div")`
    display: grid;
    grid-template-rows: 495px 150px;
    grid-template-columns: 405px 580px;
    grid-gap: 5px;
    
    grid-template-areas:
    "left middle top-right"
    "left middle bot-right";
    margin: 30px auto;
`

function Solve() {
    const history = useHistory();
    const [chartData, setChartData] = useState<ChartData>()

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
            <Configurator className="left" width={350} height={455} chartData={chartData} setChartData={setChartData}/>
            <Chart className="middle" chart={chartData} width={350} height={350}/>
            <InstanceStats chart={chartData} width={180} height={200}/>
        </ChartContainer>
    </Container>
}

export default Solve;