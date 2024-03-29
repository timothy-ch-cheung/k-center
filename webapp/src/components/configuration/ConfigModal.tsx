import React, {useState} from "react";
import {ChartData, ChartFrame} from "../chart/Chart";
import {Button, Modal, Paper} from "@material-ui/core";
import {H3, SectionDivider} from "./Layout";
import styled from "@emotion/styled";
import ConfigFormBody, {Mode} from "./ConfigFormBody";
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
    resetSteps: () => void
    setId: (id: string) => void
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
        requestBody.id = props.id
        API.post("/step/start", requestBody).then(function (response) {
                const newChart = {...props.chartData, ...{step: {label: "Graph loaded."}}}
                props.setChartData(newChart)
                props.setStepSolveRequestData(requestBody)
                props.resetSteps()
                setIsLoading(false)
                setOpen(false);
                props.setId(response.data.id)
            }
        )
    }

    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Load new problem</H3>
        <SectionDivider/>
        <Button variant="contained" color="primary" onClick={handleOpen} cy-data="steps-modal-btn">Load</Button>

        <Modal open={open} onClose={handleClose}>
            <Window variant="outlined">
                <ConfigFormBody
                    submitButtonText="Confirm"
                    handleSubmit={handleLoadSubmit}
                    chartData={props.chartData}
                    setChartData={props.setChartData}
                    isProcessing={isLoading}
                    mode={Mode.Step}
                />
            </Window>
        </Modal>
    </ChartFrame>
}