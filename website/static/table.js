const ctx = document.getElementById("myChart");
const table = document.getElementById("table-responsive");
const updateButton = document.getElementById('plotUpdate');
const changeStsButton = document.getElementById('stsChange');


let newData = [[], [], []];
let myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: newData[0],
    datasets: [{
      data: newData[1],
      lineTension: 0,
      backgroundColor: 'transparent',
      borderColor: '#007bff',
      borderWidth: 4,
      pointBackgroundColor: '#007bff'
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: false
        }
      }]
    },
    legend: {
      display: false,
    }
  }
});

function api_get_update() {
  jQuery.get("../api/ai/", function( data ) {
    newData[0] = [];
    newData[1] = [];
    newData[2] = [];
    for (const item in data) {
      newData[0].push(data[item]['id']);
      newData[1].push(data[item]['current']);
      newData[2].push(data[item]['sts']);
    }
    newData[0].push(7);
    newData[1].push(2);
    newData[2].push(1);
  });
}

jQuery( document ).ready(function() {
  jQuery.get("../api/ai/", function( data ) {
    for (const item in data) {
      newData[0].push(data[item]['id']);
      newData[1].push(data[item]['current']);
      newData[2].push(data[item]['sts']);
    }
  });
});

updateButton.onclick = function () {
  api_get_update();
}
