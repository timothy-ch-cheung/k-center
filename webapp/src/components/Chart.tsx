import React, {useEffect, useRef} from 'react';
import d3Chart from './D3Chart'
import styled from '@emotion/styled'

const ChartFrame = styled("div")`
    background-color: white; 
    padding: 10px; 
    padding-right: 30px; 
    border-radius: 25px;
    border: 2px solid green;
`

const ChartSvg = styled("svg")`
    color: black;
    font-family: "Times New Roman", Times, serif;
    font-size: 20px;
`

const ToolTip = styled("div")`
    background-color: rgba(105,105,105, 0.8);
    border-radius: 5px;
    height: 18px;
    opacity: 0;
    pointer-events: none;
    position: absolute;
    text-align: center;
    font-size: 16px;
    padding: 5px;
`

interface ChartItem {
    colour: string,
    x: number,
    y: number,
    center?: boolean
}

interface ChartData {
    data: ChartItem[]
    centerRadius: number
}

interface Props {
    chart: ChartData
    width: number
    height: number
}

export default function Chart(props: Props): JSX.Element {
    useEffect(() => {
        d3Chart.create({
            width: props.width,
            height: props.height,
            chart: props.chart
        });
    }, [])

    useEffect(() => {
        d3Chart.update({
            width: props.width,
            height: props.height,
            chart: props.chart
        });
    }, [props])

    return <ChartFrame>
        <ChartSvg className="chart"/>
        <ToolTip className="tooltip"/>
    </ChartFrame>
}