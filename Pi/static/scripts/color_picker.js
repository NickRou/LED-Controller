document.addEventListener('DOMContentLoaded', function() {

    var colorPicker = new window.iro.ColorPicker(".colorPicker", {
        width: 280,
        color: "rgb(255, 0, 0)",
        borderWidth: 1,
        borderColor: "#fff",
    }, false);
    
    var values = document.getElementById("values");
    var rgb = "rgb(255, 0, 0)"
    
    colorPicker.on(["color:init", "color:change"], function(color){
        values.innerHTML = "rgb: " + color.rgbString;
        rgb = color.rgbString;
    });

    document.getElementById('submit-button').onclick = function() {
        $.ajax({
            url: Flask.url_for('root'),
            type: 'POST',
            data: {'rgbString' : rgb}
        });
    }
});

