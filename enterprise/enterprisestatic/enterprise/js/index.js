$(function() {
  "use strict";

  //MARKETING CHART
  var donut = new Morris.Donut({
    element: 'marketing-chart',
    resize: true,
    colors: ["#3c8dbc", "#f56954", "#00a65a"],
    data: [{
        label: "Download Sales",
        value: 12
      },
      {
        label: "In-Store Sales",
        value: 30
      },
      {
        label: "Mail-Order Sales",
        value: 20
      }
    ],
    hideHover: 'auto'
  });
  //TRAINING CHART
  var donut = new Morris.Donut({
    element: 'training-chart',
    resize: true,
    colors: ["#3c8dbc", "#f56954", "#00a65a"],
    data: [{
        label: "Download Sales",
        value: 12
      },
      {
        label: "In-Store Sales",
        value: 30
      },
      {
        label: "Mail-Order Sales",
        value: 20
      }
    ],
    hideHover: 'auto'
  });
  //EKONOMI CHART
  var donut = new Morris.Donut({
    element: 'ekonomi-chart',
    resize: true,
    colors: ["#3c8dbc", "#f56954", "#00a65a"],
    data: [{
        label: "Download Sales",
        value: 12
      },
      {
        label: "In-Store Sales",
        value: 30
      },
      {
        label: "Mail-Order Sales",
        value: 20
      }
    ],
    hideHover: 'auto'
  });
  //PERSONALIA CHART
  load_data()

  function load_data() {
    $.ajax({
      url: "/enterprise/getDataChart/", // the endpoint
      //type : "GET", // http method
      success: function(json) {
        console.log(json);
        var donut = new Morris.Donut({
          element: 'personalia-chart',
          resize: true,
          colors: ["#3c8dbc", "#f56954", "#00a65a", "#cede15"],
          data: [{
              label: "WB Aktif",
              value: json['personalia']['WB Aktif']
            },
            {
              label: "PRA A1 Aktif",
              value: json['personalia']['PRA A1 Aktif']
            },
            {
              label: "A1 Aktif",
              value: json['personalia']['A1 Aktif']
            },
            {
              label: "A2 Aktif",
              value: json['personalia']['A2 Aktif']
            }
          ],
          hideHover: 'auto'
        });
      },
    });
  }

});
