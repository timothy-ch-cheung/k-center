import styled from "@emotion/styled";
import {Divider} from "@material-ui/core";

export const H3 = styled("h3")`
    margin: 5px 10px;
`

export const SectionDivider = styled(Divider)`
    margin-bottom: 10px;
`

interface Spacing {
    height?: number
}
export const Spacer = styled("div")`
    height: ${(props: Spacing) => {return props.height? props.height: 15}}px;
`

export const HorizontalGroup = styled("div")`
    display: flex;
    justify-content: space-between;
`