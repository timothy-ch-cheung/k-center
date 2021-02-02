import * as d3 from "d3";
import {radiusToPixels} from "../chart/D3Chart";

const D3ChartPreview = {}
let chart

const margin = {top: 5, right: 5, bottom: 5, left: 5};

D3ChartPreview.create = function (props) {
    chart = d3.select(`.preview_${props.id}`)
        .attr('width', props.width)
        .attr('height', props.height)
        .append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`);
}


D3ChartPreview.update = function (props) {
    const circleSize = props.data.length > 150 ? 1 : 2
    chart = d3.select(`.preview_${props.id}`)
    d3.selectAll(`.preview_${props.id} .circle`).remove();
    d3.selectAll(`.preview_${props.id} .radii`).remove();

    const x = d3.scaleLinear()
        .range([0, props.width]);

    const y = d3.scaleLinear()
        .range([props.height, 0]);

    const minDomain = Math.min(d3.min(props.data, (d) => d.y), d3.min(props.data, (d) => d.x))
    const maxDomain = Math.max(d3.max(props.data, (d) => d.y), d3.max(props.data, (d) => d.x))
    const min = minDomain - (maxDomain * 0.75)
    const max = maxDomain + (maxDomain * 0.75)
    console.log("min " + min + " " + minDomain)
    console.log("max " + max + " " + maxDomain)

    x.domain([min, max]);
    y.domain([min, max]);

    props.solution && chart.selectAll('.radii')
        .data(props.solution.centers)
        .enter().append('circle')
        .attr('class', 'radii')
        .attr('cx', (d) => x(d.x))
        .attr('cy', (d) => y(d.y))
        .attr('r', radiusToPixels(props.width, maxDomain, props.solution.radius))
        .style("stroke", "black")
        .style('fill', 'none');

    chart.selectAll('.circle')
        .data(props.data)
        .enter().append('circle')
        .attr('class', (d) => `circle ${d.colour} ${d.center ? 'center' : ''}`)
        .attr('cx', (d) => x(d.x))
        .attr('cy', (d) => y(d.y))
        .attr('r', circleSize)
        .style('fill', (d) => d.colour);
}

export default D3ChartPreview;