layui.use('element', function(){
  var element = layui.element;
});
layui.use('table', function(){
              var table = layui.table;
             table.render({
                elem: '#demo'
                ,cellMinWidth: 80
                ,url: '/demo'
                ,page: true
                ,cols: [[
                  {field: 'id', title: 'ID', sort: true, fixed: 'left'}
                  ,{field: 'case', title: '用例名称', }
                  ,{field: 'name', title: '接口名称', sort: true}
                  ,{field: 'md', title: '请求方式'}
                  ,{field: 'path', title: '接口地址'}
                  ,{field: 'data', title: '接口参数',  sort: true}
                  ,{field: 'harder', title: '请求头',  sort: true}
                  ,{field: 'jcd', title: '检查点', }
                  ,{field: 'r', title: '结果', sort: true}
                ]]
              });
            });
$(document).ready(function(){
    $("#submit").click(function(){
        $.post("/login",
        {
            case:$("#case").val(),
            name:$("#name").val(),
            method:$("#md").val(),
            url:$("#path").val(),
            data:$("#data").val(),
            harder:$("#harder").val(),
            jcd:$("#jcd").val()

        },
            function(data,status){
            alert("数据: \n" + data + "\n状态: " + status);
        });
    });
    $("#chick").click(function(){
        $.post("/interface",
        {
            case:$("#case").val(),
            name:$("#name").val(),
            method:$("#md").val(),
            url:$("#path").val(),
            data:$("#data").val(),
            harder:$("#harder").val(),
            jcd:$("#jcd").val()
        },
            function(data,status){
            alert("数据: \n" + data + "\n状态: " + status);
        });
    });
});