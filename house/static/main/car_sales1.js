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
    var chartDom = document.getElementById('car_sales');

    // 初始化图表（如果尚未初始化）
    if (!carSalesChart) {
        carSalesChart = echarts.init(chartDom, 'infographic');

        // 响应窗口变化
        window.addEventListener("resize", function () {
            carSalesChart.resize();
        });
    }

    // 数据处理
    var pieData = data.map(item => {
        return {
            name: item.car_name,
            value: item.total_sales
        };
    });

    // 配置项
    var option = {
        title: {
            text: '不同车系总销量占比',
            left: 'center',
            textStyle: {
                color: '#fff',
                fontSize: 16
            }
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
            orient: 'vertical',
            right: 300,
            top: 'center',
            textStyle: {
                color: '#fff'
            }
        },
        series: [{
            name: '销量占比',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
                borderRadius: 5,
                borderColor: '#0f2453',
                borderWidth: 2
            },
            label: {
                show: true,
                formatter: '{b}: {c}',
                color: '#fff'
            },
            emphasis: {
                label: {
                    show: true,
                    fontSize: '18',
                    fontWeight: 'bold'
                }
            },
            labelLine: {
                show: true
            },
            data: pieData
        }]
    };

    // 应用配置
    carSalesChart.setOption(option);
}

// 页面加载完成后初始化模块
document.addEventListener('DOMContentLoaded', initCarSalesModule);