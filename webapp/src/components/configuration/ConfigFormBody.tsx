import React, {useState} from "react";
import {Button, CircularProgress, FormControl, InputLabel, MenuItem, Select} from "@material-ui/core";
import NumberSlider from "../number_slider/NumberSlider";
import styled from "@emotion/styled";
import PaletteIcon from "@material-ui/icons/Palette";
import {HorizontalGroup, SectionDivider, Spacer} from "./Layout";
import {ChartData} from "../chart/Chart";
import API from "../../API";
import {SolveRequestData} from "./ConfigPanel";
import {algorithms} from "../../constants/algorithms";

interface Props {
    submitButtonText: string
    handleSubmit: (event: any) => void
    chartData?: ChartData
    setChartData: (data: any) => void
    isProcessing: boolean
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

export default function (props: Props) {
    const [k, setK] = useState<number>(1)
    const [blue, setBlue] = useState<number>(1)
    const [red, setRed] = useState<number>(1)
    const [problemInstance, setProblemInstance] = useState<string>('')
    const [algorithm, setAlgorithm] = useState<string>('')

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
    }

    const handleAlgorithmSelectChange = (event: any) => {
        setAlgorithm(event.target.value)
    }

    const handleSubmit = (event: any) => {
        event.preventDefault()
        const requestBody: SolveRequestData = {
            k: k,
            blue: blue,
            red: red,
            graph: problemInstance,
            algorithm: algorithm
        }
        props.handleSubmit(requestBody)
    }

    return <form onSubmit={handleSubmit}>
        <FormControlNoWrap>
            <InputLabel>Problem instance</InputLabel>
            <Select onChange={handleProblemInstanceSelectChange}>
                <MenuItem value={"basic"}>basic</MenuItem>
                <MenuItem value={"basic_with_outlier"}>basic (with outlier)</MenuItem>
                <MenuItem value={"medium"}>medium</MenuItem>
                <MenuItem value={"large"}>large</MenuItem>
                <MenuItem value={"k_center_large"}>k center large</MenuItem>
                <MenuItem value={"extreme_point"}>extreme point</MenuItem>
                <MenuItem value={"thousand"}>Thousand</MenuItem>
                <MenuItem value={"five_thousand"}>Five Thousand</MenuItem>
                <MenuItem value={"ten_thousand"}>Ten Thousand</MenuItem>
            </Select>
        </FormControlNoWrap>
        <FormControlNoWrap>
            <InputLabel>Algorithm</InputLabel>
            <Select onChange={handleAlgorithmSelectChange}>
                <MenuItem value={"greedy"}>{algorithms.greedy.name}</MenuItem>
                <MenuItem value={"greedy_reduce"}>{algorithms.greedy_reduce.name}</MenuItem>
                <MenuItem value={"colourful_bandyapadhyay_pseudo"}>{algorithms.colourful_bandyapadhyay_pseudo.name}</MenuItem>
                <MenuItem value={"colourful_bandyapadhyay"}>{algorithms.colourful_bandyapadhyay.name}</MenuItem>
                <MenuItem value={"pbs"}>{algorithms.pbs.name}</MenuItem>
                <MenuItem value={"colourful_pbs"}>{algorithms.colourful_pbs.name}</MenuItem>
            </Select>
        </FormControlNoWrap>
        <Spacer/>
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
                disabled={props.isProcessing}>{props.submitButtonText}
            </Button>
            {props.isProcessing && <CircularProgress style={{height: "35px", width: "35px"}}/>}
        </HorizontalGroup>
    </form>
}