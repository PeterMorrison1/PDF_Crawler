import requests
import pprint
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import urllib.request
from foreign_site import ForeignSite

pp = pprint.PrettyPrinter(indent=4)

def main():
    print("Start scraper")

    # URL = "https://pubmed.ncbi.nlm.nih.gov/31285808/?from_single_result=Davari%2C+M.%2CGharibnaseri%2C+Z.%2CRavanbod%2C+R.%2CSadeghi%2C+A.+Health+status+and+quality+of+life+in+patients+with+severe+hemophilia+A%3A+A+cross-sectional+survey&expanded_search_query=Davari%2C+M.%2CGharibnaseri%2C+Z.%2CRavanbod%2C+R.%2CSadeghi%2C+A.+Health+status+and+quality+of+life+in+patients+with+severe+hemophilia+A%3A+A+cross-sectional+survey"
    URL = "https://pubmed.ncbi.nlm.nih.gov/31136347/?from_single_result=Caruso+Brown%2C+A.+E.+Embracing+Discomfort+on+the+Path+to+Humility&expanded_search_query=Caruso+Brown%2C+A.+E.+Embracing+Discomfort+on+the+Path+to+Humility"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    id_list = soup.find(id='full-view-identifiers')
    PMCID = id_list.find('span', class_='identifier pmc')

    if PMCID:
        run_id_code(PMCID)
    else:
        link_div = soup.find('div', class_='full-text-links-list')
        links = link_div.find_all('a', class_='link-item')

        for link in links:
            print("LINK: " + link.get("href").strip())
            for_site = ForeignSite(link.get("href").strip(), '', '', '')
            print(for_site.get_site_parser())


        print("Probably need to run selenium now for each possible webpage...")


def run_id_code(PMCID):
    newURL = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id="
    id = PMCID.find('a', class_='id-link').text.strip()
    print("The id is: " + id)
    print("Now run the search with that id")
    print("https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=" + id)
    request = newURL + id
    new_page = requests.get(request)

    root = ET.fromstring(new_page.content)
    # root = root.find("./records/record")
    xml_links = root.findall("./records/record/link")
    for link in xml_links:
        type = link.get('format')
        if type == "pdf":
            pdf_url = link.get("href").strip()
            print("Download: " + pdf_url)
            # response = requests.get(pdf_url)
            with urllib.request.urlopen(pdf_url) as r:
                data = r.read()
                file_name = "\\Users\\Peter\\Documents\\PDF_Crawler\\TestOutput\\" + id + ".pdf"
                with open(file_name, 'wb') as f:
                    f.write(data)
                

if __name__ == '__main__':
    main()