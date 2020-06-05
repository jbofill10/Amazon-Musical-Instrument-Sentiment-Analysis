import pandas as pd
import Preprocessing, Visualize

from Models import NaiveBayes, RFR, XGBoost

def main():
    df = pd.read_csv('Data/Amazon_Instrument_Reviews/Musical_instruments_reviews.csv')

    # Visualize.run(df)

    train_test_data = Preprocessing.run(df)

    # Holds confusion matrices for visualizations after testing
    results_dict = {}

    results_dict['mnb'] = NaiveBayes.run(train_test_data)
    results_dict['rfr'] = RFR.run(train_test_data)
    results_dict['xgboost'] = XGBoost.run(train_test_data)



if __name__ == '__main__':
    main()