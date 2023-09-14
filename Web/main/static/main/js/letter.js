function runAway(element) {
    var dx = Math.random() * 100 - 50;
    var dy = Math.random() * 100 - 50;
    element.style.transform = "translate(" + dx + "px, " + dy + "px)";

    setTimeout(function() {
            element.style.transform = "translate(0, 0)";
        }, 3000);
}