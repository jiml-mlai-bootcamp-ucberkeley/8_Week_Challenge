
from print_more_stuff import print_more_stuff

import numpy as np
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.feature_selection import SequentialFeatureSelector, RFE, SelectFromModel
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# Create models and feature selections in one file instead of each Notebook

def dosomething(config):
    
    kind = config["kind"]
    title = config["title"]
    df = config["df"]
    features = config["features"]
    target = config["target"]
    best_params = {}
    
    if config["best_params"]:
        best_params = config["best_params"]
    

    num_features_to_select = len(features)-1
    random_state_value = 42
    grid_params = {}
    
    estimator = LinearRegression()
    
    match kind:
        case "Decision Tree":
            estimator = DecisionTreeRegressor(**best_params)
        case "Ada Boost":
            estimator = AdaBoostRegressor(**best_params)
        case "Gradient Boosting":
            estimator = GradientBoostingRegressor(**best_params)
        case "Hist Gradient Boosting":
            estimator = HistGradientBoostingRegressor(**best_params)
        case "Random Forest":
            estimator = RandomForestRegressor(**best_params)
        case "KNearset Neighbors":
            estimator = KNeighborsRegressor(**best_params)
        case "Lasso":
            estimator = Lasso(**best_params)
        case "Linear":
            estimator = LinearRegression()
        case "Ridge":
            estimator = Ridge(**best_params)
        case "Polynomial":
            estimator = Pipeline([
                ('poly_features', PolynomialFeatures()), 
                ('poly_model', LinearRegression(fit_intercept=True))
            ])
            grid_params = best_params
    
    X = df[features]
    y = df[target]
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state_value)
    
    
    something_gscv = GridSearchCV(estimator,param_grid=grid_params)
    something_model = something_gscv.fit(X_train,y_train)
    something_predict = something_model.predict(X_test)
    
    pms_config = {
        "title":title, 
        "y_param":y_test, 
        "predictions":something_predict, 
        "gscv":something_gscv
    }
    
    results = print_more_stuff(pms_config)
    rtnval = {"results":results, "predictions":something_predict}
    
    return rtnval