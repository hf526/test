var c=$("#case").val();
var n=$("#name").val();
var m=$("#md").val();
var u=$("#path").val();
var d=$("#data").val();
var h=$("#harder").val();
var j=$("#jcd").val();

//$("#chick").click(function(){
//    if (get_val("#md")==null|| get_val("#path")==null|| get_val("#data")==null)
//        {
//                   $("#md").css("border-color","red");
//                   alert("aa");
//        }
//    else{
//        alert()
//        $("#md").css("border-color","red");
//        $.post("/fangwenjk",
//    {
//        case:$("#case").val(),
//        name:$("#name").val(),
//        method:$("#md").val(),
//        url:$("#path").val(),
//        data:$("#data").val(),
//        harder:$("#harder").val(),
//        jcd:$("#jcd").val()
//
//    },
//        function(data,status){
//        alert("数据: \n" + data + "\n状态: " + status);
//    });
//    };
//
//});
function get_val(d){     //获取输入值
    return $(d).val()
}


$("chick").click(function(){
  alert($(this).serialize());
});