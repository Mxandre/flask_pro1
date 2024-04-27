
document.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.getElementById('email');
    const checkEmailBtn = document.getElementById('check-email-btn');
    const emailCheckResult = document.getElementById('email-check-result');

    checkEmailBtn.addEventListener('click', () => {
        const email = emailInput.value.trim();

        if (email !== '') {
            fetch('/check_email', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email: email })
            })
            .then(response => response.json())
            .then(data => {
                if (data.is_registered) {
                    emailCheckResult.textContent = '该邮箱已被注册';
                } else {
                    emailCheckResult.textContent = '该邮箱可用';
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        } else {
            emailCheckResult.textContent = '';
        }
    });
});

function email_time(){
$("#captcha-btn").click(function(event){
var $this=$(this)

event.preventDefault();
var email=$('input[name="email"]').val();
$.ajax({
url:"/ans/captcha?email="+email,
method:"POST",
success :function(result){
var time=60;
$this.off("click")
var timer=setInterval(function(){
$this.text(time);
time--;
if(time<=0){
clearInterval(timer);
$this.text("获取验证码");
email_time();

}
},1000)
alert("success");
console.log(result);
},
error : function(error){
alert("fail");
console.log(error);
}
})
})
}

$(function(){
email_time();

})