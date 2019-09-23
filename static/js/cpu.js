var ctx = document.getElementById('cpu_chart');
ctx.style.backgroundColor = '#FFFFFF';

let cpu_chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [10,20,30,40,50,60,70,80,90,100],
    datasets: [
      {
        label: "CPU Average Load",
        data: [11,23,34,42,56,66,72,81,93,109],
        borderColor: "#3cba9f",
        fill: false
      }
    ]
  },
  options: {
    responsive: false,
    maintainAspectRatio: false,
    scales: {
      xAxes: [{
        scaleLabel: {
          display: true,
          labelString: "Time [s]"
        }
      }]
    }
  }
})
