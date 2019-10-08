"""
This file is for testing.
Step 1. Read CSV file by ``from_csv'' function
Step 2. Select a visualization selection method.
Step 3. Select output method, e.g., to_single_html()
Step 4. Check results.
"""

import deepeye_pack
from IPython.core.display import display, HTML

#create a deepeye_pack class that wraps everything
dp = deepeye_pack.deepeye('demo') # the name here doesn't actually matter

#The followings are test datasets
#User can choose one to test

# file = './datasets/FlyDelay_NewYork.csv'
# file = './datasets/Foreign Visitor Arrivals By Purpose(Jan-Dec 2015).csv'
# file = './datasets/HollywoodsMostProfitableStories.csv'
# file = './datasets/MostPopularBaby_Names(NewYork).csv'
# file = './datasets/SummerOlympic_1896_2008.csv'
# file = './datasets/electricityConsumptionOfEasternChina.csv'
# file = './datasets/happinessRanking(2015-2016).csv'
file = './datasets/titanicPassenger.csv'

#read the datasets
dp.from_csv(file)

# choose one from three ranking function

# dp.learning_to_rank()
dp.partial_order()
#dp.diversified_ranking()

# output functions
# can use several different methods at the same time

dp.to_single_html()
#dp.to_single_json()
#dp.to_multiple_htmls()
#dp.to_list()
#dp.to_print_out()
#dp.to_multiple_jsons()

# dp.show_visualizations().render_notebook()