var ctx_memory = document.getElementById('memory_chart');
ctx_memory.style.backgroundColor = '#FFFFFF';

let memory_chart = new Chart(ctx_memory,{
	type: 'bar',
	data: {
		labels: ["Available Memory", "Free Memory", "Used Memory"],
		datasets: [{
			label: "Virtual Memory Usage",
			data: [aval_mem, free_mem, used_mem],
	        backgroundColor: ["#F5C603", "#D62226", "#25D366"]
		}]
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
	            labelString: "Memory [MB]"
	          },
	          ticks: {
	        	  beginAtZero: true
	          }
	        }]
	    }
	}
})