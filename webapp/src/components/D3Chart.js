import * as d3 from "d3";

const D3Chart = {}
let chart

const margin = {top: 40, right: 20, bottom: 60, left: 60};
const legendWidth = 100;

const radiusToPixels = (chartSize, maxDomain, radius) => (chartSize / maxDomain) * radius

D3Chart.create = function (props) {
    chart = d3.select(".chart")
        .attr('width', props.width + margin.left + margin.right + legendWidth)
        .attr('height', props.height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`);
}

D3Chart.update = function (props) {
    const x = d3.scaleLinear()
        .range([0, props.width]);

    const y = d3.scaleLinear()
        .range([props.height, 0]);

    const maxDomain = Math.max(d3.min(props.chart.data, (d) => d.y), d3.max(props.chart.data, (d) => d.x)) * 1.25

    x.domain([0, maxDomain]);
    y.domain([0, maxDomain]);

    chart.append('g')
        .attr('transform', `translate(0,${props.height})`)
        .call(d3.axisBottom(x).tickValues([1].concat(x.ticks())));

    chart.append('text')
        .attr('transform', `translate(${props.width / 2},${props.height + margin.top})`)
        .attr('id', 'x-label')
        .text('X');

    chart.append('g')
        .call(d3.axisLeft(y).tickValues([1].concat(y.ticks())));

    chart.append('text')
        .attr('transform', 'rotate(-90)')
        .attr('dx', `-${props.height / 2}`)
        .attr('dy', '-1.5em')
        .text('Y');

    chart.selectAll('.radii')
        .data(props.chart.data)
        .enter().append('circle')
        .attr('class', 'radii')
        .attr('cx', (d) => x(d.x))
        .attr('cy', (d) => y(d.y))
        .attr('r', radiusToPixels(props.width, maxDomain, props.chart.centerRadius))
        .style("stroke", (d) => d.center ? "black" : "none")
        .style('fill', 'none');

    chart.selectAll('.circle')
        .data(props.chart.data)
        .enter().append('circle')
        .attr('class', 'circle')
        .attr('cx', (d) => x(d.x))
        .attr('cy', (d) => y(d.y))
        .attr('r', 5)
        .style('fill', (d) => d.colour === "RED" ? '#C13522' : '#225FC1');

    drawTooltips(props.chart.data);
    drawLegend(props)
}

function drawTooltips(data) {
    const tooltip = d3.select('.tooltip');

    chart.selectAll('.circle')
        .data(data)
        .on('mouseover', (event, d) => {
            tooltip.transition()
                .duration(100)
                .style('opacity', .9);
            tooltip.text(`(x: ${d.y}, y: ${d.x}) Class: ${d.colour}`)
                .style('left', `${event.pageX + 5}px`)
                .style('top', `${event.pageY - 20}px`);
        })
        .on('mouseout', () => {
            tooltip.transition()
                .duration(400)
                .style('opacity', 0);
        });
}

function drawLegend(props) {
    chart.append("rect")
        .attr('x', props.width + 20)
        .attr('y', 20)
        .attr('width', '20')
        .attr('height', '10')
        .style('fill', "LightSlateGray")
        .style('outline', "solid 1px Black")
        .on("click", () => {
                let currentOpacity = d3.selectAll(".radii").style("opacity")
                d3.selectAll(".radii").transition().style("opacity", currentOpacity == 1 ? 0 : 1)
            }
        );

    chart.append("text")
        .attr('x', props.width + 45)
        .attr('y', 28)
        .style('font-size', "10px")
        .text('Toggle Centers')
}

export default D3Chart;