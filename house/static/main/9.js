// 颜色映射
const colorMap = {
    jiaoche: '#ff9f7f',
    mpv: '#37a2da',
    suv: '#32c5e9',
    xinnengyuan: '#9fe6b8'
};

// 车辆类型
const types = ['jiaoche', 'mpv', 'suv'];

// 初始化 ECharts 图表
const chartDom = document.getElementById('main');
const myChart = echarts.init(chartDom);

// 全局 option
let option = {
    backgroundColor: '#000',
    tooltip: {
        formatter: function (params) {
            return `${params.name}<br>销量: ${params.value}辆`;
        }
    },
    series: [
        {
            type: 'graph',
            layout: 'force',
            roam: true,
            draggable: true,
            focusNodeAdjacency: true, // 鼠标悬停时高亮相邻节点
            label: {
                show: true,
                color: '#fff'
            },
            force: {
                repulsion: 150,
                edgeLength: [50, 200],
                gravity: 0.1
            },
            data: [],
            links: [],
            lineStyle: {
                color: 'source',
                curveness: 0.3,
                opacity: 0.5
            },
            emphasis: {
                lineStyle: {
                    width: 2
                }
            }
        }
    ]
};

// 加载数据并构建图表
async function loadGraph() {
    const month = document.getElementById('monthSelector').value;
    const allData = await fetchCarData(month);
    const graphData = buildGraphData(allData);

    option.series[0].data = graphData.nodes;
    option.series[0].links = graphData.links;
    myChart.setOption(option);
}

// 获取所有类型的前5数据
async function fetchCarData(month) {
    const allData = {};
    for (const type of types) {
        const res = await fetch(`/data/getCarSalesByMonthAndType?type=${type}&month=${month}`);
        const raw = await res.json();
        allData[type] = raw
            .sort((a, b) => b.sales - a.sales)
            .slice(0, 5)
            .map((item, index) => ({
                name: item.car_name,
                value: item.sales,
                type: type,
                symbolSize: 60 - index * 5,
                itemStyle: {
                    color: colorMap[type]
                }
            }));
    }
    return allData;
}

// 构建节点与关系
function buildGraphData(allData) {
    const nodes = [];
    const links = [];

    // 添加节点
    types.forEach(type => {
        nodes.push(...allData[type]);
    });

    // 同组连接（组内 top5 构成闭合圈）
    types.forEach(type => {
        const group = allData[type];
        const len = group.length;
        for (let i = 0; i < len; i++) {
            links.push({
                source: group[i].name,
                target: group[(i + 1) % len].name  // 最后一个连回第一个
            });
        }
    });

    // 组间连接（各类型相同排名连接）
    for (let rank = 0; rank < 1; rank++) {
        const nodesAtRank = types.map(type => allData[type][rank]).filter(Boolean);
        for (let i = 0; i < nodesAtRank.length; i++) {
            for (let j = i + 1; j < nodesAtRank.length; j++) {
                links.push({
                    source: nodesAtRank[i].name,
                    target: nodesAtRank[j].name
                });
            }
        }
    }

    return { nodes, links };
}

// // 点击节点只显示相关节点与连接
// myChart.on('click', function (params) {
//     if (params.dataType === 'node') {
//         const selectedName = params.data.name;

//         const connectedLinks = option.series[0].links.filter(link =>
//             link.source === selectedName || link.target === selectedName
//         );

//         const relatedNodes = new Set();
//         connectedLinks.forEach(link => {
//             relatedNodes.add(link.source);
//             relatedNodes.add(link.target);
//         });

//         const filteredNodes = option.series[0].data.filter(node =>
//             relatedNodes.has(node.name)
//         );

//         myChart.setOption({
//             series: [{
//                 ...option.series[0],
//                 data: filteredNodes,
//                 links: connectedLinks
//             }]
//         });
//     }
// });

// 页面首次加载图表（默认1月）
window.onload = () => {
    document.getElementById('monthSelector').value = '01';
    loadGraph();
};
document.getElementById('monthSelector').addEventListener('change', loadGraph);
