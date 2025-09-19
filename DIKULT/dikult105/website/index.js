htmlWhitespace = document.getElementById("whitespace");
htmlWhitespace.addEventListener("mouseover", whitespaceHover);
htmlWhitespace.addEventListener("mouseleave", whitespaceLeave);

function whitespaceHover() {
    htmlWhitespace.classList.add("hover_whitespace")
    setTimeout(() => {
        htmlWhitespace.innerHTML = "Is not your Enemy";
        htmlWhitespace.classList.add("friend")
        setTimeout(() => {
            htmlWhitespace.classList.add("set_friend")
        }, 1000);
    }, 1000);
}