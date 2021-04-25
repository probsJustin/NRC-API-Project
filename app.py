import requests

# Nuclear Information Gathering API Test
# Nuclear Regulatory Commission
# Info A: https://www.nrc.gov/developer.html
# International Atomic Energy Agency
# Info B: https://www.iaea.org/resources/databases/power-reactor-information-system-pris

class NuclearInformation:
    def __init__(self):
        self.information = dict()
        self.exampleRequestUrl = "https://adams.nrc.gov/wba/services/search/advanced/nrc?q=(mode:sections,sections:(filters:(public-library:!t),properties_search:!(!(DocumentType,infolder,%27inspection+report%27,%27%27),!(DocketNumber,infolder,%2705000%27,%27%27),!(AuthorAffiliation,infolder,NRC/NRR,%27%27)),single_content_search:%27safety+valve%27))&qn=New&tab=content-search-pars&s=$size&so=DESC"

    def getInfoFromNRC(self):
        return requests.get(url=self.exampleRequestUrl).content

    def update(self):
        print(self.getInfoFromNRC())

instance_of_nuclear = NuclearInformation()
instance_of_nuclear.update()