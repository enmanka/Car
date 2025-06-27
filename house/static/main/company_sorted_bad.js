(function (func) {
    $.ajax({
        url: "/data/getCompanySorted",
        type: "GET",
        data: {"order": 0},
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChart = echarts.init(document.getElementById('chart_14'), 'infographic');

    var option = {
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c}%"
        },
        calculable: true,
        series: [
            {
                name: '评分',
                type: 'funnel',
                x: '10%',
                y: 60,
                //x2: 80,
                y2: 60,
                width: '80%',
                // height: {totalHeight} - y - y2,
                min: 0,
                max: 150,
                minSize: '0%',
                maxSize: '100%',
                sort: 'ascending',
                gap: 10,
                itemStyle: {
                    normal: {
                        // color: 各异,
                        borderColor: '#fff',
                        borderWidth: 1,
                        label: {
                            show: true,
                            position: 'inside'
                            // textStyle: null      // 默认使用全局文本样式，详见TEXTSTYLE
                        },
                        labelLine: {
                            show: false,
                            length: 10,
                            lineStyle: {
                                // color: 各异,
                                width: 1,
                                type: 'solid'
                            }
                        }
                    },
                    emphasis: {
                        // color: 各异,
                        borderColor: 'red',
                        borderWidth: 5,
                        label: {
                            show: true,
                            formatter: '{b}:{c}%',
                            textStyle: {
                                fontSize: 20
                            }
                        },
                        labelLine: {
                            show: true
                        }
                    }
                },
                data: data.series
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});