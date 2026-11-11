const {minify} = require('html-minifier-terser'); const fs = require('fs');
(async () => {
  const src = fs.readFileSync(process.argv[2], 'utf8');
  const out = await minify(src, {collapseWhitespace: true, conservativeCollapse: true, removeComments: true, minifyCSS: true,
    minifyJS: {compress: {passes: 1}, mangle: true, format: {comments: false}}, keepClosingSlash: true});
  fs.writeFileSync(process.argv[3], out); console.log(src.length, '->', out.length);
})().catch(e => { console.error('MINIFY FAILED', e.message); process.exit(1); });
