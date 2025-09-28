const buttons = document.querySelectorAll('.header__project-nav button');
const sections = {
    0: document.querySelector('.header__section-home'),
    1: document.querySelector('.header__project-whitespace'),
    2: document.querySelector('.header__project-snapshot'),
    3: document.querySelector('.header__project-insanity')
}

let currentSelection = 0;

buttons.forEach((button, index) => {
    button.addEventListener('click', () => {
        sections[currentSelection].style.display = 'none';
        const targetIndex = index + 1;
        sections[targetIndex].style.display = 'flex';
        sections[targetIndex].style.animation = 'slideInFromRight 0.8s ease-out';

        currentSelection = targetIndex;
    });
});