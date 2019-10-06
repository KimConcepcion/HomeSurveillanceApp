var ctx_storage = document.getElementById('storage_chart');
ctx_storage.style.backgroundColor = '#FFFFFF';

let storage_chart = new Chart(ctx_storage, {
	type: 'pie',
	data: {
		datasets: [{
			label: "Memory Usage",
			data: [used_strg, free_strg],
			backgroundColor: [
				"#224B8B",
				"#0097FF",
			]
		}],
		labels: [
			'Used Storage [Gb]',
			'Free Storage [Gb]'
		]
	},
	options: {
		responsive: false
	}
})