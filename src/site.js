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

/* ── Contact form handler ──────────────────────────────── */
for (const form of document.querySelectorAll('.raiko-form')) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = (form.querySelector('[name="name"]')?.value || '').trim();
    const email = (form.querySelector('[name="email"]')?.value || '').trim();
    const company = (form.querySelector('[name="company"]')?.value || '').trim();
    const message = (form.querySelector('[name="message"]')?.value || '').trim();
    const topic = form.dataset.topic || 'Raiko demo talebi';

    if (!name || !email || !message) {
      const missingFields = [];
      if (!name) missingFields.push('Adınız');
      if (!email) missingFields.push('E-posta adresiniz');
      if (!message) missingFields.push('Mesajınız');
      alert('Lütfen şu alanları doldurun: ' + missingFields.join(', '));
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert('Lütfen geçerli bir e-posta adresi girin.');
      return;
    }

    const subject = encodeURIComponent(topic + ' hakkında görüşme talebi');
    const body = encodeURIComponent(
      'Ad: ' + name + '\n' +
      'E-posta: ' + email + '\n' +
      (company ? 'Şirket/Sektör: ' + company + '\n' : '') +
      '\nMesaj:\n' + message
    );

    const btn = form.querySelector('.raiko-submit');
    if (btn) btn.disabled = true;

    window.location.href = 'mailto:info@raiko.tech?subject=' + subject + '&body=' + body;

    setTimeout(() => {
      const successEl = form.querySelector('.raiko-form-success');
      if (successEl) successEl.hidden = false;
      form.querySelectorAll('.raiko-field').forEach(f => { f.style.display = 'none'; });
      if (btn) btn.style.display = 'none';
      const note = form.querySelector('.raiko-form-note');
      if (note) note.style.display = 'none';
    }, 600);
  });
}
