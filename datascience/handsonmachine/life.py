import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import sklearn.linear_model
from xlwings.constants import LineStyle


def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]


oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t',
                             encoding='latin1', na_values="n/a")

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]
print(X)
print(type(X))
print(y)
X = [[ 9054.914],
 [ 9437.372],
 [12239.894],
 [12495.334],
 [15991.736],
 [17288.083],
 [18064.288],
 [19121.592],
 [20732.482],
 [25864.721],
 [27195.197],
 [29866.581],
 [32485.545],
 [35343.336],
 [37044.891],
 [37675.006],
 [40106.632],
 [40996.511],
 [41973.988],
 [43331.961],
 [43603.115],
 [43724.031],
 [43770.688],
 [49866.266],
 [50854.583],
 [50961.865],
 [51350.744],
 [52114.165],
 [55805.204]]
y = [6. , 5.6, 4.9, 5.8, 6.1, 5.6, 4.8, 5.1, 5.7, 6.5, 5.8, 6., 5.9, 7.4, 7.3, 6.5, 6.9, 7. , 7.4, 7.3, 7.3, 6.9, 6.8, 7.2, 7.5, 7.3, 7. , 7.5, 7.2]

# Visualize the data
country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')

# plt.show()

# Select a linear model
model = sklearn.linear_model.LinearRegression()

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[22587]]  # Cyprus' GDP per capita
print(model.predict(X_new))  # outputs [[ 5.96242338]])
print(model)
print(model.coef_)
print(model.intercept_)
print(22587 * model.coef_ + model.intercept_)
# X = np.linspace(0, 60000, 1000)
plt.plot(X, model.intercept_ + model.coef_ * X, color='red', linewidth='3', LineStyle='--')
# plt.plot(y, (y - model.intercept_) / model.coef_, "b")
plt.show()
