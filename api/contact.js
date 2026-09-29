const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST || 'mail.kurumsaleposta.com',
  port: parseInt(process.env.SMTP_PORT || '465', 10),
  secure: true, // Port 465 requires SSL
  auth: {
    user: process.env.SMTP_USER || 'info@raiko.tech',
    pass: process.env.SMTP_PASS || '@hd5-jX:0ZtL8@S3',
  },
  tls: {
    // Kurumsal e-posta sertifika uyumluluğu için
    rejectUnauthorized: false,
  },
});

const RECIPIENTS = [
  'kaankarakas93@gmail.com',
  'info@raiko.tech',
  'sinanaksoz5@gmail.com'
];

module.exports = async function handler(req, res) {
  // CORS & method check
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    let body = req.body;
    if (typeof body === 'string') {
      try {
        body = JSON.parse(body);
      } catch (e) {
        // fallback to query or raw string
      }
    }

    const { name, email, company, message, topic, want_meeting } = body || {};

    if (!name || !email || !message) {
      return res.status(400).json({ error: 'Lütfen zorunlu alanları doldurun (İsim, E-posta, Mesaj).' });
    }

    const dateStr = new Date().toLocaleString('tr-TR', {
      timeZone: 'Europe/Istanbul',
      dateStyle: 'full',
      timeStyle: 'medium'
    });

    const leadTopic = topic ? `[${topic}] ` : '';
    const meetingTag = want_meeting ? '📅 [TOPLANTI TALEBİ] ' : '';
    const subject = `${meetingTag}Yeni Lead: ${leadTopic}${name} ${company ? `(${company})` : ''}`.trim();

    const textContent = `
${want_meeting ? '*** DİKKAT: MÜŞTERİ HEMEN TOPLANTI / DEMO PLANLAMAK İSTEDİ ***\n' : ''}Yeni Lead Bildirimi
------------------------------------------------
Ad Soyad : ${name}
E-posta  : ${email}
Şirket   : ${company || '-'}
Sayfa/Konu: ${topic || 'Genel'}
Toplantı İsteği: ${want_meeting ? 'EVET (Takvim açıldı)' : 'HAYIR (Sadece mesaj)'}
Tarih    : ${dateStr}

Mesaj:
${message}
------------------------------------------------
Bu mesaj www.raiko.tech iletişim formu üzerinden iletilmiştir.
`;

    const htmlContent = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f7f7f5; margin: 0; padding: 24px; color: #11110f; }
    .card { max-width: 580px; margin: 0 auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e1d8; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.06); }
    .header { background: #11110f; color: #ffffff; padding: 24px 28px; }
    .header h2 { margin: 0; font-size: 20px; font-weight: 700; color: #ffc400; }
    .header p { margin: 4px 0 0; font-size: 13px; color: #a2a29a; }
    .content { padding: 28px; }
    .meeting-badge { background: #fff8e1; border: 1.5px solid #ffc400; color: #855500; border-radius: 8px; padding: 12px 16px; font-size: 14px; font-weight: 700; margin-bottom: 20px; display: flex; align-items: center; gap: 8px; }
    .item { margin-bottom: 16px; }
    .item-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: #79796e; font-weight: 700; margin-bottom: 4px; }
    .item-value { font-size: 15px; color: #11110f; font-weight: 500; }
    .item-value a { color: #d97706; text-decoration: none; font-weight: 600; }
    .message-box { background: #fbfbf8; border: 1px solid #eae8de; border-radius: 8px; padding: 16px; margin-top: 20px; font-size: 14.5px; line-height: 1.6; color: #2e2d27; white-space: pre-wrap; }
    .footer { padding: 16px 28px; background: #f4f2eb; border-top: 1px solid #eae8de; font-size: 12px; color: #8e8d85; text-align: center; }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h2>🚀 Yeni Lead Bildirimi</h2>
      <p>Raiko web sitesi üzerinden yeni bir talep alındı</p>
    </div>
    <div class="content">
      ${want_meeting ? `
      <div class="meeting-badge">
        <span>📅</span>
        <span>MÜŞTERİ HEMEN TOPLANTI SAATİ SEÇMEK İSTEDİ (Cal.com ekranı açıldı)</span>
      </div>` : ''}
      <div class="item">
        <div class="item-label">Ad Soyad</div>
        <div class="item-value">${name}</div>
      </div>
      <div class="item">
        <div class="item-label">E-posta</div>
        <div class="item-value"><a href="mailto:${email}">${email}</a></div>
      </div>
      ${company ? `
      <div class="item">
        <div class="item-label">Şirket / Sektör</div>
        <div class="item-value">${company}</div>
      </div>` : ''}
      ${topic ? `
      <div class="item">
        <div class="item-label">İlgili Konu / Sayfa</div>
        <div class="item-value">${topic}</div>
      </div>` : ''}
      <div class="item">
        <div class="item-label">Toplantı Tercihi</div>
        <div class="item-value">${want_meeting ? '<strong>Evet, toplantı planlamak istiyor</strong>' : 'Sadece mesaj iletildi'}</div>
      </div>
      <div class="item">
        <div class="item-label">Tarih</div>
        <div class="item-value">${dateStr}</div>
      </div>
      <div class="item" style="margin-bottom: 0;">
        <div class="item-label">Mesaj</div>
        <div class="message-box">${message}</div>
      </div>
    </div>
    <div class="footer">
      Bu mesaj <strong>raiko.tech</strong> iletişim formu üzerinden gönderilmiştir.
    </div>
  </div>
</body>
</html>
`;

    const info = await transporter.sendMail({
      from: '"Raiko Lead" <info@raiko.tech>',
      to: RECIPIENTS.join(', '),
      replyTo: email,
      subject: subject,
      text: textContent,
      html: htmlContent,
    });

    return res.status(200).json({ success: true, messageId: info.messageId });
  } catch (error) {
    console.error('Mail send error:', error);
    return res.status(500).json({ error: 'Mail gönderilirken hata oluştu.', details: error.message });
  }
};
