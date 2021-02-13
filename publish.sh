git add *
git commit -m "New publish"
git push
make clean
make publish
ghp-import output -b gh-pages
git push origin gh-pages
