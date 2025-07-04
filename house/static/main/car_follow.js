// 定义全局图表变量
var carSalesChart = null;

// 主函数：初始化图表和事件监听
function initCarSalesModule() {
    // 初始化图表（加载所有车系总销量数据）
    fetchCarSalesData();
}

// 数据获取函数
function fetchCarSalesData() {
    $.ajax({
        url: "/data/getCarFollow",
        type: "GET",
        dataType: "json",
        beforeSend: function () {
            // 可以在这里添加加载状态
            if (carSalesChart) {
                carSalesChart.showLoading({
                    text: '数据加载中...',
                    color: '#4a90e2',
                    textColor: '#fff',
                    maskColor: 'rgba(0, 0, 0, 0.8)',
                    zlevel: 0
                });
            }
        },
        success: function (data) {
            console.log('获取到的数据:', data);
            if (Array.isArray(data) && data.length > 0) {
                renderCarSalesChart(data);
            } else {
                console.error('获取的数据为空或格式不正确');
            }
        },
        error: function (xhr, status, error) {
            console.error("数据加载失败:", error);
            // 可以在这里添加错误提示
        },
        complete: function () {
            if (carSalesChart) {
                carSalesChart.hideLoading();
            }
        }
    });
}

// 图表渲染函数
function renderCarSalesChart(data) {
    const chartDom = document.getElementById('car_sales');
    console.log('获取到的 chartDom:', chartDom);
    if (!chartDom) {
        console.error('未找到 id 为 car_sales 的 DOM 元素');
        return;
    }
    const myChart = echarts.init(chartDom, null, {
        renderer: 'webgl',
        useDirtyRect: false
    });

    // 数据处理
    const xData = data.map(item => item.car_name);
    const yData = data.map(item => item.city_range);
    const zData = data.map(item => item.follow);

    data.forEach(item => {
        xData.push(item.car_name);
        yData.push(item.city_range);
        zData.push(item.follow);
    });

    // 去重并排序
    const uniqueXData = [...new Set(xData)].sort();
    const uniqueYData = [...new Set(yData)].sort();

    const seriesData = [];
    for (let i = 0; i < xData.length; i++) {
        const xIndex = uniqueXData.indexOf(xData[i]);
        const yIndex = uniqueYData.indexOf(yData[i]);
        seriesData.push([xIndex, yIndex, zData[i]]);
    }

    // 定义更鲜艳的柱状图渐变颜色
    const barColor = new echarts.graphic.LinearGradient(
        0, 0, 0, 1,
        [
            { offset: 0, color: '#FF5733' },
            { offset: 0.5, color: '#33FF57' },
            { offset: 1, color: '#5733FF' }
        ],
        false
    );

    const option = {
        title: {
            text: '不同车型在不同城市的关注度',
            left: 'center',
            textStyle: {
                color: '#fff',
                fontSize: 28,
                fontWeight: 'bold',
                textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)'
            }
        },
        visualMap: {
            max: Math.max(...zData),
            inRange: {
                color: [
                    '#313695',
                    '#4575b4',
                    '#74add1',
                    '#abd9e9',
                    '#e0f3f8',
                    '#ffffbf',
                    '#fee090',
                    '#fdae61',
                    '#f46d43',
                    '#d73027',
                    '#a50026'
                ]
            }
        },
        tooltip: {
            trigger: 'item',
            formatter: function (params) {
                if (params && params.data && params.data.length >= 3) {
                    const param = params;
                    return `车型: ${uniqueXData[param.data[0]]} <br/>城市: ${uniqueYData[param.data[1]]} <br/>关注度: ${param.data[2]} `;
                } else {
                    return '暂无数据';
                }
            },
            backgroundColor: 'rgba(0, 0, 0, 0.9)',
            textStyle: {
                color: '#fff',
                fontSize: 14
            },
            borderColor: '#4a90e2',
            borderWidth: 2,
            extraCssText: 'box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);'
        },
        xAxis3D: {
            name: '车型',
            type: 'category',
            data: uniqueXData,
            position: 'left',
            axisLabel: {
                color: '#fff',
                rotate: 45,
                interval: 0,
                fontSize: 14,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 5
            },
            axisLine: {
                lineStyle: {
                    color: '#fff',
                    width: 2
                }
            },
            axisTick: {
                show: false
            }
        },
        yAxis3D: {
            name: '城市',
            type: 'category',
            data: uniqueYData,
            position: 'left',
            axisLabel: {
                color: '#fff',
                fontSize: 16,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 5
            },
            axisLine: {
                lineStyle: {
                    color: '#fff',
                    width: 2
                }
            },
            axisTick: {
                show: false
            }
        },
        zAxis3D: {
            type: 'value',
            name: '关注度',
            nameLocation: 'middle',
            nameGap: 40,
            nameTextStyle: {
                color: '#fff',
                fontSize: 16,
                fontWeight: 'bold'
            },
            axisLabel: {
                color: '#fff',
                formatter: '{value}',
                fontSize: 14,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 5
            },
            axisLine: {
                lineStyle: {
                    color: '#fff',
                    width: 2
                }
            },
            axisTick: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.2)',
                    type: 'dashed'
                }
            }
        },
        grid3D: {
            boxWidth: 300,
            boxDepth: 120,
            viewControl: {
                alpha: 30,
                beta: 40,
                distance: 150
            },
            light: {
                main: {
                    intensity: 1.8,
                    shadow: true,
                    color: '#fff'
                },
                ambient: {
                    intensity: 0.5
                }
            }
        },
        series: [{
            type: 'bar3D',
            data: seriesData,
            itemStyle: {
                color: barColor,
                borderWidth: 2,
                borderColor: 'rgba(255, 255, 255, 0.8)',
                opacity: 0.4
            },
            barSize: 13,
            shading: 'color',
            emphasis: {
                itemStyle: {
                    color: 'rgba(200,0,0,1)',
                    borderWidth: 3,
                    borderColor: '#fff',
                    opacity: 0.9
                },
                label: {
                    show: true,
                    color: '#900',
                    fontSize: 20,
                    textShadow: '2px 2px 4px rgba(0, 0, 0, 0.5)'
                }
            },
            animationDuration: 1500,
            animationEasing: 'elasticOut'
        }]
    };

    console.log('ECharts 配置项:', option);
    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }

    // 响应窗口变化
    window.addEventListener('resize', function () {
        myChart.resize();
    });

    carSalesChart = myChart;
}

// 页面加载完成后初始化模块
document.addEventListener('DOMContentLoaded', initCarSalesModule);