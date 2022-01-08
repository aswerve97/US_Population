document.forms['query'].addEventListener('submit', (event) => {
    event.preventDefault();
    fetch(event.target.action, {
        method: 'POST',
        body: new URLSearchParams(new FormData(event.target))
    }).then((resp) => {
        return resp.json();
    }).then((body) => {
        renderChart(body);
    }).catch((error) => {
        console.log("Response failed: " + event.error)
    });
});

function renderChart(predictedPop) {
    let chartCanvas = document.getElementById('usPopulation');
    let popChart = Chart.getChart("usPopulation"); 
    
    if(typeof popChart !== 'undefined') {
        popChart.data.datasets[0].data = predictedPop;
        popChart.update()
    }
    
    else {
        let myChart = new Chart(chartCanvas, {
            type: 'line',
            data: {
                datasets: [{
                label: 'Predicted US population',
                data: predictedPop,
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
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