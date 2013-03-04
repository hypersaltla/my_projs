import urllib.request, urllib.error, json, re, os
from bs4 import BeautifulSoup, Comment, Tag
from time import gmtime, strftime

def get_artist(soup, dump):
    artist_item = dict()
    artist = soup.find(class_='header_redesign')
    artist_item["artist_name"] = artist.string.strip()
    search_area = artist.parent.extract()
    counter = 0
    for per_bio in search_area.find_all(class_='bio'):
        if per_bio.get_text(strip=True) != "":
            if counter == 0:
                short_bio = per_bio.contents[0]
                artist_item["birth_data_and_place"] = short_bio.strip()
                artist_item["occupation"] = per_bio.contents[1].contents[0].strip()
                 #looks weird because of the <br> tag is not closed
                artist_item["nationality"] = per_bio.contents[1].contents[1].contents[0].strip()
                counter += 1
            else:
                artist_item["long_biography"] = per_bio.get_text(strip=True)
    json.dump(artist_item, dump)
    dump.write("\n")

def get_collection(soup, dump, url):
    collection_item = dict()
    with urllib.request.urlopen(url+"&handle=li") as imgpage:
        img_soup = BeautifulSoup(imgpage)
        img_list = img_soup.find_all("img")
        for item in img_list:
            if re.search("/art/collections/images/l/",item["src"]):
                collection_item["img_url"] = "www.getty.edu"+item["src"]
                break
                
    collection_item['title'] = soup.find(class_='header_redesign').string.strip()
    
    enlarge_a = soup.find(class_='art')
    enlarge_url = enlarge_a['href']
    forms = soup.find_all('form')
    for my_form in forms:
        if my_form['name'] == u"bookmarkobj":
            if my_form.p.a:
                collection_item['artist_name'] = my_form.p.a.string.strip()
            else:
                collection_item['artist_name'] = my_form.p.contents[0].strip()
            
            made = my_form.br.contents[0].strip()
            result_nation = re.search('([a-zA-Z\s]+),',made)
            result_date = re.search('\d+[\d\s,\-a-z]+',made)
            
            if result_nation:
                collection_item['nationality'] = result_nation.group(1)
            if result_date:
                collection_item['date_made'] = result_date.group(0)
            collection_item['technique'] = ""
            for ever in my_form.br.br.children:
                if ever == my_form.br.br.br:
                    break
                else:
                    collection_item['technique'] += ever.string.strip()
            if len(my_form.br.br.br.contents) > 1:
                collection_item['dimensions'] = my_form.br.br.br.contents[0].strip()
                collection_item['access_id'] = my_form.br.br.br.br.contents[0].strip()
            else:
                collection_item['access_id'] = my_form.br.br.br.contents[0].strip()
            break
    siblings= my_form.parent.parent.next_siblings
    for tr in siblings:
        find = tr.find('p')
        if find != -1 and find:
            collection_item['description'] = tr.td.p.get_text(strip=True)
            break
    json.dump(collection_item,dump)
    dump.write("\n")


next_url = "http://www.getty.edu/art/gettyguide/artMakerList?lt=A&pg=1"
lts = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cur_lt = 0 #parse begins with the artists whose lastname start with A

dirname = "getty_data/"
if not os.path.exists(dirname):
    os.makedirs(dirname)

artist_dump = open(dirname+"artist_" + lts[cur_lt] +".json", "w")
artwork_dump = open(dirname+"artwork_" + lts[cur_lt] +".json", "w")

with open('err_log.txt','w') as logf:
    while cur_lt < 26: #parse ends when finish with artists whose lastname ends with Z
        #open the url of next page containing artists
        with urllib.request.urlopen(next_url) as f:
                    soup = BeautifulSoup(f)
                    artist_hrefs = soup.find_all(class_="art") #get a list of urls link to artist bio page
                    for per_artist in artist_hrefs:
                            if per_artist.img:
                                    #open and parse one page of an artist
                                    with urllib.request.urlopen(per_artist['href']) as ard:
                                            ard_soup = BeautifulSoup(ard)
                                            try:
                                                get_artist(ard_soup, artist_dump)
                                            except AttributeError as atterr:
                                                info = per_artist['href']
                                                info += ", "
                                                info += str(atterr)
                                                info += ", "
                                                info += strftime("%d/%m/%Y %H:%M:%S", gmtime())
                                                logf.write(info+'\n')

                                            #get urls link to the collections of the artists for the 1st page
                                            coll_urls = ard_soup.find_all(class_="art")
                                            for each_col in coll_urls:
                                                    if each_col.img:
                                                            try:
                                                                    if each_col['href'].find("artObjectDetails") != -1:
                                                                            #open the page containing collection information
                                                                            cod = urllib.request.urlopen(each_col['href'])
                                                                            try:
                                                                                get_collection(BeautifulSoup(cod), artwork_dump, each_col['href'])
                                                                            except AttributeError as atterr:
                                                                                 info = each_col['href']
                                                                                 info += ", "
                                                                                 info += str(atterr)
                                                                                 info += ", "
                                                                                 info += strftime("%d/%m/%Y %H:%M:%S", gmtime())
                                                                                 logf.write(info+'\n')
                                                                                
                                                            except urllib.error.HTTPError as httperr:
                                                                    print(httperr)
                                            next_page_href = ard_soup.find(src="/art/collections/images/art_next.gif")
                                    #link to the next page of collections
                                    while next_page_href:
                                            with urllib.request.urlopen(next_page_href.parent['href']) as next_p:
                                                    next_p_soup = BeautifulSoup(next_p)
                                                    
                                                    coll_urls = next_p_soup.find_all(class_="art")
                                                    for each_col in coll_urls:
                                                            #print(each_col['href'])
                                                            try:
                                                                    if each_col['href'].find("artObjectDetails") != -1:
                                                                            cod = urllib.request.urlopen(each_col['href'])
                                                                            try:
                                                                                get_collection(BeautifulSoup(cod), artwork_dump, each_col['href'])
                                                                            except AttributeError as atterr:
                                                                                info = each_col['href']
                                                                                info += ", "
                                                                                info += str(atterr)
                                                                                info += ", "
                                                                                info += strftime("%d/%m/%Y %H:%M:%S", gmtime())
                                                                                logf.write(info+'\n')
                                                                            
                                                            except urllib.error.HTTPError as httperr:
                                                                    print(httperr)
                                                    next_page_href = next_p_soup.find(src="/art/collections/images/art_next.gif")
                    href = soup.find(src='/art/collections/images/art_next.gif')
                    if href:
                            next_url = href.parent['href']
                    else:
                            cur_lt += 1
                            artist_dump.close()
                            artwork_dump.close()
                            if cur_lt < 26:
                                next_url = "http://www.getty.edu/art/gettyguide/artMakerList?lt="+lts[cur_lt]+"&pg=1"
                                artist_dump = open(dirname+"artist_" + lts[cur_lt] +".json", "w")
                                artwork_dump = open(dirname+"artwork_" + lts[cur_lt] +".json", "w")
