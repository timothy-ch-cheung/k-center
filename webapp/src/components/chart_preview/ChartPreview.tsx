import {ChartSvg, Solution} from "../chart/Chart";
import {ChartItem} from "../chart/ChartInterfaces";
import React, {useEffect} from "react";
import d3ChartPreview from './D3ChartPreview'
import styled from "@emotion/styled";
import {Dimensions} from "../../interfaces";

interface Props {
    data?: ChartItem[]
    width: number
    height: number
    solution?: Solution
    id: number
    onClick?: (id: any) => void
}

const ChartFrame = styled("div")`
  background-color: white;
  padding: 5px;
  border-radius: 15px;
  border: 1px solid lightgray;
  margin: 3px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;ó
  user-select: none;
  width: ${(props: Dimensions) => props.width}px;
  height: ${(props: Dimensions) => props.height}px;
  overflow: hidden;
`

const Heading = styled("h5")`
  margin: 0;
`

export default function ChartPreview(props: Props): JSX.Element {
    let initialised = false
    let chartHeight = 0.8 * props.height
    const initialise = () => {
        props.data && d3ChartPreview.create({
            width: props.width,
            height: chartHeight,
            data: props.data,
            solution: props.solution,
            id: props.id
        });
        initialised = true
    }

    const handleClick = () => {
        props.onClick && props.onClick(props.id)
    }

    useEffect(() => {
        initialise()
    }, [])

    useEffect(() => {
        if (!initialised) {
            initialise()
        }

        props.data && d3ChartPreview.update({
            width: props.width,
            height: chartHeight,
            data: props.data,
            solution: props.solution,
            id: props.id
        });
    }, [props, props.data])

    return <ChartFrame width={props.width} height={props.height} onClick={handleClick}>
        <Heading>{`${props.id} cost=${props.solution?.radius.toFixed(3)}`}</Heading>
        <ChartSvg className={`preview_${props.id}`}/>
    </ChartFrame>
}