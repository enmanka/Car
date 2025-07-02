document.addEventListener('DOMContentLoaded', function () {
    const wordChart = echarts.init(document.getElementById('main'));
    const barChart = echarts.init(document.getElementById('bar-chart'));
    const monthSelect = document.getElementById('month-select');

    function loadWordCloudData(month = 'all') {
        const url = month === 'all'
            ? '/data/getAllCarSales'
            : `/data/getCarSalesByMonth?month=${month}`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                // 渲染词云图
                const wordOption = {
                    backgroundColor: '#000',
                    tooltip: {
                        show: true,
                        formatter: function (params) {
                            return `${params.name}：${params.value} 辆`;
                        }
                    },
                    series: [{
                        type: 'wordCloud',
                        shape: 'circle',
                        gridSize: 2,
                        sizeRange: [15, 80],
                        rotationRange: [-45, 45],
                        drawOutOfBound: true,
                        width: '100%',
                        height: '100%',
                        textStyle: {
                            color: function () {
                                return 'rgb(' + [
                                    Math.round(Math.random() * 200),
                                    Math.round(Math.random() * 200),
                                    Math.round(Math.random() * 200)
                                ].join(',') + ')';
                            }
                        },
                        emphasis: {
                            textStyle: {
                                shadowBlur: 10,
                                shadowColor: '#fff'
                            }
                        },
                        data: data
                    }]
                };
                wordChart.setOption(wordOption);

                // 构建柱状图（取前五）
                const top5 = [...data]
                    .sort((a, b) => b.value - a.value)
                    .slice(0, 5);

                const barOption = {
                    backgroundColor: '#000',
                    title: {
                        text: '销量前五品牌',
                        left: 'center',
                        top: 10,
                        textStyle: {
                            color: '#fff',
                            fontSize: 18
                        }
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: { type: 'shadow' }
                    },
                    grid: {
                        top: 60,
                        left: '15%',
                        right: '10%',
                        bottom: '10%'
                    },
                    xAxis: {
                        type: 'value',
                        axisLabel: { color: '#fff' },
                        splitLine: { lineStyle: { color: '#333' } }
                    },
                    yAxis: {
                        type: 'category',
                        data: top5.map(item => item.name),
                        axisLabel: { color: '#fff' }
                    },
                    series: [{
                        name: '销量',
                        type: 'bar',
                        data: top5.map(item => item.value),
                        barWidth: '60%',
                        label: {
                            show: true,
                            position: 'right',
                            distance: 5,
                            color: '#fff',
                            formatter: (params) => {
                                const rank = params.dataIndex + 1;
                                return `{rank|No.${rank}} ${params.data}`;
                            },
                            rich: {
                                rank: {
                                    color: '#FFD700',
                                    backgroundColor: '#333',
                                    padding: [2, 4],
                                    borderRadius: 3,
                                    fontSize: 12,
                                    fontWeight: 'bold'
                                }
                            }
                        },
                        itemStyle: {
                            color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [
                                { offset: 0, color: '#00c6ff' },
                                { offset: 1, color: '#0072ff' }
                            ])
                        }
                    }]
                };

                barChart.setOption(barOption);
            })
            .catch(error => {
                console.error('获取数据失败:', error);
            });
    }

    loadWordCloudData();

    monthSelect.addEventListener('change', function () {
        const selectedMonth = this.value;
        loadWordCloudData(selectedMonth);
    });

    window.addEventListener('resize', function () {
        wordChart.resize();
        barChart.resize();
    });
});
