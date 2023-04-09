import re


def main():
    print(parse(input("HTML: ").replace('"', '')))


def parse(url):
    # check if input matches exptected input
    if s := re.search("^<iframe\s(?:.+)?src=(https?://(?:www\.)?youtube\.com/embed/\S+)(?:.+)?(?:></iframe>)$", url):
        # get the second match group, the first is 'iframe' match
        old_url = s.group(1).replace("http:", "https:").replace("www.", "")
        new_url = old_url.replace("youtube.com/embed/", "youtu.be/")
        return new_url

    return None


if __name__ == "__main__":
    main()