var c=$("#case").val();
var n=$("#name").val();
var m=$("#md").val();
var u=$("#path").val();
var d=$("#data").val();
var h=$("#harder").val();
var j=$("#jcd").val();

$("#chick").click(function(){
    if (get_val("#method")==null|| get_val("#path")==null|| get_val("#path")==null)
        {
                    alert("success");
        }
    else{
        $.post("/fangwenjk",
    {
//        case:c,
//        name:n,
//        method:m,
//        url:u,
//        data:d,
//        harder:h,
//        jcd:j
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
    };

});
function get_val(d){     //获取输入值
    return $(d).val()
}
