// var imageStock = ["/static/img/group15.png", "/static/img/group15-dark.png"];

(function () {
    var rotator3 = document.getElementById('home-banner-img'); // change to match   image ID
    var imageDir = '/static/img/';
    // set number of seconds delay
    // list image names
    var images = ['group15.png', 'group15-dark.png'];

    // don't change below this line
    var num = 0;
    var changeImage = function () {
        var len = images.length;
        rotator3.src = imageDir + images[num++];
        if (num == len) {
            num = 0;
        }
    };

    function SwImg() {
        setInterval(changeImage, 2000);


    }


    setTimeout(SwImg, 2000);


})();
