import requests

# Nuclear Information Gathering API Test
# Nuclear Regulatory Commission
# Info A: https://www.nrc.gov/developer.html
# International Atomic Energy Agency
# Info B: https://www.iaea.org/resources/databases/power-reactor-information-system-pris

# Related pypi modules 'nrc_scrape' https://pypi.org/project/nrc-scrape/
# Related pypi modules 'NuclearTools' https://pypi.org/project/NuclearTools/
# Related pypi modules 'pyrk' https://bids.berkeley.edu/resources/videos/pyrk-python-package-nuclear-reactor-kinetics

class NuclearInformation:
    def __init__(self):
        self.NRC = "Nuclear Regulatory Commission"
        self.information = dict()
        # Operating Reactor Inspection Reports
        self.example_NRC_ORI = "https://adams.nrc.gov/wba/services/search/advanced/nrc?q=(mode:sections,sections:(filters:(public-library:!t),properties_search:!(!(DocumentType,infolder,%27inspection+report%27,%27%27),!(DocketNumber,infolder,%2705000%27,%27%27),!(AuthorAffiliation,infolder,NRC/NRR,%27%27)),single_content_search:%27safety+valve%27))&qn=New&tab=content-search-pars&s=$size&so=DESC"
        # Part 21 Component Defect Reports
        self.example_NRC_CDR = "https://adams.nrc.gov/wba/services/search/advanced/nrc?q=(mode:sections,sections:(filters:(public-library:!t),properties_search:!(!(DocumentType,ends,%27Part+21+Correspondence%27,%27%27),!(AuthorAffiliation,infolder,NRC/NRR,%27%27)),single_content_search:%27safety+valve%27))&qn=New&tab=content-search-pars&s=$size&so=DESC"
        # Web Based ADAMS Document Library
        self.example_NRC_ADAMS = "https://adams.nrc.gov/wba/services/search/advanced/nrc?q=(mode:sections,sections:(filters:(public-library:!t),properties_search_any:!(!(DocumentType,ends,%27Enforcement+Action%27,%27%27)),single_content_search:%27Gamma+Knife%27))&qn=New&tab=content-search-pars&s=PublishDatePARS&so=ASC"

    def update_resource(self, func_request_url):
        return requests.get(url=func_request_url).content

    def run_examples(self):
        self.information[self.NRC + " example ADAMS"] = self.update_resource(self.example_NRC_ADAMS)
        self.information[self.NRC + " example CDR"] = self.update_resource(self.example_NRC_CDR)
        self.information[self.NRC + " example ORI"] = self.update_resource(self.example_NRC_ORI)

    def print_examples(self):
        for x in self.information:
            print(f"[{x}] : ")

instance_of_nuclear = NuclearInformation()
instance_of_nuclear.run_examples()
instance_of_nuclear.print_examples()