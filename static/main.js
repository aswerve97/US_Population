document.forms['query'].addEventListener('submit', (event) => {
    event.preventDefault();
    fetch(event.target.action, {
        method: 'POST',
        body: new URLSearchParams(new FormData(event.target))
    }).then((resp) => {
        return resp.json();
    }).then((body) => {
        let actualPop = getActualPopulation();
        renderChart(body, actualPop);
    }).catch((error) => {
        console.log('Response failed: ' + error);
    });
});

document.forms[('query')].addEventListener('input', (event) => {
    yearInput();
});

function sendRequest() {
    fetch('/date', {
        method: 'POST',
        body: new URLSearchParams(new FormData(document.forms['query']))
    }).then((resp) => {
        return resp.json();
    }).then((body) => {
        let actualPop = getActualPopulation();
        renderChart(body, actualPop);
    }).catch((error) => {
        console.log('Response failed: ');
    });
}

function yearInput() {
    const startYearElem = document.getElementById('start_year');
    const endYearElem = document.getElementById('end_year');

    startYear = parseInt(startYearElem.value);
    endYear = parseInt(endYearElem.value);
    if ((endYear && startYear) && validateYear(startYear, 1900, endYear)) {
        sendRequest();
    }
}

//Checks if year is between bounds, and if it is either 20th or 21st century 
function validateYear(year, lower, upper) {
    return ((lower <= year)
        && (year <= upper)
        && (/^(19|20)\d{2}$/.test(upper.toString()))
    );
}

async function getActualPopulation() {
    let response = await fetch('/actualPop');
    return response.json();
}

function updateChart(newData, chart, pos) {
    chart.data.datasets[pos].data = newData;
    chart.update();
}

function filterActualPopulation(pop) {
    let popChart = Chart.getChart('usPopulation');
    let years = Object.keys(popChart.data.datasets[0].data);
    let startYear = years[0];
    let endYear = (years[[years.length - 1]] > 2000) ? 2000 : years[[years.length - 1]];
    let newPop = {};

    for (let key in pop) {
        if ((parseInt(startYear) <= parseInt(key)) && (parseInt(key) <= parseInt(endYear))) {
            Object.assign(newPop, { [key]: pop[key] });
        }
    }
    updateChart(newPop, popChart, 1);
}

function renderChart(predictedPop, actualPop) {
    let chartCanvas = document.getElementById('usPopulation');
    const popChart = Chart.getChart('usPopulation');

    if (typeof popChart !== 'undefined') {
        updateChart(predictedPop, popChart, 0);
        actualPop.then((pop) => {
            filterActualPopulation(pop);
        })
    }

    else {
        let myChart = new Chart(chartCanvas, {
            type: 'line',
            data: {
                datasets: [
                    {
                        label: 'Predicted US population',
                        data: predictedPop,
                        fill: false,
                        borderColor: 'rgb(0,255,0)',
                        tension: 0.1
                    },
                    {
                        label: 'Actual US population',
                        data: actualPop.then((pop) => {
                            filterActualPopulation(pop)
                        }),
                        fill: false,
                        borderColor: 'rgb(255,0,0)',
                        tension: 0.1
                    }]
            }
        });
    }
}