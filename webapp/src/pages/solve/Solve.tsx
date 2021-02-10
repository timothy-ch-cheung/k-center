import React, {useState} from "react";
import Chart, {ChartData} from "../../components/chart/Chart";
import {Container, HomeIcon} from "../index/App";
import styled from '@emotion/styled';
import {IconButton} from "@material-ui/core";
import {useHistory} from "react-router-dom";
import ConfigPanel, {SolveRequestData} from "../../components/configuration/ConfigPanel";
import InstanceStats from "../../components/stats/optimal/InstanceStats";
import SolutionStats from "../../components/stats/solution/SolutionStats";
import CloseableAlert from "../../components/alert/ClosableAlert";


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

export interface AlertData {
    message: string
    type: string
}

function Solve() {
    const history = useHistory();
    const [alertOpen, setAlertOpen] = useState<boolean>(false)
    const [alertData, setAlertData] = useState<AlertData>({message: "", type: "none"})
    const [chartData, setChartData] = useState<ChartData>()
    const [solveRequestData, setSolveRequestData] = useState<SolveRequestData>()

    const handleBackButtonClick = () => {
        history.push('/')
    }

    const onCloseAlert = () => {
        setAlertOpen(false)
    }

    const openAlert = (data: AlertData) => {
        setAlertOpen(true)
        setAlertData(data)
    }

    return <Container>
        <CloseableAlert open={alertOpen} onClose={onCloseAlert} alertData={alertData}/>
        <div>
            <IconButton aria-label="back" onClick={handleBackButtonClick}>
                <HomeIcon fontSize="large"/>
            </IconButton>
        </div>
        <ChartContainer>
            <ConfigPanel
                gridArea="left" width={350} height={455}
                chartData={chartData}
                setChartData={setChartData}
                setSolveRequestData={setSolveRequestData}
                alertOpen={openAlert}
            />
            <Chart gridArea="middle" data={chartData?.data} width={350} height={350}
                   solution={chartData?.solutions ? chartData?.solutions[0] : undefined}/>
            <InstanceStats gridArea="top-right" chart={chartData} width={180} height={210}/>
            <SolutionStats
                gridArea="bot-right" width={180} height={200}
                solution={chartData?.solutions?.length == 1 ? chartData?.solutions[0] : undefined}
                solveRequestData={solveRequestData}
            />
        </ChartContainer>
    </Container>
}

export default Solve;