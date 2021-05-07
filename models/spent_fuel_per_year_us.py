

class year_of_spent_fuel:
    def __init__(self):
        self.year = list(range(2))
        self.number_of_assemblies = list(range(2))
        self.initial_uranium_content = list(range(2))
        self.average_burnup = list(range(2))
        self.all_discharged_assemblies = list(range(2))
        self.year[1] = "Year : "
        self.number_of_assemblies[1] = "Number of assemblies : "
        self.initial_uranium_content[1] = "Initial Uranium Content : "
        self.average_burnup[1] = "Average Burnup (GWDt/MTU) : "
        self.all_discharged_assemblies[1] = "All Discharged Assemblies : "

    def __repr__(self):
        rO = f'US Spent Fuel For {self.year[1]}, {self.number_of_assemblies[1] + self.number_of_assemblies[0]}'
        rO = rO + f' {self.initial_uranium_content[1] + self.initial_uranium_content[0]}'
        rO = rO + f' {self.average_burnup[1] + self.average_burnup[0]}'
        rO = rO + f' {self.all_discharged_assemblies[1] + self.all_discharged_assemblies[0]}'
        return rO

    def setData(self, a, b, c, d, e):
        self.year[0] = a
        self.number_of_assemblies[0] = b
        self.initial_uranium_content[0] = c
        self.average_burnup[0] = d
        self.all_discharged_assemblies[0] = e
