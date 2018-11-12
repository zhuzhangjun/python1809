$(function () {
    //获取json中的数据
    $.get("../json/productList-1.json", function (data) {
        var arr = data;
        console.log(data);
        for (var i = 0; i < arr.length; i++) {
            var obj = arr[i]; //每个商品数据

            //找到id相同的商品后，就可以使用obj了
            if (obj.id == pid) {
                loadUI(obj);
            }
        }
    })

    //获取json中的数据

    function loadUI(obj) {
        $(".smallImg img").attr("src", obj.middleimg1);
        $("#smllList img").eq(0).attr("src", obj.smallimg1);
        $("#smllList img").eq(0).attr("data-msrc", obj.middleimg1);
        $("#smllList img").eq(1).attr("data-msrc", obj.middleimg2);
        $("#smllList img").eq(2).attr("data-msrc", obj.middleimg3);
        $("#smllList img").eq(3).attr("data-msrc", obj.middleimg4);

        $("#smllList img").eq(0).attr("data-bsrc", obj.bigimg1);
        $("#smllList img").eq(1).attr("data-bsrc", obj.bigimg2);
        $("#smllList img").eq(2).attr("data-bsrc", obj.bigimg3);
        $("#smllList img").eq(3).attr("data-bsrc", obj.bigimg4);

        $("#smllList img").eq(1).attr("src", obj.smallimg2);
        $("#smllList img").eq(2).attr("src", obj.smallimg3);
        $("#smllList img").eq(3).attr("src", obj.smallimg4);

        $(".bigImg").attr("src", obj.bigimg1);

        $("#titlname h1").html(obj.title);
        $("#titlname strong").html(obj.hint);
        $("#unit").html(obj.unit);
        $("#punit").html(obj.unit);
        $("#original").html(obj.original);
        $("#price").html(obj.price);
        $("#evaluate").html(obj.evaluate);
        $("#repertory").html(obj.repertory);
        $(".ncs-goods-img-content img").eq(0).attr("src", obj.dtbgimg1);
        $(".ncs-goods-img-content img").eq(1).attr("src", obj.dtbgimg2);
        $(".ncs-goods-img-content img").eq(2).attr("src", obj.dtbgimg3);
        $(".ncs-goods-img-content img").eq(3).attr("src", obj.dtbgimg4);
        $(".ncs-goods-img-content img").eq(4).attr("src", obj.dtbgimg5);
        $(".ncs-goods-img-content img").eq(5).attr("src", obj.dtbgimg6);
    }

    //查找参数对应的值
    function getParams(str, name) {
        var arr = str.split("&");
        for (var i = 0; i < arr.length; i++) {
            var str1 = arr[i]; // id=1002
            var arr1 = str1.split("=");
            if (arr1[0] == name) {
                return arr1[1];
            }
        }
        return "";
    }
})
//////////////////////////////////////////////////////////////////////////////////////////
//.smallArea 小区域
//.smallImg  中区域
//.bigArea 大区域
//bigImg
//-------------------------------------------放大镜-------------------------------------
$(function () {

    //等比公式
    //小图width/大图width == 小区域width/大区域width

    //在中区域移动
    $(".smallImg").mousemove(function (e) {

        $(".smallArea").show(); //显示小区域
        $(".bigArea").show(); //显示大区域

        $(".smallArea").width($(".smallImg").width() * $(".bigArea").width() / $(".bigImg").width());
        $(".smallArea").height($(".smallImg").height() * $(".bigArea").height() / $(".bigImg").height());

        //放大系数
        var scale = $(".bigImg").width() / $(".smallImg img").width();
        //var scale=2;
        //console.log($(".bigImg").width())


        var x = e.pageX - $(".smallImg").offset().left - $(".smallArea").width() / 2;
        var y = e.pageY - $(".smallImg").offset().top - $(".smallArea").height() / 2;
        //console.log($(".bigImg").attr("src"));


        //控制不超出左右边界
        if (x < 0) {
            x = 20;
        }
        else if (x > $(".smallImg").width() - $(".smallArea").width() - 20) {
            x = $(".smallImg").width() - $(".smallArea").width() - 20;
        }
        //控制不超出上下边界
        if (y < 0) {
            y = 20
        }
        else if (y > $(".smallImg").height() - $(".smallArea").height() - 20) {
            y = $(".smallImg").height() - $(".smallArea").height() - 20;
        }

        //小区域移动
        $(".smallArea").css({left: x, top: y});
        //console.log(scale)
        //大图移动
        $(".bigImg").css({left: -scale * x, top: -scale * y});
    })
    //移除小图
    $(".smallImg").mouseleave(function (e) {
        $(".smallArea").hide(); //隐藏小区域
        $(".bigArea").hide(); //隐藏大区域
    })

    //图片切换
    $("#smllList li").mouseenter(function () {
        //改变小图切换样式
        $(this).addClass("current-controller").siblings().removeClass("current-controller");

        //改变路径
        //console.log($(this).find("img").attr("data-msrc"));

        var msrc = $(this).find("img").attr("data-msrc");
        var bsrc = $(this).find("img").attr("data-bsrc");
        //console.log(msrc);

        $(".smallImg img").attr("src", msrc);
        $(".bigImg").attr("src", bsrc);
    })
})
// 加操作
$('.ncs-buy .ncs-btn .addcart').click(function () {
    // 商品ID
    var detail = $(this).attr('detail_info')
    // that为了解决，在ajax中，this指向问题
    var $that = $(this)

    $.get('/addcart/', {'detail': detail}, function (response) {
        console.log(response)
        console.log(111111111111111111111111111111111111111111)
        if (response.status == -1) { // 未登录
            window.open('/login/', target = "_self")
        } else if (response.status == 1) {   // 添加成功
            // 错误的！！！
            // $('.bt-wrapper .glyphicon-minus').show()
            // $('.bt-wrapper .num').show().html(response.number)


            // 只修改当前操作的商品
            // $(this).prev().show().html(response.number)
            // $(this).prev().prev().show()
            console.log('添加成功！')
        }
    })
})
