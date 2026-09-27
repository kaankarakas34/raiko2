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

const heroScene = document.querySelector('.hero-scene');
if (heroScene && window.matchMedia('(min-width: 761px) and (prefers-reduced-motion: no-preference)').matches) {
  const viewer = heroScene.querySelector('spline-viewer');
  const showScene = () => heroScene.classList.add('scene-ready');
  viewer.addEventListener('load', showScene, { once: true });
  const viewerScript = document.createElement('script');
  viewerScript.type = 'module';
  viewerScript.src = 'https://unpkg.com/@splinetool/viewer/build/spline-viewer.js';
  viewerScript.onerror = () => heroScene.classList.add('scene-unavailable');
  document.head.append(viewerScript);
  customElements.whenDefined('spline-viewer').then(() => {
    let attempts = 0;
    const readyCheck = setInterval(() => {
      if (heroScene.classList.contains('scene-ready')) {
        clearInterval(readyCheck);
        return;
      }
      const canvas = viewer.shadowRoot?.querySelector('canvas#spline');
      if (canvas?.style.visibility === 'visible') {
        showScene();
        clearInterval(readyCheck);
      } else if (++attempts >= 75) {
        heroScene.classList.add('scene-unavailable');
        clearInterval(readyCheck);
      }
    }, 200);
  });
}
