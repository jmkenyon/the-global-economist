# By Joshua Kenyon

import random
import matplotlib.pylab as plt


class GdpGrowth(object):
    def __init__(self, start_gdp, countries):
        self.start_gdp = start_gdp
        self.countries = countries

    def growth_model(self):
        # data for all countries will be stored in this list
        list_of_countries = []
        # to ensure that all countries start on the same start GDP
        fixed_gdp = self.start_gdp
        # list of possible percentage growth rates
        possible_growth = [-2, -1, 0, 1, 2, 3, 4]
        # iterate through each country
        for country in range(self.countries):
            end_gdp = self.start_gdp
            # a list of an individual country's end gdp for each year
            country_data = []
            # 34 years of growth
            for i in range(34):
                # 1 time step of gdp change
                end_gdp += self.start_gdp * (random.choice(possible_growth)/100)
                self.start_gdp = end_gdp
                country_data.append(round(end_gdp, 2))
            # adding each country's gdp data to the list of all countries
            list_of_countries.append(country_data)
            # initialize to same start gdp for next country
            self.start_gdp = fixed_gdp
        return list_of_countries

    def best(self, list_of_countries):
        # works out the highest end growth rate for all countries
        best = list_of_countries[0][33]
        best_country = 0
        for j in range(self.countries):
            if list_of_countries[j][33] > best:
                best = list_of_countries[j][33]
                best_country = j
        return list_of_countries[best_country]

    def worst(self, list_of_countries):
        # works out the lowest end growth rate for all countries
        worst = list_of_countries[0][33]
        worst_country = 0
        for j in range(self.countries):
            if list_of_countries[j][33] < worst:
                worst = list_of_countries[j][33]
                worst_country = j
        return list_of_countries[worst_country]

    def plot(self, top, low):
        # plotting the graph
        plt.figure("growth rate")
        plt.clf()
        plt.plot(top, label="Highest")
        plt.plot(low, label="Lowest")
        plt.xlabel("Year")
        plt.ylabel("GDP")
        plt.legend()
        plt.title("Highest vs Lowest GDP Growth")
        plt.show()


countries_data = GdpGrowth(100, 195)
data_of_all_countries = countries_data.growth_model()
best = countries_data.best(data_of_all_countries)
worst = countries_data.worst(data_of_all_countries)
print(countries_data.plot(best, worst))
