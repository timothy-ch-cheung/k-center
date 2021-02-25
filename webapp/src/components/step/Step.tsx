import {ChartFrame} from "../chart/Chart";
import {SectionDivider} from "../configuration/Layout";
import PagingBar from "../Pagination/PagingBar";
import React, {useState} from "react";
import styled from "@emotion/styled";
import {SolutionStep} from "../../pages/steps/Steps";
import API from "../../API";
import {algorithms} from "../../constants/algorithms";
import {Dimensions} from "../../interfaces";
import TitlePanel from "../title_panel/TitlePanel";
import {Button, ButtonGroup} from "@material-ui/core";

export interface PageSetting {
    nextEnabled: boolean
    prevEnabled: boolean
    currentPage: number
    maxPage?: number
}

export interface UpdatePageControl {
    nextEnabled?: boolean
    prevEnabled?: boolean
    currentPage?: number
    maxPage?: number
}

export interface PageControl extends PageSetting {
    updateControl: (update: UpdatePageControl) => void
}

interface Props {
    width: number
    height: number
    gridArea: string
    text?: string
    solutionHistory: SolutionStep[]
    updateSolutionHistory: (history: any) => void
    setChartData: (data: SolutionStep) => void
    id: string
    algorithm?: string
    pageControl: PageControl
    isInspect: boolean
    setIsInspect: (isInspect: boolean) => void
    isInitialMoveMade: boolean
    setIsInitialMoveMade: (isInitialMoveMade: boolean) => void
    isActive: boolean
    setIsActive: (isActive: boolean) => void
}


const DEFAULT_STEP_TEXT = ""

const TextBox = styled("p")`
  width: ${(props: Dimensions) => props.width}px;
  flex: 2;
`

const SmallButton = styled(Button)`
  font-size: 0.6em;
  padding: 5px;
  width: 50%;
`

interface SubStep {
    isInspect: boolean
    isActive: boolean
    isInitialMoveMade: boolean
    onInspectClick: () => void
    onSkipClick: () => void
}

const StepBar = (props: SubStep) => {
    const inspectEnabled = !props.isInitialMoveMade || (props.isActive && !props.isInspect)
    const skipEnabled = props.isInitialMoveMade && props.isActive && props.isInspect
    return <ButtonGroup>
        <SmallButton disabled={!inspectEnabled} onClick={props.onInspectClick}>Inspect next
            generation</SmallButton>
        <SmallButton disabled={!skipEnabled} onClick={props.onSkipClick}>Skip to next
            generation</SmallButton>
    </ButtonGroup>
}

export default function Step(props: Props) {
    const [isLoading, setIsLoading] = useState<boolean>(false)

    const handlePrev = () => {
        const newPage = props.pageControl.currentPage - 1
        const update: UpdatePageControl = {nextEnabled: true, currentPage: newPage}

        if (props.pageControl.currentPage > 1) {
            props.setChartData(props.solutionHistory[newPage - 1])
        }
        if (props.pageControl.currentPage == 2) {
            update.prevEnabled = false
        }
        props.pageControl.updateControl(update)
    }

    const apiNext = (path: string, update: UpdatePageControl, newPage: number) => {
        API.post(path, {id: props.id}).then(function (response) {
                props.setChartData(response.data)
                props.updateSolutionHistory(response.data)
                if (!response.data.step.active) {
                    update = {...update, ...{maxPage: newPage, nextEnabled: false}}
                    let completedSolution = JSON.parse(JSON.stringify(props.solutionHistory[props.pageControl.currentPage - 1]))
                    completedSolution.step.label = response.data.step.label
                    props.setIsActive(false)
                }
                if (response.data.step.inspect) {
                    props.setIsInspect(true)
                } else {
                    props.setIsInspect(false)
                }
                props.pageControl.updateControl(update)
                setIsLoading(false)
                console.log(response.data)
            }
        )
    }

    const handleNext = () => {
        const newPage = props.pageControl.currentPage + 1
        let update: UpdatePageControl = {prevEnabled: true, currentPage: newPage}
        if (props.pageControl.currentPage == props.solutionHistory.length) {
            setIsLoading(true)
            if (props.isInspect) {
                apiNext("/step/inspect", update, newPage)
            } else {
                apiNext("/step/next", update, newPage)
            }

        } else {
            props.setChartData(props.solutionHistory[newPage - 1])
            if (props.pageControl.maxPage != -1 && newPage == props.pageControl.maxPage) {
                update = {...update, ...{nextEnabled: false}}
            }
            props.pageControl.updateControl(update)
        }
        props.setIsInitialMoveMade(true)
    }

    const handleInspect = () => {
        const newPage = props.pageControl.currentPage + 1
        let update: UpdatePageControl = {prevEnabled: true, currentPage: newPage}
        apiNext("/step/inspect", update, newPage)
        props.setIsInspect(true)
        props.setIsInitialMoveMade(true)
    }

    const handleSkip = () => {
        const newPage = props.pageControl.currentPage + 1
        let update: UpdatePageControl = {prevEnabled: true, currentPage: newPage}
        if (props.pageControl.currentPage == props.solutionHistory.length) {
            setIsLoading(true)
            apiNext("/step/next", update, newPage)
        }
        props.setIsInspect(false)
    }

    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <div style={{display: "flex", flexFlow: "column", height: props.height}}>
            <TitlePanel
                title={"Step-By-Step Walkthrough"}
                subtitle={props.algorithm ? algorithms[props.algorithm].short_name : ""}
                loading={isLoading}
                dimensions={{width: props.width, height: 50}}/>
            <SectionDivider/>
            <TextBox width={props.width} height={320}>
                {props.text ? props.text : DEFAULT_STEP_TEXT}
            </TextBox>
            <SectionDivider/>
            {props.algorithm && algorithms[props.algorithm].type == "genetic" &&
            <StepBar isInspect={props.isInspect}
                     isActive={props.isActive}
                     isInitialMoveMade={props.isInitialMoveMade}
                     onInspectClick={handleInspect}
                     onSkipClick={handleSkip}
            />}
            <PagingBar currentPage={props.pageControl.currentPage}
                       isNextEnabled={props.pageControl.nextEnabled && !isLoading}
                       isPrevEnabled={props.pageControl.prevEnabled && !isLoading}
                       handlePrevClick={handlePrev}
                       handleNextClick={handleNext}
                       maxPage={props.pageControl.maxPage}
            />
        </div>
    </ChartFrame>
}