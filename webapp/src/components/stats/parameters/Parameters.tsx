import React from "react";
import {SolveRequestData} from "../../configuration/ConfigPanel";
import {ChartFrame} from "../../chart/Chart";
import {H3, SectionDivider} from "../../configuration/Layout";
import {P} from "../Layout";


interface Props {
    solveRequestData?: SolveRequestData
    width: number
    height: number
    gridArea: string
}

export default function (props: Props) {
    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Parameters</H3>
        <SectionDivider/>
        <P>K: {props.solveRequestData?.k}</P>
        <P>Min blue: {props.solveRequestData?.blue}</P>
        <P>Min red: {props.solveRequestData?.red}</P>
    </ChartFrame>
}