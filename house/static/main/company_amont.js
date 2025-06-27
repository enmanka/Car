(function (func) {
    $.ajax({
        url: "/data/getCompanyAmont",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChart = echarts.init(document.getElementById('chart_16'), 'infographic');

    var option = {
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        calculable: true,
        series: [
            {
                name: '资金保有量',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: data.series
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});