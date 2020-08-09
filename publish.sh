git add *
git commit -m "New publish"
git push
make clean
pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git push origin gh-pages
