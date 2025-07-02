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
        url: "/data/getCarSales_All",
        type: "GET",
        dataType: "json",
        beforeSend: function () {
            // 可以在这里添加加载状态
            if (carSalesChart) {
                carSalesChart.showLoading();
            }
        },
        success: function (data) {
            renderCarSalesChart(data);
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
    const myChart = echarts.init(chartDom, null, {
        renderer: 'canvas',
        useDirtyRect: false
    });

    // 数据处理
    const xData = data.map(item => item.car_name);
    const yData = data.map(item => item.total_sales);

    // 定义柱状图渐变颜色
    const barColor = new echarts.graphic.LinearGradient(
        0, 0, 0, 1,
        [
            { offset: 0, color: '#66b3ff' },
            { offset: 1, color: '#2C58A6' }
        ]
    );

    const option = {
        title: {
            text: '不同车系总销量',
            left: 'center',
            textStyle: {
                color: '#fff',
                fontSize: 22,
                fontWeight: 'bold',
                textShadow: '2px 2px 4px rgba(0, 0, 0, 0.3)'
            }
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow',
                shadowStyle: {
                    color: 'rgba(0, 0, 0, 0.1)'
                }
            },
            formatter: '{b} : {c} 辆',
            backgroundColor: 'rgba(0, 0, 0, 0.8)',
            textStyle: {
                color: '#fff'
            },
            borderColor: 'rgba(255, 255, 255, 0.2)',
            borderWidth: 1
        },
        // legend: {
        //     data: ['销量'],
        //     textStyle: {
        //         color: '#fff'
        //     },
        //     bottom: 10
        // },
        xAxis: {
            type: 'category',
            data: xData,
            axisLabel: {
                color: '#fff',
                rotate: 45, // 旋转 x 轴标签
                interval: 0
            },
            axisLine: {
                lineStyle: {
                    color: '#fff'
                }
            },
            axisTick: {
                show: false
            }
        },
        yAxis: {
            type: 'value',
            // name: '销量',
            nameLocation: 'middle',
            nameGap: 40,
            axisLabel: {
                color: '#fff',
                formatter: '{value}'
            },
            axisLine: {
                lineStyle: {
                    color: '#fff'
                }
            },
            axisTick: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: 'rgba(255, 255, 255, 0.1)',
                    type: 'dashed'
                }
            }
        },
        series: [{
            name: '销量',
            type: 'bar',
            data: yData,
            itemStyle: {
                color: barColor,
                borderRadius: [5, 5, 0, 0] // 设置柱状图圆角
            },
            barWidth: '60%',
            emphasis: {
                itemStyle: {
                    color: '#4a90e2'
                }
            },
            animationDuration: 1000,
            animationEasing: 'cubicOut'
        }]
    };

    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }

    // 响应窗口变化
    window.addEventListener('resize', function () {
        myChart.resize();
    });
}

// 页面加载完成后初始化模块
document.addEventListener('DOMContentLoaded', initCarSalesModule);
document.addEventListener('DOMContentLoaded', initCarSalesModule);