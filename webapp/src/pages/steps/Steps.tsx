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
import Step, {PageSetting, UpdatePageControl} from "../../components/step/Step";
import {algorithms} from "../../constants/algorithms";
import PopulationChart from "../../population_chart/PopulationChart";
import {View} from "../../components/view_panel/ViewPanel";

interface Step {
    active: boolean
    label: string
}

export interface SolutionStep extends ChartData {
    step?: Step
    active?: boolean
    subSolve?: boolean
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

const DEFAULT_STEP_PAGE_SETTINGS = {
    prevEnabled: false,
    nextEnabled: true,
    currentPage: 0,
    maxPage: -1
}


export default function Steps() {
    const history = useHistory();
    const [id, setId] = useState<string>(uuid());
    const [solutionHistory, setSolutionHistory] = useState<SolutionStep[]>([])
    const [solveRequestData, setSolveRequestData] = useState<StepSolveRequestData>()
    const [chartData, setChartData] = useState<SolutionStep>()
    const [pageSetting, setPageSetting] = useState<PageSetting>(DEFAULT_STEP_PAGE_SETTINGS)
    const [chartView, setChartView] = useState<View>(View.Population)
    const [isInspect, setIsInspect] = useState<boolean>(false)
    const [isInitialMoveMade, setIsInitialMoveMade] = useState<boolean>(false)
    const [isActive, setIsActive] = useState<boolean>(true)

    const updatePageControl = (update: UpdatePageControl) => {
        setPageSetting({...pageSetting, ...update})
    }

    const resetPageControl = () => {
        setPageSetting(DEFAULT_STEP_PAGE_SETTINGS)
        setSolutionHistory([])
        setChartView(View.Population)
        setIsInspect(false)
        setIsInitialMoveMade(false)
        setIsActive(true)
    }

    const handleBackButtonClick = () => {
        history.push('/')
    }

    const updateSolutionHistory = (solution: SolutionStep) => {
        setSolutionHistory(solutionHistory.concat(solution))
    }

    const renderGraphVisualisation = () => {
        const isGenetic = solveRequestData?.algorithm && algorithms[solveRequestData.algorithm].type == "genetic"
        if (!isGenetic) {
            return <Chart gridArea="middle" data={chartData?.data} width={350} height={350}
                          solution={chartData?.solutions ? chartData?.solutions[0] : undefined}/>
        } else {
            return <PopulationChart gridArea="middle" data={chartData?.data} width={360} height={350}
                                    solutions={chartData?.solutions} chartView={chartView} setChartView={setChartView}/>
        }
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
                resetSteps={resetPageControl}
            />
            <InstanceStats gridArea="mid-left" chart={chartData} width={190} height={165}/>
            <Parameters gridArea="bot-left" solveRequestData={solveRequestData} width={190} height={130}/>
            {renderGraphVisualisation()}
            <Step gridArea="right"
                  width={320} height={455}
                  solutionHistory={solutionHistory}
                  updateSolutionHistory={updateSolutionHistory}
                  setChartData={setChartData}
                  text={chartData?.step?.label}
                  id={id}
                  algorithm={solveRequestData?.algorithm}
                  pageControl={Object.assign(pageSetting, {updateControl: updatePageControl})}
                  isInspect={isInspect}
                  setIsInspect={setIsInspect}
                  isInitialMoveMade={isInitialMoveMade}
                  setIsInitialMoveMade={setIsInitialMoveMade}
                  isActive={isActive}
                  setIsActive={setIsActive}
            />
        </ChartContainer>
    </Container>
}