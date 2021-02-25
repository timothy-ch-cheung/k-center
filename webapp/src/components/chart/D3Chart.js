import * as d3 from "d3";

const D3Chart = {}
let chart

const margin = {top: 40, right: 20, bottom: 60, left: 60};
const legendWidth = 100;

export const radiusToPixels = (chartSize, maxDomain, radius) => (chartSize / maxDomain) * radius

D3Chart.create = function (props) {
    chart = d3.select(".chart")
        .attr('width', props.width + margin.left + margin.right + legendWidth)
        .attr('height', props.height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', `translate(${margin.left}, ${margin.top})`);
}

D3Chart.update = function (props) {
    const circleSize = props.data.length > 150 ? 2 : 5
    d3.selectAll('.chart .circle').remove();
    d3.selectAll('.chart .radii').remove();
    d3.selectAll('.chart .toggle-text').remove();
    d3.selectAll('.chart .toggle').remove();
    d3.selectAll('.chart .axis').remove();

    const x = d3.scaleLinear()
        .range([0, props.width]);

    const y = d3.scaleLinear()
        .range([props.height, 0]);

    const maxDomain = Math.max(d3.min(props.data, (d) => d.y), d3.max(props.data, (d) => d.x)) * 1.25

    x.domain([0, maxDomain]);
    y.domain([0, maxDomain]);

    chart.append('g')
        .attr('class', 'axis')
        .attr('transform', `translate(0,${props.height})`)
        .call(d3.axisBottom(x).tickValues([1].concat(x.ticks())));

    chart.append('text')
        .attr('transform', `translate(${props.width / 2},${props.height + margin.top})`)
        .attr('class', 'axis')
        .text('X');

    chart.append('g')
        .attr('class', 'axis')
        .call(d3.axisLeft(y).tickValues([1].concat(y.ticks())));

    chart.append('text')
        .attr('transform', 'rotate(-90)')
        .attr('class', 'axis')
        .attr('dx', `-${props.height / 2}`)
        .attr('dy', '-1.5em')
        .text('Y');

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

    drawTooltips(props.data);
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
            tooltip.text(`(x: ${d.x.toFixed(3)}, y: ${d.y.toFixed(3)}) Class: ${d.colour}`)
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
    drawCentersBoundaryToggle(props.width);
    drawHighlightCenterButton(props.width);
    drawClassToggles(props.data, props.width);
}

function drawCentersBoundaryToggle(chartWidth) {
    chart.append("rect")
        .attr('class', 'center-toggle')
        .attr('class', 'toggle')
        .attr('x', chartWidth + 20)
        .attr('y', 20)
        .attr('width', '20')
        .attr('height', '10')
        .style('fill', "LightSlateGray")
        .style('outline', "solid 1px Black")
        .on("click", () => {
                let radii = d3.selectAll(".radii")
                if (radii.size() != 0) {
                    let currentOpacity = radii.style("opacity")
                    d3.selectAll(".radii").transition().style("opacity", currentOpacity == 1 ? 0 : 1)
                    d3.select('.center-toggle').transition().style("opacity", currentOpacity == 1 ? 0.2 : 1)
                }
            }
        );

    chart.append("text")
        .attr('class', 'toggle-text')
        .attr('x', chartWidth + 45)
        .attr('y', 28)
        .style('font-size', "10px")
        .text('Toggle Centers')
}

function drawHighlightCenterButton(chartWidth) {
    chart.append("rect")
        .attr('class', 'center-toggle')
        .attr('class', 'toggle')
        .attr('x', chartWidth + 20)
        .attr('y', 40)
        .attr('width', '20')
        .attr('height', '10')
        .style('fill', "Purple")
        .style('outline', "solid 1px Black")
        .on("click", () => {
            d3.selectAll(".center")
                .transition().style("opacity", 0).duration(150)
                .transition().style("opacity", 1).duration(150)
                .transition().style("opacity", 0).duration(150)
                .transition().style("opacity", 1).duration(150);
        });

    chart.append("text")
        .attr('class', 'toggle-text')
        .attr('x', chartWidth + 45)
        .attr('y', 48)
        .style('font-size', "10px")
        .text('Highlight Centers')
}

function drawClassToggles(chartData, chartWidth) {
    let colours = Array.from(new Set(chartData.map(x => x.colour)));

    chart.selectAll(".legend")
        .data(colours)
        .enter()
        .append("g")
        .append("rect")
        .attr('class', (d) => `${d}-toggle`)
        .attr('class', 'toggle')
        .attr('x', chartWidth + 20)
        .attr('y', (d, i) => {
            return 80 + (i * 20)
        })
        .attr('width', '20')
        .attr('height', '10')
        .style('fill', (d) => d)
        .style('outline', "solid 1px Black")
        .on("click", (event, d) => {
                let currentOpacity = d3.selectAll("." + d).style("opacity")
                d3.selectAll("." + d).transition().style("opacity", currentOpacity == 1 ? 0 : 1)
                d3.select(`.${d}-toggle`).transition().style("opacity", currentOpacity == 1 ? 0.2 : 1)
            }
        );

    chart.selectAll(".legend")
        .data(colours)
        .enter()
        .append("text")
        .attr('class', 'toggle-text')
        .attr('x', chartWidth + 45)
        .attr('y', (d, i) => {
            return 88 + (i * 20)
        })
        .style('font-size', "10px")
        .text((d) => d);

}

export default D3Chart;