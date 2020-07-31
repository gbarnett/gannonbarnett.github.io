# Personal Website 
Setup using pelican, a static site generator. To see details about the framework, see https://docs.getpelican.com/en/stable/index.html. 

# Publishing
Using gitlab pages, pulls from branch gh-pages.
The `src` branch contains the source for the website. Develop in the `src` branch, and then run the following to publish the output:
```
pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git push origin gh-pages
```

# Local Development 
To serve the html locally, run:
`pelican --autoreload --listen` 
Which will automatically listen to changes and update to http://localhost:8000. 

