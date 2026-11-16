const { chromium } = require('playwright');
(async () => {
  const [,, htmlPath, outDir] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await p.goto('file://' + htmlPath);
  await p.evaluate(() => document.fonts.ready);
  const n = await p.locator('section').count();
  for (let i = 1; i <= n; i++) {
    const s = p.locator('#s' + i);
    const box = await s.boundingBox();
    const over = await s.evaluate(el => [...el.querySelectorAll('*')].some(c => { const r = c.getBoundingClientRect(), R = el.getBoundingClientRect(); return r.bottom > R.bottom - 110 && !c.closest('.foot') && !c.classList.contains('swipe'); }));
    if (over) console.log('WARN slide', i, 'content reaches footer zone');
    await s.screenshot({ path: `${outDir}/slide-${String(i).padStart(2,'0')}.png` });
  }
  await b.close();
})();
