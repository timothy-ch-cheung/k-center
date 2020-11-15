import React from 'react';
import {IconButton, Tooltip} from "@material-ui/core";
import InfoIcon from "@material-ui/icons/Info";
import {HorizontalGroup} from "../configuration/Configurator";
import styled from "@emotion/styled";

interface Props {
    tooltipText: any
    text: string
    style?: object
}

const IconBtn = styled(IconButton)`
    height: 24px;
    padding: 0px;
`

export default function TextWithTooltip(props: Props): JSX.Element {
    return <HorizontalGroup>
        <p style={{...{marginTop: "0px", marginBottom: "0px"}, ...props.style}}>{props.text}</p>
        <Tooltip title={props.tooltipText}>
            <IconBtn aria-label="back">
                <InfoIcon/>
            </IconBtn>
        </Tooltip>
    </HorizontalGroup>
}