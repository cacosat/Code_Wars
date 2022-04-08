def domain_name(url):
    result = ""
    if url[:8] == "https://":
        url = url[8:]
    elif url[:7] == "http://":
        url = url[7:]
    lst = url.split(".")
    if lst[0] == "www":
        result = lst[1]
        print(lst)
    else:
        result = lst[0]
    print(result)
    return result

domain_name("www.xakep.ru")