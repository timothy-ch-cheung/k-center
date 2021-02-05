import {ChartItem} from "../components/chart/ChartInterfaces";
import Chart, {Solution} from "../components/chart/Chart";
import React, {useState} from "react";
import ChartPreview from "../components/chart_preview/ChartPreview";
import styled from "@emotion/styled";
import {Dimensions} from "../interfaces";
import {GridList, GridListTile, Modal, Paper} from "@material-ui/core";
import {v4 as uuid} from "uuid";

interface Props {
    data?: ChartItem[]
    width: number
    height: number
    gridArea?: string
    solutions?: Solution[]
}

const ChartFrame = styled("div")`
  background-color: white;
  margin: 5px;
  padding: 15px;
  border-radius: 15px;
  border: 2px solid green;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  width: ${(props: Dimensions) => props.width}px;
  height: ${(props: Dimensions) => props.height}px;
  overflow: hidden;
`

const Window = styled(Paper)`
  width: 600px;
  padding: 20px;
  margin: 150px auto;
`

export default function PopulationChart(props: Props): JSX.Element {
    const [solutionId, setSolutionId] = useState<number>(0);
    const [open, setOpen] = useState<boolean>(false)

    const handleClick = (id: number) => {
        setOpen(true)
        setSolutionId(id)
    }

    const handleClose = () => {
        setOpen(false)
    }

    return <>
        <ChartFrame style={{gridArea: props.gridArea}} width={props.width * 1.5} height={props.height * 1.3}>
            <GridList cellHeight={155} cols={3}>
                {props.solutions && props.solutions.map((solution, index) => {
                    return <GridListTile key={index} cols={1}>
                        <ChartPreview width={130} height={130} id={index} data={props.data} solution={solution}
                                      onClick={handleClick}/>
                    </GridListTile>
                })}
            </GridList>
        </ChartFrame>
        <Modal open={open} onClose={handleClose}>
            <Window variant="outlined">
                <Chart gridArea="middle" data={props.data} width={350} height={350}
                       solution={props.solutions ? props.solutions[solutionId] : undefined}/>
            </Window>
        </Modal>
    </>
}