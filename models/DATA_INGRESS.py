import models.location as location
import models.spent_fuel_per_year_us as spent_fuel

class DATA_INGRESS():
    def __init__(self):
        self.data_for_export = list()
        self.data_for_export_spent_fuel_per_year_us = list()

    def load_data(self, filename):
        with open(filename) as f:
            return f.readlines()

temp_data_ingress = DATA_INGRESS()
temp_ingress_data = temp_data_ingress.load_data("../data_lists/GLOBAL_ENERGY_OBSERVITORY_list_of_nuclear_reactors_2018.txt")
for count, x in enumerate(temp_ingress_data, 0):
    if(count % 4 ==0):
        tempLocation = location.general_location()
        tempLocation.design_capacity = temp_ingress_data[count+1].replace('\n', '')
        tempLocation.common_name_global_energy_observatory = temp_ingress_data[count][1:].replace('\n', '')
        tempLocation.country = temp_ingress_data[count + 2].replace('\n', '')
        tempLocation.state = temp_ingress_data[count + 3].replace('\n', '')
        temp_data_ingress.data_for_export.append(tempLocation)


temp_ingress_data = temp_data_ingress.load_data("../data_lists/NRC_US_list_of_nuclear_reactors_2021.txt")
for count, x in enumerate(temp_ingress_data, 0):
    if(count % 9 == 0):
        tempLocation = location.general_location()
        tempLocation.common_name = x.replace('\n', '')
        tempLocation.docket_number = temp_ingress_data[count + 1].replace('\n', '')
        tempLocation.license_number = temp_ingress_data[count + 2].replace('\n', '')
        tempLocation.reactor_type = temp_ingress_data[count + 3].replace('\n', '')
        tempLocation.owner = temp_ingress_data[count + 4].replace('\n', '')
        tempLocation.NRC_region = temp_ingress_data[count + 5].replace('\n', '')
        temp_data_ingress.data_for_export.append(tempLocation)

temp_ingress_data = temp_data_ingress.load_data("../data_lists/SCRAPED_EIA_list_of_US_nuclear_reactors_2018.txt")
for count, x in enumerate(temp_ingress_data, 0):
    if(count % 10 == 0):
        tempLocation = location.general_location()
        tempLocation.common_name = x.replace('\n', '')
        tempLocation.state = temp_ingress_data[count + 1].replace('\n', '')
        tempLocation.reactor_type = temp_ingress_data[count + 2].replace('\n', '')
        tempLocation.reactor_vendor = temp_ingress_data[count + 3].replace('\n', '')
        tempLocation.core_size = temp_ingress_data[count + 4].replace('\n', '')
        tempLocation.license_expiration_date = temp_ingress_data[count + 6].replace('\n', '')
        tempLocation.retirement = temp_ingress_data[count + 8].replace('\n', '')
        temp_data_ingress.data_for_export.append(tempLocation)

temp_ingress_data = temp_data_ingress.load_data("../data_lists/SCRAPED_EIA_list_of_spent_fuel_per_year_US.txt")
for count, x in enumerate(temp_ingress_data, 0):
    if(count % 11 == 0):
        temp_fuel_count = spent_fuel.year_of_spent_fuel()
        if count > 11 and count < 500:
            temp_fuel_count.setData(temp_ingress_data[count - 4], temp_ingress_data[count - 3], temp_ingress_data[count - 2], temp_ingress_data[count - 1], temp_ingress_data[count])



