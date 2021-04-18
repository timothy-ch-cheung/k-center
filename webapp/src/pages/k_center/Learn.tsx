import {Container, HomeIcon} from "../index/App";
import React from "react";
import {IconButton} from "@material-ui/core";
import {useHistory} from "react-router-dom";
import {Carousel} from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css"
import k_center_initial from "../../assets/1a_initial_points.png"
import k_center_task from "../../assets/1b_k_center_task.png"
import k_center_solution from "../../assets/1c_k_center_solution.png"
import rk_center_initial from "../../assets/2a_robust_k_center_initial.png"
import rk_center_task from "../../assets/2b_robust_k_center_task.png"
import rk_center_solution from "../../assets/2c_robust_k_center_solution.png"
import ck_center_label from "../../assets/3a_colourful_points.png"
import rkck_solution from "../../assets/3b_colourful_robust_solution.png"
import ck_center_task from "../../assets/3c_colourful_task.png"
import ck_center_solution from "../../assets/3d_colourful_solution.png"
import styled from '@emotion/styled'

interface Slide {
    img: string
    title: string
    description: string
}

const Title = styled("h1")`
  color: white;
  margin-bottom: 5px;
  margin-top: 5px;
`

const Description = styled("p")`
  color: white;
  font-size: 1vw;
  margin-bottom: 5px;
  height: 3vh;
`

const UnselectableDiv = styled("div")`
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
`

function Learn() {
    const history = useHistory();

    const handleBackButtonClick = () => {
        history.push('/')
    }

    const slides: Array<Slide> = [
        {
            img: k_center_initial, title: "What is the k-center problem?", description: `Imagine you are planning a city 
        with a parcel delivery network and the points represent potential locations for residents or warehouses. 
        The parcels will be delivered from the warehouse closest to the resident.`
        },
        {
            img: k_center_initial, title: "What are the k-center problem?", description: `What is the best locations to build 
        warehouses such that the distance a delivery driver must travel is minimised? Another way to state this is 
        where should  warehouses be built such that the maximum distance between a resident and their nearest warehouse 
        is minimised?`
        },
        {
            img: k_center_task, title: "The constraint k", description: `What if the budget was limited
        and you only have enough money to build k warehouses? For example, what if your budget limited you to building 
        two warehouses, where should they be located?`
        },
        {
            img: k_center_solution, title: "This is the k-center problem.", description: `Finding out the optimal location
         for the warehouses is the same as solving the k-center problem. The answer is shown below, with the green arrow
          showing the cost of the solution.`
        },
        {
            img: rk_center_initial, title: "An intermediate problem", description: `You would like to ensure the 
            majority of people get their parcels quickly. What if we wanted to exclude few people living in the 
            countryside (highlighted in green box) since servicing these people leads to awkward warehouse locations 
            causing many people in the inner city to receive poor service?`
        },
        {
            img: rk_center_task, title: "An intermediate problem", description: `Therefore we might only want to 
        consider a certain percentage of residents when considering warehouse locations to serve the majority rather
        than the few. In our example lets say we want to consider at least 62.5% of residents.`
        },
        {
            img: rk_center_solution, title: "The Robust k-center problem", description: `This is called the Robust 
            k-center problem. Notice in the answer shown below, the green arrow showing the solution cost is shorter, 
            but two residents are excluded (this doesn't necessarily mean we don't deliver to them, we just don't 
            prioritise them).`
        },
        {
            img: k_center_initial, title: "Applying this to a new scenario", description: `Instead of allocating 
            warehouse locations for a delivery service what if were allocating hospitals with ambulance depots? We would 
            like to have the ambulances arrive to houses as fast as possible.`
        },
        {
            img: ck_center_label, title: "Demographics of the residents", description: `Assume we have some 
            knowledge about the residents. For example, people aged over 60 tend to live in the countryside and they 
            are more likely to require an ambulance due to higher likelihood of health complications. We can label
            the two groups as blue and red.`
        },
        {
            img: rkck_solution, title: "The robust k-center bias", description: `The solution provided by the
            robust k-center problem would exclude people over 60 even though they need the service more.`
        },
        {
            img: ck_center_task, title: "Taking prior knowledge into account", description: `We can label residents
            over 60 as red and residents under 60 as blue. We then ask what is the best allocation of hospitals to cover
            62.5% of residents such that all red residents are covered?`
        },
        {
            img: ck_center_solution, title: "The colourful k-center problem", description: `This is the colourful 
            k-center problem. The red and blue parameters allow us to control for bias when selecting the hospital
            locations.`
        }
    ]

    return <Container>
        <div>
            <IconButton aria-label="back" onClick={handleBackButtonClick}>
                <HomeIcon fontSize="large"/>
            </IconButton>
        </div>
        <UnselectableDiv style={{width: "70%", margin: "0 auto"}} cy-data="carousel">
            <Carousel autoPlay={false} showThumbs={false}>
                {slides.map((slide, index) => {
                    return <div>
                        <Title>{slide.title}</Title>
                        <Description>{slide.description}</Description>
                        <img src={slide.img} style={{width:"80%"}}/>
                    </div>
                })}
            </Carousel>
        </UnselectableDiv>

    </Container>
}

export default Learn