var jmeno_souboru = 'log.png';
$(document).ready(function () {
        var timeoutObject = null;
        function call() {
        $.ajax({
            url: '?action=checkfile&filename=' + jmeno_souboru,
            complete: function(data) {
                console.log(data);
                if (data.responseText.indexOf('no') == 0) {
                    setTimeout(call, 5000);
                }
                else {
                    if (data.responseText.indexOf('yes') == 0) {
                        $('.pic').append(' <img src="images/log.png" alt="Graph"> ');
                        $('.pictohide').hide();
                        clearTimeout(timeoutObject)
                    }
                    else {
                        setTimeout(call, 5000);
                    }
                }
            }
        });
    }
    setTimeout(function () { call(); }, 5000);

});
