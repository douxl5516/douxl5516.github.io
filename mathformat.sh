yarn remove hexo-renderer-marked
yarn add hexo-renderer-kramed
yarn remove hexo-math
yarn add hexo-renderer-mathjax
\cp backup/inline.js node_modules/kramed/lib/rules/inline.js
\cp backup/mathjax.html node_modules/hexo-renderer-mathjax/mathjax.html
\cp -r backup/renderer.js node_modules/hexo-renderer-kramed/lib/renderer.js