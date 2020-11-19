import {ChartData, ChartFrame} from "../chart/Chart";
import {H3, SectionDivider} from "../configuration/Layout";
import PagingBar from "../Pagination/PagingBar";
import React, {useState} from "react";
import styled from "@emotion/styled";
import {SolutionStep} from "../../pages/steps/Steps";
import API from "../../API";

interface Props {
    width: number
    height: number
    gridArea: string
    text?: string
    solutionHistory: SolutionStep[]
    updateSolutionHistory: (history: any) => void
    setChartData: (data: SolutionStep) => void
    id: string

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

export default function Step(props: Props) {
    const [nextEnabled, setNextEnabled] = useState<boolean>(true)
    const [prevEnabled, setPrevEnabled] = useState<boolean>(false)
    const [currentPage, setCurrentPage] = useState<number>(0)
    const [maxPage, setMaxPage] = useState<number>(-1)

    const handlePrev = () => {
        const newPage = currentPage - 1
        setNextEnabled(true)
        if (currentPage > 1) {
            props.setChartData(props.solutionHistory[newPage-1])
        }
        if (currentPage == 2) {
            setPrevEnabled(false)
        }
        setCurrentPage(newPage)
    }

    const handleNext = () => {
        const newPage = currentPage + 1
        setPrevEnabled(true)
        if (currentPage == props.solutionHistory.length) {
            API.post("/step/next", {id: props.id}).then(function (response) {
                    if(response.data.step.active) {
                        props.setChartData(response.data)
                        props.updateSolutionHistory(response.data)
                    } else {
                        setMaxPage(newPage)
                        setNextEnabled(false)
                        console.log(props.solutionHistory[currentPage])
                        let completedSolution = JSON.parse(JSON.stringify(props.solutionHistory[currentPage-1]))
                        completedSolution.step.label = response.data.step.label
                    }
                }
            )
        } else if (currentPage < props.solutionHistory.length - 1) {
            props.setChartData(props.solutionHistory[newPage])
        }

        if (maxPage != -1  && newPage == maxPage) {
            setNextEnabled(false)
        }
        setCurrentPage(newPage)

    }

    return <ChartFrame style={{gridArea: props.gridArea}} width={props.width} height={props.height}>
        <H3>Step-By-Step Walkthrough</H3>
        <SectionDivider/>
        <TextBox width={props.width} height={340}>
            {props.text ? props.text : DEFAULT_STEP_TEXT}
        </TextBox>
        <SectionDivider/>
        <PagingBar currentPage={currentPage}
                   isNextEnabled={nextEnabled}
                   isPrevEnabled={prevEnabled}
                   handlePrevClick={handlePrev}
                   handleNextClick={handleNext}
                   maxPage={maxPage}
        />
    </ChartFrame>
}