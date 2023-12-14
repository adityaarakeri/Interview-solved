"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""


import random
import string

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}

    def shorten(self, url):
        if url in self.url_to_code:
            # If the URL is already shortened, return the existing short code
            return self.url_to_code[url]

        # Generate a new short code
        short_code = self._generate_short_code()
        
        # Store the mapping in both dictionaries
        self.url_to_code[url] = short_code
        self.code_to_url[short_code] = url

        return short_code

    def restore(self, short_code):
        # Return the original URL if the short code exists, otherwise return None
        return self.code_to_url.get(short_code, None)

    def _generate_short_code(self):
        # Generate a random six-character alphanumeric string
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

# Example usage:
url_shortener = URLShortener()

# Shorten a URL
short_code = url_shortener.shorten("https://www.example.com")
print("Shortened URL:", short_code)

# Restore the original URL
original_url = url_shortener.restore(short_code)
print("Restored URL:", original_url)