import {ChartFrame} from "../chart/Chart";
import {H3, SectionDivider} from "../configuration/Layout";
import PagingBar from "../Pagination/PagingBar";
import React from "react";
import styled from "@emotion/styled";
import {SolutionStep} from "../../pages/steps/Steps";
import API from "../../API";
import {algorithms} from "../../constants/algorithms";

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

}

interface Dimensions {
    width: number
    height: number
}


const DEFAULT_STEP_TEXT = ""

const TextBox = styled("p")`
    width: ${(props: Dimensions) => props.width}px;
    height: ${(props: Dimensions) => props.height}px;
`

const Subtitle = styled("h5")`
    margin: 5px 20px;
`

export default function Step(props: Props) {

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

    const handleNext = () => {
        const newPage = props.pageControl.currentPage + 1
        let update: UpdatePageControl = {prevEnabled: true, currentPage: newPage}
        if (props.pageControl.currentPage == props.solutionHistory.length) {
            API.post("/step/next", {id: props.id}).then(function (response) {
                    props.setChartData(response.data)
                    props.updateSolutionHistory(response.data)
                    if (!response.data.step.active) {
                        update = {...update, ...{maxPage: newPage, nextEnabled: false}}
                        let completedSolution = JSON.parse(JSON.stringify(props.solutionHistory[props.pageControl.currentPage - 1]))
                        completedSolution.step.label = response.data.step.label
                    }
                    props.pageControl.updateControl(update)
                }
            )
        } else {
            props.setChartData(props.solutionHistory[newPage - 1])
            if (props.pageControl.maxPage != -1 && newPage == props.pageControl.maxPage) {
                update = {...update, ...{nextEnabled: false}}
            }
            props.pageControl.updateControl(update)
        }
    }

    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Step-By-Step Walkthrough</H3>
        {props.algorithm && <Subtitle>{algorithms[props.algorithm].short_name}</Subtitle>}
        <SectionDivider/>
        <TextBox width={props.width} height={320}>
            {props.text ? props.text : DEFAULT_STEP_TEXT}
        </TextBox>
        <SectionDivider/>
        <PagingBar currentPage={props.pageControl.currentPage}
                   isNextEnabled={props.pageControl.nextEnabled}
                   isPrevEnabled={props.pageControl.prevEnabled}
                   handlePrevClick={handlePrev}
                   handleNextClick={handleNext}
                   maxPage={props.pageControl.maxPage}
        />
    </ChartFrame>
}