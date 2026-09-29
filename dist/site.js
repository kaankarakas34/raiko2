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
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const nameEl = form.querySelector('[name="name"]');
    const emailEl = form.querySelector('[name="email"]');
    const companyEl = form.querySelector('[name="company"]');
    const messageEl = form.querySelector('[name="message"]');
    const btn = form.querySelector('.raiko-submit');
    const btnText = form.querySelector('.raiko-submit-text');
    const successEl = form.querySelector('.raiko-form-success');
    const errorEl = form.querySelector('.raiko-form-error');
    const errorText = form.querySelector('.raiko-form-error-text');

    if (errorEl) errorEl.hidden = true;

    const name = (nameEl?.value || '').trim();
    const email = (emailEl?.value || '').trim();
    const company = (companyEl?.value || '').trim();
    const message = (messageEl?.value || '').trim();
    const topic = form.dataset.topic || 'Raiko Görüşme Talebi';

    const showError = (msg) => {
      if (errorEl && errorText) {
        errorText.textContent = msg;
        errorEl.hidden = false;
      } else {
        alert(msg);
      }
    };

    if (!name || !email || !message) {
      showError('Lütfen adınızı, e-posta adresinizi ve mesajınızı doldurun.');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      showError('Lütfen geçerli bir e-posta adresi girin.');
      return;
    }

    const originalBtnText = btnText ? btnText.textContent : 'Mesaj gönder';
    if (btn) btn.disabled = true;
    if (btnText) btnText.textContent = 'İletiliyor...';

    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        body: JSON.stringify({ name, email, company, message, topic }),
      });

      const data = await response.json().catch(() => ({}));

      if (response.ok && data.success) {
        if (successEl) successEl.hidden = false;
        form.querySelectorAll('.raiko-field').forEach((f) => { f.style.display = 'none'; });
        if (btn) btn.style.display = 'none';
        const note = form.querySelector('.raiko-form-note');
        if (note) note.style.display = 'none';
        form.reset();
      } else {
        throw new Error(data.error || 'İletim sırasında bir sorun oluştu.');
      }
    } catch (err) {
      console.error('Form submission error:', err);
      showError(err.message || 'Mesaj iletilemedi. Lütfen info@raiko.tech adresine doğrudan yazın.');
      if (btn) btn.disabled = false;
      if (btnText) btnText.textContent = originalBtnText;
    }
  });
}
