var myChart = echarts.init(document.getElementById('map1'));
// 指定图表的配置项和数据
option = {
   title: {
       text: '项目用例分布',
       x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    series : [
        {
            name: '用例分布',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[
                {value:335, name:'资产云'},
                {value:310, name:'IMAPP'},
                {value:234, name:'凯胜'},
                {value:135, name:'任务单'},
                {value:1548, name:'采购系统'}
            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
myChart.setOption(option);
var myChart1 = echarts.init(document.getElementById('map2'));
// 指定图表的配置项和数据
option = {
    title: {
       text: '用例分布',
       x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    series : [
        {
            name: '访问来源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:[
                {value:335, name:'资产云'},
                {value:310, name:'IMAPP'},
                {value:234, name:'凯胜'},
                {value:135, name:'任务单'},
                {value:1548, name:'采购系统'}
            ],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
// 使用刚指定的配置项和数据显示图表。
myChart1.setOption(option);
