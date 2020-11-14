import React, {useState} from "react";
import {ChartData, ChartFrame} from "../chart/Chart";
import {Button, CircularProgress, Divider, FormControl, InputLabel, MenuItem, Select} from "@material-ui/core";
import styled from "@emotion/styled";
import NumberSlider from "../number_slider/NumberSlider";
import PaletteIcon from '@material-ui/icons/Palette';
import API from "../../API";

interface Props {
    width: number
    height: number
    chartData?: ChartData
    setChartData: (chart: any) => void
}

const H3 = styled("h3")`
    margin: 5px 10px;
`

const SectionDivider = styled(Divider)`
    margin-bottom: 10px;
`

const FormControlNoWrap = styled(FormControl)`
    display: flex;
    wrap: nowrap;
    margin-bottom: 10px;
`

const Spacer = styled("div")`
    height: 15px;
`

const BluePaletteIcon = styled(PaletteIcon)`
    color: blue
`

const RedPaletteIcon = styled(PaletteIcon)`
    color: red
`

const HorizontalGroup = styled("div")`
    display: flex;
    justify-content: space-between;
`

function Configurator(props: Props) {
    const [k, setK] = useState<number>(1)
    const [blue, setBlue] = useState<number>(1)
    const [red, setRed] = useState<number>(1)
    const [problemInstance, setProblemInstance] = useState<string>('')
    const [algorithm, setAlgorithm] = useState<string>('')
    const [isSolving, setIsSolving] = useState<boolean>(false)

    const handleProblemInstanceSelectChange = (event: any) => {
        const problemInstance = event.target.value
        setProblemInstance(problemInstance)
        API.get(`/graph/${problemInstance}`).then(function (response) {
                props.setChartData(response.data)
                setK(response.data.k)
                setBlue(response.data.minBlue)
                setRed(response.data.minRed)
            }
        )
    }

    const handleAlgorthmSelectChange = (event: any) => {
        setAlgorithm(event.target.value)
    }

    const handleSolveSubmit = (event: any) => {
        event.preventDefault()
        setIsSolving(true)
        const requestBody = {
            k: k,
            blue: blue,
            red: red,
            graph: problemInstance,
            algorithm: algorithm
        }
        API.post("/solve", requestBody).then(function (response) {
                console.log(response.data)
                props.setChartData(response.data)
                setIsSolving(false)
            }
        )
    }

    return <ChartFrame width={props.width} height={props.height}>
        <H3>Configuration</H3>
        <SectionDivider/>
        <form onSubmit={handleSolveSubmit}>
            <FormControlNoWrap>
                <InputLabel>Problem instance</InputLabel>
                <Select onChange={handleProblemInstanceSelectChange}>
                    <MenuItem value={"basic"}>basic</MenuItem>
                    <MenuItem value={"basic_with_outlier"}>basic (with outlier)</MenuItem>
                    <MenuItem value={"medium"}>medium</MenuItem>
                    <MenuItem value={"large"}>large</MenuItem>
                </Select>
            </FormControlNoWrap>
            <FormControlNoWrap>
                <InputLabel>Algorithm</InputLabel>
                <Select onChange={handleAlgorthmSelectChange}>
                    <MenuItem value={"greedy"}>greedy</MenuItem>
                    <MenuItem value={"greedy_reduce"}>greedy (modified to optimise radii)</MenuItem>
                    <MenuItem value={"colourful_bandyapadhyay"}>O(1)-colourful (Bandyapadhyay et al. 2019)</MenuItem>
                </Select>
            </FormControlNoWrap>
            <Spacer/>
            <NumberSlider
                label="Number of centers"
                min={1}
                max={props.chartData?.nodes ||10}
                value={k}
                setValue={setK}/>
            <NumberSlider
                label="Min blue coverage"
                min={1}
                max={props.chartData?.blue ||10}
                value={blue}
                setValue={setBlue}
                icon={<BluePaletteIcon/>}/>
            <NumberSlider
                label="Min red coverage"
                min={1}
                max={props.chartData?.red ||10}
                value={red}
                setValue={setRed}
                icon={<RedPaletteIcon/>}/>
            <Spacer></Spacer>
            <SectionDivider/>
            <HorizontalGroup>
                <Button variant="contained" color="primary" type="submit">Solve</Button>
                {isSolving && <CircularProgress style={{height: "35px", width:"35px"}}/>}
            </HorizontalGroup>

        </form>
    </ChartFrame>
}

export default Configurator;