import React from 'react';
import {ChartFrame, GraphPlaceHolder, Solution} from "../../chart/Chart";
import {H3, SectionDivider} from "../../configuration/Configurator";

interface Props {
    solution?: Solution
    width: number
    height: number
    gridArea: string
}

const threeDecimalPlaces = new Intl.NumberFormat('en-GB', {
    minimumFractionDigits: 3,
    maximumFractionDigits: 3,
});

export default function SolutionStats(props: Props): JSX.Element {
    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Solution Stats</H3>
        <SectionDivider/>
        {!props.solution?.radius && <GraphPlaceHolder>Graph Unsolved</GraphPlaceHolder>}
        {props.solution?.radius && <>
            <p>k: {Math.round(props.solution?.k)}</p>
            <p>Cost: {threeDecimalPlaces.format(props.solution?.radius)}</p>
            <p>Outliers: {Math.round(props.solution?.outliers)}</p>
            <p>Time Taken: {threeDecimalPlaces.format(props.solution?.timeTaken)}s</p>
        </>}
    </ChartFrame>
}