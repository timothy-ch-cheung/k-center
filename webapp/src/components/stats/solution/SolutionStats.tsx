import React from 'react';
import {ChartFrame, GraphPlaceHolder, Solution} from "../../chart/Chart";
import {SolveRequestData} from "../../configuration/ConfigPanel";
import TextWithTooltip, {ToolTipLine} from "../../text_with_tooltip/TextWithTooltip";
import {H3, SectionDivider} from "../../configuration/Layout";
import {P} from "../Layout";

interface Props {
    solution?: Solution
    solveRequestData?: SolveRequestData
    width: number
    height: number
    gridArea: string
}

interface CompareK {
    solutionK: number
    optimalK: number
}

const threeDecimalPlaces = new Intl.NumberFormat('en-GB', {
    minimumFractionDigits: 3,
    maximumFractionDigits: 3,
});

function SolutionK(props: CompareK) {
    const text = `k: ${Math.round(props.solutionK)}`
    if (props.optimalK === props.solutionK) {
        return <P>{text}</P>
    } else {
        return <TextWithTooltip
            tooltipText={<ToolTipLine>The solution has a different amount of centers than specified in config</ToolTipLine>}
            text={text}
            style={{color: "red"}}
        />
    }
}

export default function SolutionStats(props: Props): JSX.Element {
    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Solution Stats</H3>
        <SectionDivider/>
        {!props.solution?.radius && <GraphPlaceHolder>Graph Unsolved</GraphPlaceHolder>}
        {props.solution?.radius && props.solveRequestData?.k && <>
            <SolutionK solutionK={props.solution?.k} optimalK={props.solveRequestData.k}/>
            <P>Cost: {threeDecimalPlaces.format(props.solution?.radius)}</P>
            <P>Outliers: {Math.round(props.solution?.outliers)}</P>
            <P>Time Taken: {threeDecimalPlaces.format(props.solution?.timeTaken)}s</P>
        </>}
    </ChartFrame>
}