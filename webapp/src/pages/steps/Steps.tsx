import React, {useState} from "react";
import {Container, HomeIcon} from "../index/App";
import {v4 as uuid} from 'uuid';
import Chart, {ChartData} from "../../components/chart/Chart";
import styled from "@emotion/styled";
import ConfigModal, {StepSolveRequestData} from "../../components/configuration/ConfigModal";
import InstanceStats from "../../components/stats/optimal/InstanceStats";
import {IconButton} from "@material-ui/core";
import {useHistory} from "react-router-dom";
import Parameters from "../../components/stats/parameters/Parameters";
import Step from "../../components/step/Step";

interface Props {

}

interface Step {
    active: boolean
    label: string
}

export interface SolutionStep extends ChartData {
    step?: Step
}

const ChartContainer = styled("div")`
    display: grid;
    grid-template-rows: 115px 200px 175px;
    grid-template-columns: 240px 580px 260px;
    grid-gap: 5px;
    margin: 30px auto;
    width: 1250px;
    grid-template-areas:
    "top-left middle right"
    "mid-left middle right"
    "bot-left middle right";
`


export default function Steps(props: Props) {
    const history = useHistory();
    const [id, setId] = useState<string>(uuid());
    const [solutionHistory, setSolutionHistory] = useState<SolutionStep[]>([])
    const [solveRequestData, setSolveRequestData] = useState<StepSolveRequestData>()
    const [chartData, setChartData] = useState<SolutionStep>()

    const handleBackButtonClick = () => {
        history.push('/')
    }

    const updateSolutionHistory = (solution: SolutionStep) => {
        setSolutionHistory(solutionHistory.concat(solution))
    }

    return <Container>
        <div>
            <IconButton aria-label="back" onClick={handleBackButtonClick}>
                <HomeIcon fontSize="large"/>
            </IconButton>
        </div>
        <ChartContainer>
            <ConfigModal
                gridArea="top-left"
                width={190} height={80}
                chartData={chartData}
                setChartData={setChartData}
                setStepSolveRequestData={setSolveRequestData}
                id={id}
            />
            <InstanceStats gridArea="mid-left" chart={chartData} width={190} height={165}/>
            <Parameters gridArea="bot-left" solveRequestData={solveRequestData} width={190} height={130}/>
            <Chart gridArea="middle" chart={chartData} width={350} height={350}/>
            <Step gridArea="right"
                  width={260} height={455}
                  solutionHistory={solutionHistory}
                  updateSolutionHistory={updateSolutionHistory}
                  setChartData={setChartData}
                  text={chartData?.step?.label}
                  id={id}
            />
        </ChartContainer>
    </Container>
}