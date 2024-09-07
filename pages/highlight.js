// highlight.js
function highlightElement(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.style.border = '2px solid red';
        element.style.backgroundColor = 'yellow';
        element.style.zIndex = '1000';
        element.style.position = 'relative';
    }
}
