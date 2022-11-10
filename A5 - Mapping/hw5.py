"""
Thomas Kanenaga
CSE 163 AD




"""
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd


def load_in_data(shp_file_name, csv_file_name):
    """
    This method takes two parameters, the filename
    for the census dataset and the filename for the food access dataset.
    it then merges the two datasets on
    CTIDFP00 / CensusTract and returns the result as a GeoDataFrame.
    """
    census_dataset = gpd.read_file(shp_file_name)
    food_access_dataset = pd.read_csv(csv_file_name)
    state_data = census_dataset.merge(food_access_dataset,
                                      left_on='CTIDFP00',
                                      right_on='CensusTract', how='left')
    return state_data


def percentage_food_data(state_data):
    """
    A method take the merged data and returns the percentage of census tracts
    in Washington for which we have food access data. The percentage should
    be a float between 0 and 100.
    """
    # percent census w/ data on food access/ amt census tracts * 100 = percent
    amount_censusTract = len(state_data['CensusTract'])
    non_na_censusTract = len(state_data[state_data['CensusTract'].notnull()])
    percent = (non_na_censusTract / amount_censusTract) * 100
    return percent


def plot_map(state_data):
    """
    A method that that takes the merged data and plots the shapes
    of all the census tracts in Washington in a file map.png.
    """
    state_data.plot()
    plt.title("Washington State")
    plt.savefig("map.png")


def plot_population_map(state_data):
    """
    This method  takes the merged data and plots the shapes of all the
    census tracts in Washington in a file county_population_map.png where
    each county is colored according to population.
    """
    fig, ax = plt.subplots(1)
    state_data.plot(ax=ax, color='#EEEEEE')
    state_data.plot(ax=ax, column='POP2010', legend=True)
    plt.title('Washington Census Tract Populations')
    plt.savefig("population_map.png")


def plot_population_county_map(state_data):
    """
    This method takes the merged data and plots the shapes of all the census
    tracts in Washington in a file county_population_map.png where each county
    is colored according to population.
    """
    fig, ax = plt.subplots(1)
    population_county_data = state_data.dissolve(by="County", aggfunc="sum")
    state_data.plot(ax=ax, color='#EEEEEE')
    population_county_data.plot(ax=ax, column='POP2010', legend=True)
    plt.title('Washington County Populations')
    plt.savefig("county_population_map.png")


def plot_food_access_by_county(state_data):
    """
    This method  takes the merged data and produces 4 plots on the same
    figure showing information about food access across income level.
    It then saves it as a image called county_food_access.png.
    """
    food_access = state_data[['County', 'geometry', 'POP2010',
                              'lapophalf', 'lapop10',
                              'lalowihalf', 'lalowi10']]
    food_access = food_access.dissolve(by="County", aggfunc="sum")
    food_access['lapophalf_ratio'] = (food_access['lapophalf'] /
                                      food_access['POP2010'])
    food_access['lapop10_ratio'] = (food_access['lapop10'] /
                                    food_access['POP2010'])
    food_access['lalowihalf_ratio'] = (food_access['lalowihalf'] /
                                       food_access['POP2010'])
    food_access['lalowi10_ratio'] = (food_access['lalowi10'] /
                                     food_access['POP2010'])
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))
    state_data.plot(ax=ax1, color='#EEEEEE')
    state_data.plot(ax=ax2, color='#EEEEEE')
    state_data.plot(ax=ax3, color='#EEEEEE')
    state_data.plot(ax=ax4, color='#EEEEEE')
    food_access.plot(ax=ax1, column='lapophalf_ratio', legend=True, vmin=0,
                     vmax=1)
    food_access.plot(ax=ax3, column='lapop10_ratio', legend=True, vmin=0,
                     vmax=1)
    food_access.plot(ax=ax2, column='lalowihalf_ratio', legend=True, vmin=0,
                     vmax=1)
    food_access.plot(ax=ax4, column='lalowi10_ratio', legend=True, vmin=0,
                     vmax=1)
    ax1.set_title('Low Access: Half')
    ax3.set_title('Low Access: 10')
    ax2.set_title('Low Access + Low Income: Half')
    ax4.set_title('Low Access + Low Income: 10')
    plt.savefig('county_food_access.png')


def plot_low_access_tracts(state_data):
    """
    This method takes the merged data and plots all census tracts
    considered “low access” in a file low_access.png.
    """
    fig, ax = plt.subplots(1)
    state_data.plot(ax=ax, color='#EEEEEE')
    have_food_access_data = state_data.dropna()
    have_food_access_data.plot(ax=ax, color='#AAAAAA')
    # The threshold for low access in an urban census tract is at least
    # 500 people or at least 33% of the people in the census tract being
    # more than half a mile from a food source.
    state_data['lapophalf_ratio'] = (state_data['lapophalf'] /
                                     state_data['POP2010'])
    urban_low_access = ((state_data['Urban'] == 1) &
                        ((state_data['lapophalf_ratio'] >= 0.33) |
                        (state_data['lapophalf'] >= 500)))
    # The threshold for low access in a rural census tract is at least
    # 500 people or at least 33% of the people in the census tract being
    # more than 10 miles from a food source.
    state_data['lapop10_ratio'] = (state_data['lapop10'] /
                                   state_data['POP2010'])
    rural_low_access = ((state_data['Rural'] == 1) &
                        ((state_data['lapop10_ratio'] >= 0.33) |
                        (state_data['lapop10'] >= 500)))
    state_data[urban_low_access].plot(ax=ax)
    state_data[rural_low_access].plot(ax=ax)
    plt.title("Low Access Census Tracts")
    plt.savefig("low_access.png")


def main():
    state_data = load_in_data(
        '/course/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        '/course/food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
