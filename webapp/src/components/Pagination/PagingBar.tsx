import React from 'react';
import ArrowBackIosIcon from '@material-ui/icons/ArrowBackIos';
import ArrowForwardIosIcon from '@material-ui/icons/ArrowForwardIos';
import {IconButton, Typography} from "@material-ui/core";
import styled from "@emotion/styled";

interface Props {
    currentPage: number
    maxPage?: number
    isNextEnabled: boolean
    isPrevEnabled: boolean
    handlePrevClick: () => void
    handleNextClick: () => void
}

const ButtonGroup = styled("div")`
    display: flex;
    justify-content: space-between;
`

const Text = styled(Typography)`
    line-height: 2.6;
    font-size: 1.1rem;
`

export default function (props: Props) {
    return <ButtonGroup>
        <IconButton aria-label="back" disabled={!props.isPrevEnabled} onClick={props.handlePrevClick} cy-data="page-prev">
            <ArrowBackIosIcon/>
        </IconButton>
        <Text variant="button" display="block">
            Step {props.currentPage}/{props.maxPage && props.maxPage > 0 ? props.maxPage : "?"}
        </Text>
        <IconButton aria-label="forward" disabled={!props.isNextEnabled} onClick={props.handleNextClick} cy-data="page-next">
            <ArrowForwardIosIcon/>
        </IconButton>
    </ButtonGroup>
}