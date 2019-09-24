var ctx = document.getElementById('cpu_chart');
ctx.style.backgroundColor = '#FFFFFF';

let cpu_chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [1,2,3,4,5],
    datasets: [
      {
        label: "CPU Average Load",
        data: [cpu_avg_load_0, cpu_avg_load_1, cpu_avg_load_2, cpu_avg_load_3, cpu_avg_load_4],
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
      }],
      yAxes: [{
          scaleLabel: {
            display: true,
            labelString: "Average Load [%]"
          },
          ticks: {
        	  max: 30
          }
        }]
    }
  }
})