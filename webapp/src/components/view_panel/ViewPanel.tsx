import styled from "@emotion/styled";
import AppsIcon from "@material-ui/icons/Apps";
import SearchIcon from "@material-ui/icons/Search";
import {ToggleButton, ToggleButtonGroup} from "@material-ui/lab";
import React from "react";
import {Button, Chip, MobileStepper} from "@material-ui/core";
import {KeyboardArrowLeft, KeyboardArrowRight} from "@material-ui/icons";

export enum View {
    Individual,
    Population
}

interface Props {
    view: View
    changeView: (event: any, view: View) => void
    maxSteps: number
    activeStep: number
    handleNext: () => void
    handleBack: () => void
    subSolve: boolean
}

const PopulationIcon = styled(AppsIcon)`
  font-size: 1em;
`

const IndividualIcon = styled(SearchIcon)`
  font-size: 1em;
`

export default function ViewPanel(props: Props): JSX.Element {
    return <div style={{marginBottom: "2px", display: "flex", justifyContent: "space-between"}}>
        <ToggleButtonGroup value={props.view} onChange={props.changeView} aria-label="view-mode" exclusive>
            <ToggleButton value={View.Population} aria-label="population" disabled={props.subSolve}>
                <PopulationIcon/>
            </ToggleButton>
            <ToggleButton value={View.Individual} aria-label="individual" disabled={props.subSolve}>
                <IndividualIcon/>
            </ToggleButton>
        </ToggleButtonGroup>
        {props.view === View.Individual && !props.subSolve && <MobileStepper
            activeStep={props.activeStep}
            variant="dots"
            position="static"
            steps={props.maxSteps}
            style={{width: "300px", height: "20px"}}
            nextButton={
                <Button size="small" onClick={props.handleNext} disabled={props.activeStep === props.maxSteps - 1}>
                    Next
                    <KeyboardArrowRight/>
                </Button>
            }
            backButton={
                <Button size="small" onClick={props.handleBack} disabled={props.activeStep === 0}>
                    <KeyboardArrowLeft/>
                    Back
                </Button>
            }/>}
        {props.view === View.Individual &&
        <Chip label={props.subSolve? "new individual" :`Individual: ${props.activeStep}`}
              style={{height: "35px"}}/>}
    </div>
}