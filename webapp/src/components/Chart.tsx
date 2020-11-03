import React, {useEffect, useRef} from 'react';
import d3Chart from './D3Chart'


interface ChartItem {
    colour: string,
    x: number,
    y: number,
    center?: boolean
}

interface ChartData {
    chart: ChartItem[]
    width: number,
    height: number
}

export default function Chart(props: ChartData): JSX.Element {
    useEffect(() => {
        d3Chart.create({
            width: props.width || 0,
            height: props.height || 0,
            chart: props.chart || []
        });
    }, [props])

    return <div style={{backgroundColor: "white", padding: "10px", paddingRight: "30px", borderRadius: "25px",
        border: "2px solid #73AD21"}}>
        <svg className="chart"/>
    </div>
}