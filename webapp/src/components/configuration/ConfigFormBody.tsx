import React, {useState} from "react";
import {Button, CircularProgress, FormControl, FormHelperText, InputLabel, MenuItem, Select} from "@material-ui/core";
import NumberSlider from "../number_slider/NumberSlider";
import styled from "@emotion/styled";
import PaletteIcon from "@material-ui/icons/Palette";
import {HorizontalGroup, SectionDivider, Spacer} from "./Layout";
import {ChartData} from "../chart/Chart";
import API from "../../API";
import {SolveRequestData} from "./ConfigPanel";
import {algorithms} from "../../constants/algorithms";

export enum Mode {
    Solve,
    Step
}

interface Props {
    submitButtonText: string
    handleSubmit: (event: any) => void
    chartData?: ChartData
    setChartData: (data: any) => void
    isProcessing: boolean
    mode: Mode
}

const FormControlNoWrap = styled(FormControl)`
  display: flex;
  wrap: nowrap;
  margin-bottom: 10px;
`

const BluePaletteIcon = styled(PaletteIcon)`
  color: blue
`

const RedPaletteIcon = styled(PaletteIcon)`
  color: red
`

const ErrorText = styled(FormHelperText)`
  color: red;
  margin-top: 0;
`

const SelectInputLabel = styled(InputLabel)`
  background-color: white;
  padding-left: 2px;
  padding-right: 2px;
  border-radius: 4px;
`

export default function (props: Props) {
    const [k, setK] = useState<number>(1)
    const [blue, setBlue] = useState<number>(1)
    const [red, setRed] = useState<number>(1)
    const [problemInstance, setProblemInstance] = useState<string>('')
    const [algorithm, setAlgorithm] = useState<string>('')
    const [problemInstanceValid, setProblemInstanceValid] = useState<boolean>(false)
    const [isProblemInstanceChanged, setProblemInstanceChanged] = useState<boolean>(false)
    const [algorithmValid, setAlgorithmValid] = useState<boolean>(false)
    const [isAlgorithmChanged, setAlgorithmChanged] = useState<boolean>(false)

    const handleProblemInstanceSelectChange = (event: any) => {
        const problemInstance = event.target.value
        setProblemInstance(problemInstance)
        API.get(`/graph/${problemInstance}`).then(function (response) {
                props.setChartData(response.data)
                setK(response.data.optimalSolution.k)
                setBlue(response.data.optimalSolution.minBlue)
                setRed(response.data.optimalSolution.minRed)
            }
        )
        if (problemInstance !== "") {
            setProblemInstanceValid(true)
        }
    }

    const handleAlgorithmSelectChange = (event: any) => {
        setAlgorithm(event.target.value)
        if (event.target.value !== "") {
            setAlgorithmValid(true)
        }
    }

    const handleAlgorithmClose = () => {
        setAlgorithmChanged(true)
        if (!algorithm) {
            setAlgorithmValid(false)
        }
    }

    const handleProblemInstanceClose = () => {
        setProblemInstanceChanged(true)
        if (!problemInstance) {
            setProblemInstanceValid(false)
        }
    }

    const handleSubmit = (event: any) => {
        event.preventDefault()
        if (!problemInstanceValid) {
            setProblemInstanceChanged(true)
        }
        if (!algorithmValid) {
            setAlgorithmChanged(true)
        }
        if (problemInstanceValid && algorithmValid) {
            const requestBody: SolveRequestData = {
                k: k,
                blue: blue,
                red: red,
                graph: problemInstance,
                algorithm: algorithm
            }
            props.handleSubmit(requestBody)
        }
    }

    return <form onSubmit={handleSubmit}>
        <Spacer height={5}/>
        <FormControlNoWrap variant={"outlined"} margin={"dense"}>
            <SelectInputLabel>Problem Instance</SelectInputLabel>
            <Select onChange={handleProblemInstanceSelectChange}
                    error={isProblemInstanceChanged && !problemInstanceValid}
                    onClose={handleProblemInstanceClose}
                    cy-data="problem-instance-select"
            >
                <MenuItem value={"basic"} cy-data="basic-instance">basic</MenuItem>
                <MenuItem value={"basic_with_outlier"}>basic (with outlier)</MenuItem>
                <MenuItem value={"medium"} cy-data="medium-instance">medium</MenuItem>
                <MenuItem value={"large"} cy-data="large-instance">large</MenuItem>
                <MenuItem value={"k_center_large"}>k center large</MenuItem>
                <MenuItem value={"extreme_point"}>extreme point</MenuItem>
                <MenuItem value={"thousand"}>Thousand</MenuItem>
                <MenuItem value={"five_thousand"}>Five Thousand</MenuItem>
                <MenuItem value={"ten_thousand"}>Ten Thousand</MenuItem>
            </Select>
            <ErrorText>{isProblemInstanceChanged && !problemInstanceValid ? "please select a problem instance" : "."}</ErrorText>
        </FormControlNoWrap>
        <FormControlNoWrap variant={"outlined"} margin={"dense"}>
            <SelectInputLabel>Algorithm</SelectInputLabel>
            <Select
                onChange={handleAlgorithmSelectChange}
                error={isAlgorithmChanged && !algorithmValid}
                onClose={handleAlgorithmClose} cy-data="algorithm-select"
            >
                {Object.entries(algorithms).map(([algorithm_name, algorithm_properties]) => {
                    if (props.mode === Mode.Step && !algorithm_properties.stepped_enabled) {
                        return null
                    }
                    return <MenuItem value={algorithm_name} cy-data={algorithm_name}>{algorithm_properties.name}</MenuItem>
                })}
            </Select>
            <ErrorText>{isAlgorithmChanged && !algorithmValid ? "please select an algorithm" : "."}</ErrorText>
        </FormControlNoWrap>
        <NumberSlider
            label="Number of centers"
            min={1}
            max={props.chartData?.nodes || 10}
            value={k}
            setValue={setK}/>
        <NumberSlider
            label="Min blue coverage"
            min={1}
            max={props.chartData?.blue || 10}
            value={blue}
            setValue={setBlue}
            icon={<BluePaletteIcon/>}/>
        <NumberSlider
            label="Min red coverage"
            min={1}
            max={props.chartData?.red || 10}
            value={red}
            setValue={setRed}
            icon={<RedPaletteIcon/>}/>
        <Spacer/>
        <SectionDivider/>
        <HorizontalGroup>
            <Button
                variant="contained"
                color="primary"
                type="submit"
                disabled={props.isProcessing}
                cy-data="solve-submit-btn"
            >{props.submitButtonText}
            </Button>
            {props.isProcessing && <CircularProgress style={{height: "35px", width: "35px"}}/>}
        </HorizontalGroup>
    </form>
}