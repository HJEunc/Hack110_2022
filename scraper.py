import urllib.parse
import urllib.request
import ssl


def main(url1: str, url2: str):

    ssl._create_default_https_context = ssl._create_unverified_context

    # Urlencode the URL
    url1 = urllib.parse.quote_plus(url1)
    url2 = urllib.parse.quote_plus(url2)

    # Create the query URL.
    query1 = "https://api.scraperbox.com/scrape"
    query1 += "?token=%s" % "848EE571F23C6D45A602D8AA75E6D01F"
    query1 += "&url=%s" % url1

    query2 = "https://api.scraperbox.com/scrape"
    query2 += "?token=%s" % "848EE571F23C6D45A602D8AA75E6D01F"
    query2 += "&url=%s" % url2

    # Call the API.
    request1 = urllib.request.Request(query1)
    raw_response1 = urllib.request.urlopen(request1).read()
    html1 = raw_response1.decode("utf-8")

    request2 = urllib.request.Request(query2)
    raw_response2 = urllib.request.urlopen(request2).read()
    html2 = raw_response2.decode("utf-8")

    required1: list[str] = []
    name_of_mag: str = ""
    got_u: int = 0
    for i in range(len(html1)):
        if html1[i] == "&":
            got_u = i
            break
    for i in range(len(html1)):
        required_course: str = html1[i:i + 50]
        if required_course[0:11] == "Total Hours":
            break
        if required_course[0:7] == "this, '":
            if not required_course[7:15] in required1:
                required1.append(required_course[7:15])
        if required_course[0:7] == "<title>":
            name_of_mag = required_course[7:got_u - i]
    print(name_of_mag)
    print(required1)

    required2: list[str] = []
    name_of_mag_2: str = ""
    got_u_2: int = 0
    for i in range(len(html2)):
        if html2[i] == "&":
            got_u_2 = i
            break
    for i in range(len(html2)):
        required_course: str = html2[i:i + 50]
        if required_course[0:11] == "Total Hours":
            break
        if required_course[0:7] == "this, '":
            if not required_course[7:15] in required2:
                required2.append(required_course[7:15])
        if required_course[0:7] == "<title>":
            name_of_mag_2 = required_course[7:got_u_2 - i]
    print(name_of_mag_2)
    print(required2)

    master_list: list[str] = []
    for i in range(len(required1)):
        master_list.append(required1[i])
    for i in required2:
        if i not in master_list:
            master_list.append(i)
    print(master_list)

    master_str: str = ""
    for item in master_list:
        master_str += f"- {item}\n"
    master_str += " -"

    duplicates: list[str] = []
    for item in required1:
        if item in required2:
            duplicates.append(item)

    master_dup: str = ""
    for item in duplicates:
        master_dup += f"- {item}\n"
    master_dup += " -"

    exclude: list[str] = ["COMP 496", "COMP 690", "COMP 692", "COMP 790"]
  
    for i in range(len(master_str)):
        if master_str[i] in exclude:
            master_str.pop(i)
    for i in range(len(master_dup)):
        if master_dup[i] in exclude:
            master_dup.pop(i)

    output: list[str] = [name_of_mag, name_of_mag_2, master_str, master_dup]

    return output
