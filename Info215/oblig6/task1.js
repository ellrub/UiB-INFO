import * as d3 from "d3";

let dataset = [5, 10, 15, 20, 25];
    let w = 200;
    let h = 100;
    let barPadding = 1;

    let svg = d3.select("body")
        .append("svg")
        .attr("width", w)
        .attr("height", h);

    svg.selectAll("rect")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("x", function(d, i) {
        return i * (w / dataset.length);
        })

        .attr("y", function(d) {
        return h - d*4; //Height minus data value
        })

        .attr("width", w / dataset.length - barPadding)
        .attr("height", function(d) {
        return d*4; //Just the data value
        })

        .attr("fill", function(d) { return "rgb(0, 0, " + (d * 10) + ")"; });

// // Declare the chart dimensions and margins.
// const width = 640;
// const height = 400;
// const marginTop = 20;
// const marginRight = 20;
// const marginBottom = 30;
// const marginLeft = 40;

// // Declare the x (horizontal position) scale.
// const x = d3.scaleUtc()
//     .domain([new Date("2023-01-01"), new Date("2024-01-01")])
//     .range([marginLeft, width - marginRight]);

// // Declare the y (vertical position) scale.
// const y = d3.scaleLinear()
//     .domain([0, 100])
//     .range([height - marginBottom, marginTop]);

// // Create the SVG container.
// const svg = d3.create("svg")
//     .attr("width", width)
//     .attr("height", height);

// // Add the x-axis.
// svg.append("g")
//     .attr("transform", `translate(0,${height - marginBottom})`)
//     .call(d3.axisBottom(x));

// // Add the y-axis.
// svg.append("g")
//     .attr("transform", `translate(${marginLeft},0)`)
//     .call(d3.axisLeft(y));

// // Return the SVG element.
// return svg.node();
