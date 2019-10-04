var ctx_storage = document.getElementById('storage_chart');
ctx_storage.style.backgroundColor = '#FFFFFF';

let storage_chart = new Chart(ctx_storage, {
	type: 'pie',
	data: {
		datasets: [{
			label: "Memory Usage",
			data: [1, 2],
			backgroundColor: [
				"#224B8B",
				"#0097FF",
			]
		}],
		labels: [
			'Used Storage',
			'Free Storage'
		]
	},
	options: {
		responsive: false
	}
})