(function (func) {
    $.ajax({
        url: "/data/getEconomicActive",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var html = "";
    var regBusiness = $("#regBusiness");
    data.series1.forEach(function (item) {
        html += '<li><a href="javascript:;">' + item + '</a></li>'
    });
    regBusiness.html(html);
    textAnim();

    function textAnim() {
        try {
            TagCanvas.Start('cloudCanvas', 'tags2', {
                textFont: "Arial, Helvetica, sans-serif",
                maxSpeed: 0.05,
                minSpeed: 0.01,
                textColour: '#41FDFE',
                textHeight: 12,
                outlineMethod: "colour",
                fadeIn: 800,
                outlineColour: "#41b1c3",
                outlineOffset: 0,
                depth: 0.97,
                minBrightness: 0.2,
                wheelZoom: false,
                reverse: true,
                shadowBlur: 2,
                shuffleTags: true,
                shadowOffset: [1, 1],
                stretchX: 1.2,
                initial: [0, 0.1],
                clickToFront: 600,
                maxSpeed: 0.01,
                outlineDashSpeed: 0.5,
            });
        } catch (e) {
            // something went wrong, hide the canvas container
            document.getElementById('chart_5').style.display = 'none';
        }

    }


});