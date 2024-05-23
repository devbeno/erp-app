const sh = require('shelljs');
const upath = require('upath');
const appPath = upath.resolve(upath.dirname(__filename), '../erp_app');

sh.mv('dist/css', `${appPath}/public/bootstrap-5/`)
sh.mv('dist/js', `${appPath}/public/bootstrap-5/`)
sh.mv('dist/assets/*', `${appPath}/public/bootstrap-5/`)
sh.mv('dist/*.html', `${appPath}/www/bootstrap-5.html`)

sh.rm('-rf', 'dist')