# Forgotten Items

- Author: Jake Wilson

The Art Institute of Chicago is one of the largest and best-known galleries in the world. Each year its collection of nearly 300,000 works of art are seen by around 1.5 million visitors.

However, not all works get the attention they deserve. Some artworks remain unloved in dusty corners of the museum, others aren't even on display.

I decided to create a Python programme which the AIC's public API to find artworks that haven't been viewed very often, to highlight the lesser-known works in its collection.

The programme returns text info about the object, it's maker, its date, and where to find it in the gallery, along with a web link. This can be set to a MOTD or a daily cron email.

## How I built it

I knew I would need to retrieve, parse, and display data and that I would need to import a few modules: web requests, random, and json. I also knew that I would have to store info on previously-seen objects, so I would have to use the OS module to create, read and write files.

I first set up a simple request to the AIC API using hardoded values. I parsed the JSON response and printed the data to the terminal. I then added a function to generate a random artwork ID and pass that to the request function. In the course of doing this, I decided to separate the URL generator from the request function. I also added a few test parameters to filter the data.

At this point I ran into issues woth 404 responses. I checked the python docs for the URLLIB module on how to [handle errors](https://docs.python.org/3/library/urllib.error.html). I imported urllib.error and [set up a TRY-ELSE condition](https://docs.python.org/3/howto/urllib2.html#handling-exceptions) to handle exceptions. At first, this code simply displayed an error message and quit.

Reading the [API documentation](https://api.artic.edu/docs/), I identified the fields I wanted to target. I enumerated these fields in a list as a constant and created a function to extract the desired fields from the returned data.

## TODO

- The AIC also has an [image AP](https://api.artic.edu/docs/#iiif-image-api). I could display images in the terminal using PIL. Alternatively, I could generate ASCII art images.
- The programme could dynamically generate the collection_size variable [by calling limit=0](https://api.artic.edu/docs/#pagination). This would reduce the number of 404 responses.
