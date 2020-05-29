var all_buttons = document.getElementsByClassName("display_button");
var image = document.getElementById('main_image');
var image_nickname = document.getElementById("main_image_nickname")

for (var i = 0; i < all_buttons.length; i++) {
    let butt = all_buttons[i]
    butt.addEventListener("click", function() {
        // TODO: don't hardcode this path
        image.src = "/static/PeasApp/images/" + butt.getAttribute("path");
        image_nickname.innerText = butt.getAttribute("title")
    })
}
