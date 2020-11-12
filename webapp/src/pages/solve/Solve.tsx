import React, {useState} from "react";
import Chart, {ChartData} from "../../components/chart/Chart";
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
            <Configurator width={350} height={455} setChartData={setChartData}/>
            <Chart chart={chartData} width={350} height={350}/>
        </ChartContainer>
    </Container>
}

export default Solve;