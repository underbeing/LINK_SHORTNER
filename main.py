import pyshorteners

def shorten_url(long_url):
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    long_url = input("Enter the URL to shorten: ")
    short_url = shorten_url(long_url)
    print(f"Shortened URL: {short_url}")
