document.forms['query'].addEventListener('submit', (event) => {
    event.preventDefault();
    fetch(event.target.action, {
        method: 'POST',
        body: new URLSearchParams(new FormData(event.target))
    }).then((resp) => {
        return resp.json();
    }).then((body) => {
        let actualPop = getActualPopulation();
        renderChart(body,actualPop);
    }).catch((error) => {
        console.log("Response failed: " + event.error)
    });
});

async function getActualPopulation() {
    let response = await fetch('/actualPop');
    return response.json(); 
}

function updateChart(newData, chart, pos){
    chart.data.datasets[pos].data = newData;
    chart.update()
}

function filterActualPopulation(pop){
    let popChart = Chart.getChart("usPopulation");
    let startYear = Object.keys(popChart.data.datasets[0].data)[0];
    let newPop = {};
    for(let key in pop){
        if(parseInt(key) >= parseInt(startYear)){
            Object.assign(newPop, {[key]: pop[key]});
        }
    }
    updateChart(newPop, popChart, 1);
}

function renderChart(predictedPop, actualPop) {
    let chartCanvas = document.getElementById('usPopulation');
    const popChart = Chart.getChart("usPopulation"); 
    
    if(typeof popChart !== 'undefined') {
        updateChart(predictedPop, popChart, 0);
        actualPop.then((pop)=>{
            filterActualPopulation(pop)            
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
                    data: actualPop.then((pop)=>{
                        filterActualPopulation(pop)
                    }),
                    fill: false,
                    borderColor: 'rgb(255,0,0)',
                    tension: 0.1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
}