import React, {useState} from "react";
import {ChartData, ChartFrame} from "../chart/Chart";
import {Button, Modal, Paper} from "@material-ui/core";
import {H3, SectionDivider} from "./Layout";
import styled from "@emotion/styled";
import ConfigFormBody from "./ConfigFormBody";
import {SolveRequestData} from "./ConfigPanel";
import API from "../../API";
import {SolutionStep} from "../../pages/steps/Steps";

export interface StepSolveRequestData extends SolveRequestData {
    id: string
}

interface Props {
    gridArea: string
    width: number
    height: number
    chartData?: SolutionStep
    setChartData: (data: any) => void
    setStepSolveRequestData: (data: StepSolveRequestData) => void
    id: string
}

const Window = styled(Paper)`
    width: 500px;
    padding: 20px;
    margin: 150px auto;
`

export default function ConfigModal(props: Props) {
    const [open, setOpen] = useState<boolean>(false)
    const [isLoading, setIsLoading] = useState<boolean>(false)
    const [oldChart, setOldChart] = useState<ChartData>()

    const handleOpen = () => {
        setOldChart(props.chartData)
        setOpen(true);
    }

    const handleClose = () => {
        setOpen(false);
        props.setChartData(oldChart)
    }

    const handleLoadSubmit = (requestBody: StepSolveRequestData) => {
        setIsLoading(true)
        setOpen(false);
        requestBody.id = props.id
        API.post("/step/start", requestBody).then(function (response) {
                props.setChartData(response.data)
                props.setStepSolveRequestData(requestBody)
                setIsLoading(false)
            }
        )
    }

    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Load new problem</H3>
        <SectionDivider/>
        <Button variant="contained" color="primary" onClick={handleOpen}>Load</Button>

        <Modal open={open} onClose={handleClose}>
            <Window variant="outlined" style={{width: "500px", padding: "20px"}}>
                <ConfigFormBody
                    submitButtonText="Confirm"
                    handleSubmit={handleLoadSubmit}
                    chartData={props.chartData}
                    setChartData={props.setChartData}
                    isProcessing={isLoading}
                />
            </Window>
        </Modal>
    </ChartFrame>
}