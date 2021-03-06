import requests

class NRC_HANDLER:
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

    def build_nrc_wb_request(self, query, qn, tab):
        # TODO: build an example of the request that is included in this and test it
        base_url = "http://adams.nrc.gov/wba/services/search/advanced/nrc?"
        request_url = base_url + "q=" + query
        request_url = request_url + "&qn=" + qn + "&tab=" + tab
        return requests.get(url=request_url).content


'''Example 1: Find all speeches for which Macfarlane appears in the Author Name property. Sort
the results alphabetically by document title in ascending order.
Working query - Query link
Query formatted for screen display
http://adams.nrc.gov/wba/services/search/advanced/nrc?q=(
    mode:sections,sections:(
        filters:(
            public-library:!t),
        options:(
            within-folder:(enable:!f,insubfolder:!f,path:'')
        ),properties_search_all:!(
            !(AuthorName,starts,Macfarlane,''),
            !(DocumentType,starts,Speech,'')
        )
    )
)&qn=New&tab=advanced-search-pars&s=%24title&so=ASC'''



instance_of_nuclear = NRC_HANDLER()
instance_of_nuclear.run_examples()
instance_of_nuclear.print_examples()
