import React, {useState} from "react";
import Chart, {ChartData} from "../../components/chart/Chart";
import {Container} from "../index/App";
import styled from '@emotion/styled';
import Home from '@material-ui/icons/Home';
import {IconButton} from "@material-ui/core";
import {useHistory} from "react-router-dom";
import Configurator, {SolveRequestData} from "../../components/configuration/Configurator";
import InstanceStats from "../../components/stats/optimal/InstanceStats";
import SolutionStats from "../../components/stats/solution/SolutionStats";

const HomeIcon = styled(Home)`
    color: white;
`

const ChartContainer = styled("div")`
    display: grid;
    grid-template-rows: 250px 250px;
    grid-template-columns: 405px 580px 250px;
    grid-gap: 5px;
    margin: 30px auto;
    width: 1250px;
    grid-template-areas:
    "left middle top-right"
    "left middle bot-right";
`

function Solve() {
    const history = useHistory();
    const [chartData, setChartData] = useState<ChartData>()
    const [solveRequestData, setSolveRequestData] = useState<SolveRequestData>()

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
            <Configurator
                gridArea="left" width={350} height={455}
                chartData={chartData}
                setChartData={setChartData}
                setSolveRequestData={setSolveRequestData}
            />
            <Chart gridArea="middle" chart={chartData} width={350} height={350}/>
            <InstanceStats gridArea="top-right" chart={chartData} width={180} height={210}/>
            <SolutionStats
                gridArea="bot-right" width={180} height={200}
                solution={chartData?.solution}
                solveRequestData={solveRequestData}
            />
        </ChartContainer>
    </Container>
}

export default Solve;