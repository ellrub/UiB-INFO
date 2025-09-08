let counter = 0;

function hello() {
    counter ++;
    document.querySelector("h1").innerHTML = `Button clicked ${counter}`;
}