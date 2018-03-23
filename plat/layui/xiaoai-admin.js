layui.use(['element','table','jquery','laypage'], function(){
   var $ = layui.$ //重点处
  ,layer = layui.layer,
  element = layui.element,
  table = layui.table,
  laypage=layui.laypage;
    $(document).ready(function(){
      $("project").click(function(){
        $(this).hide();
      });
    });

   laypage.render({
    elem: 'demo7'
    ,count: 1
    ,layout: ['count', 'prev', 'page', 'next', 'limit', 'skip']
    ,jump: function(obj){
      console.log(obj)
    }
  });

   //展示已知数据
  table.render({
    elem: '#demo',
    height: 315
    ,cols: [[ //标题栏
      {field: 'id', title: '项目ID', width: 80, sort: true}
      ,{field: 'username', title: '项目名', width: 120}
      ,{field: 'case', title: '用例名', minWidth: 150}
      ,{field: 'url', title: '地址', minWidth: 160}
      ,{field: 'data', title: '参数', width: 80}
      ,{field: 'system', title: '请求方式', width: 50}
      ,{field: 'harder', title: '请求头', width: 80, sort: true}
      ,{field: 'banb', title: '版本', width: 60, sort: true}
      ,{field: 'zbanb', title: '最后执行版本', width: 60, sort: true}
      ,{field: 'time', title: '最后执行时间', width: 60, sort: true}
    ]]
    ,data: [{
      "id": "rwd-0001"
      ,"username": "任务单项目"
      ,"case": "用例1"
      ,"url": "www.baidu.com"
      ,"data": "{d:x}"
      ,"system": "post"
      ,"harder": "默认"
      ,"banb": "版本1"
      ,"zbanb": "版本3"
      ,"time":'2018-3-12'
    }]
    //,skin: 'line' //表格风格
    ,even: true
    //,page: true //是否显示分页
    //,limits: [5, 7, 10]
    //,limit: 5 //每页默认显示的数量
  });

});

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
