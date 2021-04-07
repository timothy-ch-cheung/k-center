import {H3} from "../configuration/Layout";
import {CircularProgress} from "@material-ui/core";
import React from "react";
import styled from "@emotion/styled";
import {Dimensions} from "../../interfaces";

interface Props {
    title: String
    subtitle?: String
    loading?: boolean
    dimensions: Dimensions
}

const Subtitle = styled("h5")`
  margin: 5px 20px;
`

const PanelContainer = styled("div")`
    display: grid;
    grid-template-rows: ${(props: Dimensions) => 0.6 * props.height}px ${(props: Dimensions) => 0.4 * props.height}px;
    grid-template-columns: ${(props: Dimensions) => 0.9 * props.width}px ${(props: Dimensions) => 0.1 * props.width}px;
    width: ${(props: Dimensions) => props.width}px;
    grid-template-areas:
    "top-left right"
    "bot-left right";
    margin-bottom: 5px;
`


export default function TitlePanel(props: Props) {
    return <PanelContainer width={props.dimensions.width} height={props.dimensions.height}>
        <H3 style={{gridArea: "top-left"}}>{props.title}</H3>
        {props.subtitle && <Subtitle style={{gridArea: "bot-left"}}>{props.subtitle}</Subtitle>}
        {props.loading && <CircularProgress style={{gridArea: "right", height: "30px", width: "30px", margin: "auto"}}/>}
    </PanelContainer>
}