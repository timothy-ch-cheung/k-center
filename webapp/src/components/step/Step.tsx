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


const DEFAULT_STEP_TEXT = ""

const TextBox = styled("p")`
  width: ${(props: Dimensions) => props.width}px;
  height: ${(props: Dimensions) => props.height}px;
`

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

    const handleNext = () => {
        const newPage = props.pageControl.currentPage + 1
        let update: UpdatePageControl = {prevEnabled: true, currentPage: newPage}
        if (props.pageControl.currentPage == props.solutionHistory.length) {
            setIsLoading(true)
            API.post("/step/next", {id: props.id}).then(function (response) {
                    props.setChartData(response.data)
                    props.updateSolutionHistory(response.data)
                    if (!response.data.step.active) {
                        update = {...update, ...{maxPage: newPage, nextEnabled: false}}
                        let completedSolution = JSON.parse(JSON.stringify(props.solutionHistory[props.pageControl.currentPage - 1]))
                        completedSolution.step.label = response.data.step.label
                    }
                    props.pageControl.updateControl(update)
                    setIsLoading(false)
                    console.log(response.data)
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
        <PagingBar currentPage={props.pageControl.currentPage}
                   isNextEnabled={props.pageControl.nextEnabled && !isLoading}
                   isPrevEnabled={props.pageControl.prevEnabled && !isLoading}
                   handlePrevClick={handlePrev}
                   handleNextClick={handleNext}
                   maxPage={props.pageControl.maxPage}
        />
    </ChartFrame>
}