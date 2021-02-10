import React, {useState} from "react";
import {Collapse, IconButton} from "@material-ui/core";
import CloseIcon from '@material-ui/icons/Close';
import {Alert, AlertTitle} from "@material-ui/lab";
import styled from "@emotion/styled";

interface Props {
    open: boolean
    onClose: () => void
    text: string
    infoText?: string
}

const AlertContainer = styled("div")`
  width: 70%;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  top: 15px;
  text-align: center;
  position: absolute;
`

function CloseableAlert(props: Props) {
    const [infoOpen, setInfoOpen] = useState<boolean>(false)
    return <AlertContainer>
        <Collapse in={props.open}>
            <Alert severity="warning"
                   action={
                       <IconButton aria-label="close" color="inherit" size="small" onClick={props.onClose}>
                           <CloseIcon fontSize="inherit"/>
                       </IconButton>
                   }
            >
                {props.text}
            </Alert>
        </Collapse>
    </AlertContainer>
}

export default CloseableAlert
