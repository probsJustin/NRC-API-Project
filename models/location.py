

class general_location():
    def __init__(self):
        self.cordinates = dict()
        self.common_name = ""
        self.common_name_global_energy_observatory = ""
        self.government_owner = ""
        self.state = ""
        self.province = ""
        self.country = ""
        self.design_capacity = ""
        self.docket_number = ""
        self.license_number = ""
        self.reactor_type = ""
        self.location = ""
        self.owner = ""
        self.NRC_region = ""

    def __repr__(self):
        if self.common_name == "":
            return f'{self.common_name_global_energy_observatory}, {self.country}, {self.state}, {self.design_capacity}'
        else:
            return f'{self.common_name}, {self.country}, {self.state}, {self.design_capacity}'


    def returnCordinates(self):
        return self.cordinates

    def returnGovName(self):
        return self.government_owner

    def returnStateName(self):
        return self.state

    def returnProvice(self):
        return self.province

    def returnCountry(self):
        return self.country

    def returnCommonName(self):
        return self.common_name

    def setCordinates(self, func_cordinates):
        self.cordinates = func_cordinates
        if(self.cordinates == func_cordinates):
            return True
        else:
            return False

    def setGovName(self, func_name):
        self.government_owner = func_name
        if(self.government_owner == func_name):
            return True
        else:
            return False

    def setStateName(self, func_statename):
        self.state = func_statename
        if(self.state == func_statename):
            return True
        else:
            return False

    def setProvince(self, func_provinceName):
        self.province = func_provinceName
        if(self.province == func_provinceName):
            return True
        else:
            return False

    def setCountry(self, func_countryName):
        self.country = func_countryName
        if(self.country == func_countryName):
            return True
        else:
            return False

    def setCommonName(self, func_commonName):
        self.common_name = func_commonName
        if(self.common_name == func_commonName):
            return True
        else:
            return False
