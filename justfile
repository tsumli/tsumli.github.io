serve: fathli
    hugo server -D -p 1313

build *args: fathli
    hugo --minify --cleanDestinationDir {{args}}

fathli:
    cd apps/fathli && npm ci --no-audit --no-fund && npm run build -- --base /graphics/3dgs/ --outDir ../../static/graphics/3dgs --emptyOutDir
