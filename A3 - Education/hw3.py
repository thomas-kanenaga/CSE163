"""
Thomas Kanenaga
CSE 163 Section AD

This file contains all of the
methods needed to solve the problems of hw3
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
# Your imports here

sns.set()

# Define your functions here


def compare_bachelors_1980(data):
    """
    This method takes a dataframe and computes
    the percentages of men and women who achieved
    a minimum degree of a Bachelor’s degree in 1980.
    The result is a 2 by 2 data frame.
    """

    mask_year = data['Year'] == 1980
    mask_male = data['Sex'] == ('M')
    mask_female = data['Sex'] == ('F')
    mask_degree = data['Min degree'] == ("bachelor's" or "master's")
    filtered_data = data.loc[mask_year & (mask_male | mask_female) &
                             mask_degree, ['Sex', 'Total']]
    return filtered_data


def top_2_2000s(data, sex='A'):
    """
    This method that takes two arguments, the data and
    a sex parameter, and computes the two most commonly
    earned degrees for that given sex between the years
    2000 and 2010 (inclusive) returning them.
    """

    mask_sex = data['Sex'] == sex
    mask_years = (data['Year'] >= 2000) & (data['Year'] <= 2010)
    filtered_data = data[mask_sex & mask_years]
    mean_data = filtered_data.groupby('Min degree')['Total'].mean()
    return mean_data.nlargest(n=2)


def line_plot_bachelors(data):
    """
    This method takes the data and plots a
    line chart of the total percentages of
    all people Sex A with bachelor's Min degree
    over time
    """

    bachelor_data = data[data['Min degree'] == "bachelor's"]
    bachelor_data = bachelor_data[bachelor_data['Sex'] == "A"]
    sns.relplot(data=bachelor_data, x='Year', y="Total", kind="line", ci=None)
    plt.title("Percentage Earning Bachelor's over Time")
    plt.ylabel("Percentage")
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(data):
    """
    This method takes the data and plots a bar chart
    comparing the total percentages of Sex F, M, and
    A with high school Min degree in the Year 2009.
    """

    high_school_data = data[
        (data['Min degree'] == "high school") &
        (data['Year'] == 2009)
        ]

    sns.catplot(data=high_school_data, x='Sex', y='Total', kind='bar')
    plt.title('Percentage Completed High School by Sex')
    plt.ylabel("Percentage")
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(data):
    """
    This method takes the data and plots how the percentage
    of Hispanic people with degrees have changed between 1990–2010
    (inclusive) for high school and bachelor's Min degree.
    """

    degree_1 = data['Min degree'] == "bachelor's"
    degree_2 = data['Min degree'] == "high school"
    time = (data['Year'] >= 1990) & (data['Year'] >= 1990)
    hispanic_min_degree = data.loc[(degree_1 | degree_2) &
                                   time, ["Year", "Hispanic", "Min degree"]]
    sns.relplot(data=hispanic_min_degree,
                x="Year", y="Hispanic", kind="line", hue="Min degree", ci=None)
    plt.title(
        'Pecentage of Hispanic High School and Bachelor Graduates Over Time ')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.xticks(rotation=-45)
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(data):
    """
    This method takes in data and trains a DecisionTreeRegressor
    to predict the percentage of degrees attained for a given Sex,
    Min degree, and Year, returning thetest mean squared error as a float.
    """

    filtered_data = data[['Year', 'Min degree', 'Sex', 'Total']]
    filtered_data = filtered_data.dropna()
    features = filtered_data.loc[:, filtered_data.columns != "Total"]
    features = pd.get_dummies(features)
    labels = filtered_data['Total']
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.20)
    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)
    predictions = model.predict(features_test)
    return mean_squared_error(labels_test, predictions)


def main():

    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    # Call your functions here
    compare_bachelors_1980(data)
    top_2_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
