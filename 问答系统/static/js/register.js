function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function (event){
        //$this: 代表的是当前按钮的jquery对象
        var $this = $(this);
        // 阻止默认的事件
        event.preventDefault();
        // 这里我通过id获取输入框，还有一种方法是通过name
        // input[name="email"]替换#exampleInputEmail1
        var email = $("#exampleInputEmail1").val();
        $.ajax({
            url:"/auth/captcha/email?email="+email,
            method:"GET",
            success: function (result){
                var code = result['code'];
                if (code == 200){
                    var countdown = 60;
                    // 开始倒计时之前，就取消按钮的点击事件
                    $this.off("click");
                    var timer = setInterval(function (){
                        $this.text(countdown);
                        countdown -= 1;
                        //倒计时结束时执行
                        if (countdown<= 0){
                            //  清掉定时器
                            clearInterval(timer);
                            // 将按钮文字重新改回来
                            $this.text("获取验证码")
                            // 重新绑定点击时间
                            bindEmailCaptchaClick();
                        }
                    },  1000);
                    alert("邮箱验证码发送成功");
                }else {
                    alert(result["message"]);
                }
            },
            fail : function (error) {
                console.log(error);
            }
        })
    });
}

// 整个网页都加载完毕后才会执行
$(function () {
    bindEmailCaptchaClick();
});