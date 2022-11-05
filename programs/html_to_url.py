"""Insert youtube HTML adress and see converted adress to URL"""


import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search('youtube.com', s) and re.search('^<iframe', s):
        url1 = re.findall('https?://w*.?youtube.com/embed/\w+', s)
        out_of_url1_list = url1[0]
        return re.sub(".*//.+/.+/", "https://youtu.be/", out_of_url1_list)
    else:
        return None

if __name__ == "__main__":
    main()
