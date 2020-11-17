import React from 'react';
import {ChartData, ChartFrame, GraphPlaceHolder} from "../../chart/Chart";
import TextWithTooltip, {ToolTipLine} from "../../text_with_tooltip/TextWithTooltip";
import {H3, SectionDivider} from "../../configuration/Layout";

interface Props {
    chart?: ChartData
    width: number
    height: number
    gridArea: string
}

interface DataProps {
    chart?: ChartData
}


function OptimalStats(props: DataProps) {
    return <div>
        <ToolTipLine>Optimal radius with constraints:</ToolTipLine>
        <ToolTipLine>k: {props.chart?.optimalSolution.k}</ToolTipLine>
        <ToolTipLine>min blue: {props.chart?.optimalSolution.minRed}</ToolTipLine>
        <ToolTipLine>min red: {props.chart?.optimalSolution.minRed}</ToolTipLine>
        <ToolTipLine>
            which
            leaves {props.chart?.optimalSolution.outliers} {props.chart?.optimalSolution.outliers == 1 ? "outlier" : "outliers"}
        </ToolTipLine>
    </div>
}


export default function InstanceStats(props: Props): JSX.Element {
    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Problem Details</H3>
        <SectionDivider/>
        {!props.chart && <GraphPlaceHolder>N/A</GraphPlaceHolder>}
        {props.chart && <>
            <p>Nodes: {props.chart.nodes}</p>
            <p>Blue nodes: {props.chart.blue}</p>
            <p>Red nodes: {props.chart.red}</p>
            <TextWithTooltip
                text={`optimal cost: ${props.chart.optimalSolution.radius}`}
                tooltipText={<OptimalStats chart={props.chart}/>}
            />

        </>}
    </ChartFrame>
}