import React, {useEffect} from 'react';
import d3Chart from './D3Chart'
import styled from '@emotion/styled'
import {ChartItem} from "./ChartInterfaces";

interface FrameProps {
    width: number,
    height: number
}

export const ChartFrame = styled("div")`
  background-color: white;
  margin: 5px;
  padding: 15px;
  padding-right: 30px;
  border-radius: 15px;
  border: 2px solid green;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  width: ${(props: FrameProps) => props.width}px;
  height: ${(props: FrameProps) => props.height}px;
  overflow: hidden;
`

export const ChartSvg = styled("svg")`
  color: black;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
`

const ToolTip = styled("div")`
  background-color: rgba(105, 105, 105, 0.85);
  border-radius: 5px;
  height: 18px;
  opacity: 0;
  pointer-events: none;
  position: absolute;
  text-align: center;
  font-size: 16px;
  padding: 5px;
`

export const GraphPlaceHolder = styled("h3")`
  color: grey;
  text-align: center;
`

export interface OptimalSolution {
    k: number
    minBlue: number
    minRed: number
    radius: number
    outliers: number
}

interface Coordinate {
    x: number
    y: number
}

export interface Solution {
    k: number
    timeTaken: number
    radius: number
    outliers: number
    centers: Coordinate
}


export interface ChartData {
    data: ChartItem[]
    nodes: number
    blue: number
    red: number
    optimalSolution: OptimalSolution
    solutions?: Solution[]
}

interface Props {
    data?: ChartItem[]
    width: number
    height: number
    gridArea?: string
    solution?: Solution
}

export default function Chart(props: Props): JSX.Element {
    let initialised = false
    const initialise = () => {
        props.data && d3Chart.create({
            width: props.width,
            height: props.height,
            data: props.data,
            solution: props.solution
        });
        initialised = true
    }

    useEffect(() => {
        initialise()
    }, [])

    useEffect(() => {
        if (!initialised) {
            initialise()
        }

        props.data && d3Chart.update({
            width: props.width,
            height: props.height,
            data: props.data,
            solution: props.solution
        });
    }, [props, props.data])

    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width * 1.5} height={props.height * 1.3}>
        <ChartSvg className={"chart"}/>
        {!props.data && <GraphPlaceHolder>Choose a problem instance</GraphPlaceHolder>}
        <ToolTip className="tooltip"/>
    </ChartFrame>
}