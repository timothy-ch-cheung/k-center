import React from 'react';
import {ChartData, ChartFrame, GraphPlaceHolder} from "../../chart/Chart";
import {H3, HorizontalGroup, SectionDivider} from "../../configuration/Configurator";
import {IconButton, Tooltip} from "@material-ui/core";
import InfoIcon from '@material-ui/icons/Info'
import styled from "@emotion/styled";

interface Props {
    chart?: ChartData
    width: number
    height: number
    gridArea: string
}

interface DataProps {
    chart?: ChartData
}

const IconBtn = styled(IconButton)`
    height: 24px;
    padding: 0px;
`

const ToolTipLine = styled("p")`
    font-size: 13px;
    margin: 5px;
`

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
    return <ChartFrame width={props.width} height={props.height}>
        <H3>Problem Details</H3>
        <SectionDivider/>
        {!props.chart && <GraphPlaceHolder>N/A</GraphPlaceHolder>}
        {props.chart && <>
            <p>Nodes: {props.chart.nodes}</p>
            <p>Blue nodes: {props.chart.blue}</p>
            <p>Red nodes: {props.chart.red}</p>
            <HorizontalGroup>
                <p style={{marginTop: "0px"}}>optimal cost: {props.chart.optimalSolution.radius}</p>
                <Tooltip title={<OptimalStats chart={props.chart}/>}>
                    <IconBtn aria-label="back">
                        <InfoIcon/>
                    </IconBtn>
                </Tooltip>
            </HorizontalGroup>

        </>}
    </ChartFrame>
}