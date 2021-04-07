import React, {useState} from "react";
import {ChartData, ChartFrame} from "../chart/Chart";
import API from "../../API";
import {H3, SectionDivider} from "./Layout";
import ConfigFormBody, {Mode} from "./ConfigFormBody";
import {AlertData} from "../../pages/solve/Solve";

interface Props {
    width: number
    height: number
    chartData?: ChartData
    setChartData: (chart: any) => void
    setSolveRequestData: (data: SolveRequestData) => void
    gridArea?: string
    alertOpen: (alert: AlertData) => void
}

export interface SolveRequestData {
    k: number
    blue: number
    red: number
    graph: string
    algorithm: string
}

function ConfigPanel(props: Props) {
    const [isSolving, setIsSolving] = useState<boolean>(false)

    const handleSolveSubmit = (requestBody: any) => {
        setIsSolving(true)
        API.post("/solve", requestBody).then(function (response) {
                props.setChartData(response.data)
                props.setSolveRequestData(requestBody)
                setIsSolving(false)
                if (response.data.alert != null) {
                    props.alertOpen(response.data.alert)
                }
            }
        )
    }

    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Configuration</H3>
        <SectionDivider/>
        <ConfigFormBody
            submitButtonText="Solve"
            handleSubmit={handleSolveSubmit}
            chartData={props.chartData}
            setChartData={props.setChartData}
            isProcessing={isSolving}
            mode={Mode.Solve}
        />
    </ChartFrame>
}

export default ConfigPanel;