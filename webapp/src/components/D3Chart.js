import * as d3 from "d3";

const EventEmitter = require('events').EventEmitter;

const D3Chart = {}

const margin = {top: 40, right: 20, bottom: 60, left: 60};

D3Chart.create = function (props) {
    const chart = d3.select(".chart")
        .attr('width', props.width + margin.left + margin.right)
        .attr('height', props.height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`);

    console.log(props)

    const x = d3.scaleLinear()
        .range([0, props.width]);

    const y = d3.scaleLinear()
        .range([props.height, 0]);

    const maxDomain = Math.max(d3.min(props.chart, (d) => d.y), d3.max(props.chart, (d) => d.x)) * 1.25
    const radiusToPixels = (radius) => (props.width/maxDomain)*radius

    x.domain([0,maxDomain]);
    y.domain([0,maxDomain]);

    chart.append('g')
        .attr('transform', `translate(0,${props.height})`)
        .style("stroke","black")
        .call(d3.axisBottom(x).tickValues([1].concat(x.ticks())));

    chart.append('text')
        .attr('transform', `translate(${props.width/2},${props.height + margin.top})`)
        .attr('id', 'x-label')
        .text('X');

    chart.append('g')
        .attr("class", "axis")
        .call(d3.axisLeft(y).tickValues([1].concat(y.ticks())));

    chart.append('text')
        .attr('transform', 'rotate(-90)')
        .attr('dx', '-10em')
        .attr('dy', '-1.5em')
        .text('Y');

    chart.selectAll('.radii')
        .data(props.chart)
        .enter().append('circle')
        .attr('class','radii')
        .attr('cx', (d) => x(d.x))
        .attr('cy', (d) => y(d.y))
        .attr('r', radiusToPixels(0.854))
        .style("stroke", (d) => d.center ? "black" : "none")
        .style('fill', 'none');

    chart.selectAll('.circle')
        .data(props.chart)
        .enter().append('circle')
        .attr('class','circle')
        .attr('cx', (d) => x(d.x))
        .attr('cy', (d) => y(d.y))
        .attr('r', 5)
        .style('fill', (d) => d.colour === "RED" ? '#C13522' : '#225FC1')
}

export default D3Chart;