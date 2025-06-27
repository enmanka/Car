(function (func) {
    $.ajax({
        url: "/data/getGongZuFang",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChart = echarts.init(document.getElementById('chart_12'), 'infographic');

    var option = {
        tooltip: {
            trigger: 'axis'
        },
        calculable: true,
        legend: {
            data: ['公租房数量', '平均面积']
        },
        xAxis: [
            {
                type: 'category',
                data: data.xAxis
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: '数量',
                axisLabel: {
                    formatter: '{value}'
                }
            },
            {
                type: 'value',
                name: '面积',
                axisLabel: {
                    formatter: '{value} '
                }
            }
        ],
        series: [

            {
                name: '公租房数量',
                type: 'bar',
                data: data.series1
            },
            {
                name: '平均面积',
                type: 'line',
                yAxisIndex: 1,
                data: data.series2
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});