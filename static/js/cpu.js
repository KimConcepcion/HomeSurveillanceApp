var ctx = document.getElementById('cpu_chart');
ctx.style.backgroundColor = '#FFFFFF';

let cpu_chart = new Chart(ctx, {
  type: 'dognut',
  data: {
    labels: [1],
    datasets: [
      {
        label: "CPU Performance",
        data: [cpu_data],
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