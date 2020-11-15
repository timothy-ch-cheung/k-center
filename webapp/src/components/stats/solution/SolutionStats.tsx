import React from 'react';
import {ChartFrame, GraphPlaceHolder, Solution} from "../../chart/Chart";
import {H3, SectionDivider, SolveRequestData} from "../../configuration/Configurator";
import TextWithTooltip, {ToolTipLine} from "../../text_with_tooltip/TextWithTooltip";

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
        return <p>{text}</p>
    } else {
        return <TextWithTooltip
            tooltipText={<ToolTipLine>The solution has more centers than specified (pseudo solution)</ToolTipLine>}
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
            <p>Cost: {threeDecimalPlaces.format(props.solution?.radius)}</p>
            <p>Outliers: {Math.round(props.solution?.outliers)}</p>
            <p>Time Taken: {threeDecimalPlaces.format(props.solution?.timeTaken)}s</p>
        </>}
    </ChartFrame>
}