import React from "react";
import {Grid, Input, Slider, Typography} from "@material-ui/core";

interface Props {
    label: string
    max: number
    min: number
    value: number
    setValue: (newValue: any) => void
    icon?: any
}

function NumberSlider(props: Props) {
    const handleSliderChange = (event: any, newValue: number | number[]) => {
        props.setValue(newValue);
    };

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        props.setValue(event.target.value === '' ? '' : Number(event.target.value))
    };

    const handleBlur = () => {
        if (props.value < props.min) {
            props.setValue(props.min)
        } else if (props.value > props.max) {
            props.setValue(props.max)
        }
    };

    return <>
        <Typography gutterBottom>
            {props.label}
        </Typography>
        <Grid container spacing={2} alignItems="center">

            <Grid item style={props.icon ? {width: "15%"} : {width: "0%"}}>
                {props.icon && <>{props.icon}</>}
            </Grid>
            <Grid item style={props.icon ? {width: "70%"} : {width: "80%"}}>
                <Slider
                    value={props.value}
                    onChange={handleSliderChange}
                    marks
                    min={props.min}
                    max={props.max}
                />
            </Grid>
            <Grid item style={{width: "15%"}}>
                <Input
                    value={props.value}
                    onChange={handleInputChange}
                    onBlur={handleBlur}
                />
            </Grid>
        </Grid>
    </>
}

export default NumberSlider