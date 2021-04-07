import React, {useState} from "react";
import {Collapse, IconButton} from "@material-ui/core";
import CloseIcon from '@material-ui/icons/Close';
import {Alert} from "@material-ui/lab";
import styled from "@emotion/styled";
import {responses} from "../../constants/responses";
import {AlertData} from "../../pages/solve/Solve";

interface Props {
    open: boolean
    onClose: () => void
    alertData: AlertData
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

const MessageContainer = styled("div")`
  display: flex;
  flex-flow: column;
`

const LinkBtn = styled("button")`
  background: none;
  border: none;
  padding: 0;
  color: #069;
  text-decoration: underline;
  cursor: pointer;
  outline: none;

  &:hover {
    text-decoration: none;
  }
`

const InfoText = styled("p")`
  text-align: left;
  margin-top: 10px;
  margin-bottom: 0px;
  color: dimgray;
`

function CloseableAlert(props: Props) {
    const [infoOpen, setInfoOpen] = useState<boolean>(false)

    const onClickLink = () => {
        setInfoOpen(!infoOpen)
    }

    const hasExtraInfo = responses[props.alertData.type].additionalInfo !== undefined

    return <AlertContainer>
        <Collapse in={props.open}>
            <Alert severity="warning"
                   action={
                       <IconButton aria-label="close" color="inherit" size="small" onClick={props.onClose}>
                           <CloseIcon fontSize="inherit"/>
                       </IconButton>
                   }
            >
                <MessageContainer>
                    <div style={{display: "flex"}}>
                        <p style={{margin: 0}}>{props.alertData.message}</p>
                        <div style={{width: "10px"}}/>
                        {
                            hasExtraInfo &&
                            <LinkBtn onClick={onClickLink}>{responses[props.alertData.type].message}</LinkBtn>
                        }
                    </div>
                    <Collapse in={infoOpen}>
                        <InfoText>{responses[props.alertData.type].additionalInfo}</InfoText>
                    </Collapse>
                </MessageContainer>

            </Alert>
        </Collapse>
    </AlertContainer>
}

export default CloseableAlert
