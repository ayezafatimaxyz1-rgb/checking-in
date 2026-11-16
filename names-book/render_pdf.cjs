const { chromium } = require('playwright');
(async () => {
  const [,, html, pdf] = process.argv;
  const b = await chromium.launch();
  const pg = await b.newPage();
  await pg.goto('file://' + require('path').resolve(html));
  await pg.waitForTimeout(500);
  await pg.pdf({ path: pdf, printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
