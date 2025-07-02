document.addEventListener("DOMContentLoaded", () => {
    const chart = echarts.init(document.getElementById("main"));

    fetch("/data/getAllCarSales")
        .then(res => res.json())
        .then((data) => {
            chart.setOption({
                tooltip: {},
                series: [{
                    type: 'wordCloud',
                    gridSize: 4,
                    sizeRange: [20, 80],
                    rotationRange: [-90, 90],
                    shape: 'pentagon',
                    width: '100%',
                    height: '100%',
                    textStyle: {
                        fontFamily: 'Microsoft YaHei',
                        fontWeight: 'bold',
                        color: function () {
                            return 'rgb(' +
                                [Math.round(Math.random() * 150 + 50),
                                Math.round(Math.random() * 150 + 50),
                                Math.round(Math.random() * 150 + 50)
                                ].join(',') + ')';
                        }
                    },
                    emphasis: {
                        focus: 'self',
                        textStyle: {
                            textShadowBlur: 10,
                            textShadowColor: '#333'
                        }
                    },
                    data: data
                }]
            });

            window.addEventListener("resize", () => chart.resize());
        })
        .catch(err => {
            console.error("加载词云失败:", err);
            alert("词云加载失败，请检查接口数据");
        });
});
