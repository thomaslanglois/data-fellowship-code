### Challenge requirements

#### Challenge 1:
To complete this challenge, you will need to:
- [ ] Open a Jupyter notebook
- [ ] Add a title and an overview that describes how this notebook will be used to practice loading different data formats in Python
- [ ] Create a new section to load the [`pandas`](https://pandas.pydata.org/) library (if you're working on your computer instead of a cloud environment, you'll need to make sure it's downloaded already to your device)
- [ ] Download happiness.csv from this repository's [data folder](../../../../data)
- [ ] Use the Pandas function `read_csv()` to load the `happiness.csv` dataset into a variable called `df_csv`
- [ ] Use the function `head()` to visualise the first 12 entries `df_csv`
- [ ] Download `happiness.xlsx` from this repository's [data folder](../../../../data)
- [ ] Use the function `read_excel()` to load the spreadsheet called `happiness` of the `happiness.xlsx` file into a variable called `df_xlsx`
- [ ] Use the function `.tail()` to visualise the last 7 entries of `df_xlsx`
- [ ] Download `happiness.tsv` from this repository's [data folder](../../../../data)
- [ ] Use the function `read_table()` to load the file called `happiness.tsv` into a variable called `df_tsv`
- [ ] Use the function `head()` with no arguments to see how many values you can observe
- [ ] Download `grades.json` from this repository's [data folder](../../../../data)
- [ ] Use the function `read_json()` to load the file called `grades.json` into a variable called `df_json`, specify in the arguments that the orientation, `orient`, is a `table`
- [ ] Check out the last 6 elements of `df_json`

#### Challenge 2:
##### Cleaning the `happiness` database
- [ ] Replace the column names with something more informative, such as `'Country', 'Region', 'Hemisphere', 'HappinessScore', 'HDI', 'GDP_PerCapita', 'Beer_PerCapita', 'Spirit_PerCapita', 'Wine_PerCapita'`
- [ ] Find out the datatype of all the variables with a single line of code of the dataset `happiness` 😱
- [ ] Replace the commas with points in the columns `'HappinessScore'` and `'GDP_PerCapita'`
- [ ] Change the type of variables of the columns `'HappinessScore'` and `'GDP_PerCapita'` to numeric
- [ ] Correct the typos and multiple categories of the variable `'Hemisphere'` so it will only contain three possible values `north`, `south` or `both`

##### Cleaning the `gapminder_data` database
- [ ] Change the name of the variable `'Total 25-54 unemployment (%)'` to `'COUNTRY'`
- [ ] "Unpivot" the database `gapminder_data` using the `.melt()` method, so each observation will be described by three variables: Country name, Year, Total 25-54 unemployment (%). Call that datafile `gmd_melt`
- [ ] Change the column names of `gmd_melt` to `COUNTRY`, `year`, and `25_54_unemployment`
- [ ] Change the format of the variable `year` to numeric
- [ ] Drop any row that contains a `NaN` value using the function `.dropna`. Save that file into `gdm_noNaN`
- [ ] Check out how many elements you dropped using the function `.shape`

#### Challenge 3:
##### Summarizing our data
- [ ] Count how many observations are in the `happiness` dataset using the function `.count()`; save that number in a variable called `totalCounts`
- [ ] Calculate the sum of all the Happiness score for all countries, save that value in a variable called `summation`
- [ ] Calculate the mean with the two numbers above
- [ ] Calculate the arithmetic mean, the median and the mode of `HappinessScore`
- [ ] Calculate the variance, the standard deviation and the interquartile range of `HappinessScore`
- [ ] Calculate the maximum and the minimum value of `HappinessScore`
- [ ] In a single line of code, calculate the mean of all the numeric variables
- [ ] In a single line of code calculate: (a) how many observations there are, (b) the mean, (c) the standard deviation, (d) minimum value, (e) Q1, (f) median, (g) Q3, (h) maximum value. Do this for all the numeric variables in `happiness`; your result has to be a dataframe 🌟🌟🌟
- [ ] Pivot a table to know the average value of all the numeric variables based on (a) `Hemisphere` and (b) `Region`. Save the results in `hemisfere` and `region`, respectively

#### Challenge 4:
##### Summarizing our data visually
- [ ] Import the library `matplotlib.pyplot` as `plt`
- [ ] Import the library seaborn as `sns`
- [ ] Create a vertical boxplot of all the alcohol consumption variables from the dataset `happiness`, set the title of the the plot to `Country Alcohol Consumption`, change the y axis to `Litres per capita (l)`, and change the labels of the x axis to `Beer`, `Spirits`, `Wine`
- [ ] Create a horizontal boxplot of `HappinessScore`, separated by `Hemispheres`. Make the title `Happiness Score in each hemisphere`; change the labels in the y axis to `north`, `both`, and `south`. Change the labels in the x axis to `Happiness Score`
- [ ] Create a vertical violin plot of `GDP_PerCapita`, separated by `Region`, change the title and the labels accordingly ;)
- [ ] Create a scatter plot between `HappinessScore` (dependent variable) and `Wine_PerCapita` (independent variable); change the colour of the data points according to the hemisphere where the country is located
- [ ] Check out the distribution of `HappinessScore` using a histogram
- [ ] Check out the distribution of `HappinessScore` using a density curve
- [ ] Create a plot which contains multiple scatter plots between all the variables and also contains the distribution of the numerical data, coloured by hemisphere 🚀🚀🚀

Remember that you need to type `plt.show()` to see the plots ;)

#### Challenge 5:
##### Filtering our data
### `happiness`
- [ ] Filter the dataset `happiness` by countries that are in both hemispheres; save that subset in a variable called `bothHemispheres` and check the first 3 entries
- [ ] Create a new subset of the dataset `happiness` that includes the countries in which litres of beer consumption per capita are higher than 150; save that in a variable called `beer150` and check the first 3 entries
- [ ] Create a subset dataset of `happiness` that only includes from the second to the seventh column, and contains only the first 35 observations; save that subset in a variable called `subset1`
- [ ] Create a subset dataset of `happiness` that includes only the third and sixth column, and contains only the rows with a `GDP_PerCapita` higher or equal to 40; save it in a variable called `subset2`and check the first 3 entries

### `gmd_melt`
- [ ] Create a subset which only contains `NaN` values; save that subset as `gmd_NaN`
