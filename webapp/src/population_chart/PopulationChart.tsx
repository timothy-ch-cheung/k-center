import {ChartItem} from "../components/chart/ChartInterfaces";
import Chart, {Solution} from "../components/chart/Chart";
import React, {useEffect, useState} from "react";
import ChartPreview from "../components/chart_preview/ChartPreview";
import styled from "@emotion/styled";
import {Dimensions} from "../interfaces";
import {GridList, GridListTile} from "@material-ui/core";
import ViewPanel, {View} from "../components/view_panel/ViewPanel";

interface Props {
    data?: ChartItem[]
    width: number
    height: number
    gridArea?: string
    solutions?: Solution[]
    chartView: View
    setChartView: (view: View) => void
}

const ChartFrame = styled("div")`
  background-color: white;
  margin: 5px;
  padding: 15px;
  border-radius: 15px;
  border: 2px solid green;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  width: ${(props: Dimensions) => props.width}px;
  height: ${(props: Dimensions) => props.height}px;
  overflow: hidden;
`

export default function PopulationChart(props: Props): JSX.Element {
    const [activeStep, setActiveStep] = useState<number>(0)

    const handleViewChange = (event: any, view: View) => {
        if (view !== null) {
            props.setChartView(view)
        }
    }

    const onNext = () => {
        setActiveStep(activeStep + 1)
    }

    const onBack = () => {
        setActiveStep(activeStep - 1)
    }

    const getFocusSolution = () => {
        if (props.solutions) {
            if (props.solutions.length === 1) {
                return props.solutions[0]
            } else {
                return props.solutions[activeStep]
            }
        }
        return undefined
    }

    useEffect(() => {
        if (props.solutions?.length === 1) {
            props.setChartView(View.Individual)
        } else {
            props.setChartView(View.Population)
        }
    }, props.solutions)


    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width * 1.5} height={props.height * 1.3}>
        {props.solutions && <ViewPanel
            view={props.chartView}
            changeView={handleViewChange}
            activeStep={activeStep}
            maxSteps={props.solutions.length}
            handleBack={onBack}
            handleNext={onNext}
            subSolve={props.solutions.length === 1}/>}

        {props.chartView === View.Population && <div style={{width: props.width * 1.2, margin: "auto"}}>
            <GridList cellHeight={"auto"} cols={3}>
                {props.solutions && props.solutions.map((solution, index) => {
                    return <GridListTile key={index} cols={1}>
                        <ChartPreview width={120} height={120} id={index} data={props.data} solution={solution}/>
                    </GridListTile>
                })}
            </GridList>
        </div>}
        {props.chartView === View.Individual &&
        <Chart gridArea="middle" data={props.data} width={320} height={295}
               solution={getFocusSolution()}/>
        }
    </ChartFrame>
}