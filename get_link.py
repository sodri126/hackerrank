import sys

def get_link(str_link):
    get_str_arr = str_link.split()
    result_str_arr = []
    for str_link in get_str_arr:
        if str_link.find("http") > -1:
            result_str_arr.append(str_link)

    return result_str_arr

if __name__ == "__main__":
    a = "They said that website https://www.facebook.com is an awesome social media http://www.twitter.com platform"
    print(get_link(a))