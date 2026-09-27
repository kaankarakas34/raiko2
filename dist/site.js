const mobileButton = document.querySelector('.menu');
const navigation = document.querySelector('.links');
const groups = [...document.querySelectorAll('.nav-group')];

function closeMenus(returnFocus = false) {
  for (const group of groups) {
    const trigger = group.querySelector('.nav-trigger');
    const panel = group.querySelector('.mega');
    if (returnFocus && trigger.getAttribute('aria-expanded') === 'true') trigger.focus();
    trigger.setAttribute('aria-expanded', 'false');
    panel.hidden = true;
  }
}

function openMenu(group) {
  closeMenus();
  const trigger = group.querySelector('.nav-trigger');
  trigger.setAttribute('aria-expanded', 'true');
  group.querySelector('.mega').hidden = false;
}

for (const group of groups) {
  const trigger = group.querySelector('.nav-trigger');
  trigger.addEventListener('click', () => {
    const wasOpen = trigger.getAttribute('aria-expanded') === 'true';
    wasOpen ? closeMenus() : openMenu(group);
  });
  group.addEventListener('pointerenter', (event) => {
    if (event.pointerType === 'mouse' && window.matchMedia('(min-width: 761px)').matches) openMenu(group);
  });
}

document.querySelector('.header').addEventListener('pointerleave', (event) => {
  if (event.pointerType === 'mouse' && window.matchMedia('(min-width: 761px)').matches) closeMenus();
});

mobileButton.addEventListener('click', () => {
  const next = mobileButton.getAttribute('aria-expanded') !== 'true';
  mobileButton.setAttribute('aria-expanded', String(next));
  navigation.classList.toggle('open', next);
  if (!next) closeMenus();
});

navigation.addEventListener('click', (event) => {
  if (!event.target.closest('a')) return;
  mobileButton.setAttribute('aria-expanded', 'false');
  navigation.classList.remove('open');
  closeMenus();
});

document.addEventListener('pointerdown', (event) => {
  if (!event.target.closest('.header')) closeMenus();
});

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  closeMenus(true);
  mobileButton.setAttribute('aria-expanded', 'false');
  navigation.classList.remove('open');
});

for (const year of document.querySelectorAll('.year')) year.textContent = new Date().getFullYear();

for (const logo of document.querySelectorAll('.ai-logo-mark img')) {
  const hideBrokenLogo = () => { logo.hidden = true; };
  logo.addEventListener('error', hideBrokenLogo, { once: true });
  if (logo.complete && logo.naturalWidth === 0) hideBrokenLogo();
}

const heroScene = document.querySelector('.hero-scene');
if (heroScene) {
  const interactiveScene = window.matchMedia('(min-width: 761px) and (prefers-reduced-motion: no-preference)');
  const loadHero = () => {
    if (interactiveScene.matches) import('/hero.js').catch(() => heroScene.classList.add('scene-unavailable'));
  };
  loadHero();
  interactiveScene.addEventListener('change', loadHero);
}
