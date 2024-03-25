import json
import datetime

def write_results(new_data, folder, filename='results.json'):

    results_dict = {"dataframe":"","normalized":"","timestamp":"","model":"",
                "explained variance score":"","mae score":"","mse score":"","r2 score":"", "mean fit time":""}

    results_dict["dataframe"] = new_data["dataframe"]
    results_dict["normalized"] = new_data["normalized"]
    now = datetime.datetime.now()
    results_dict["timestamp"] = now.strftime("%Y/%m/%d %H:%M:%S")
    results_dict["model"] = new_data["model"]
    results_dict["explained variance score"] = new_data["explained variance score"]
    results_dict["mae score"] = new_data["mae score"]
    results_dict["mse score"] = new_data["mse score"]
    results_dict["r2 score"] = new_data["r2 score"]
    results_dict["mean fit time"] = new_data["mean fit time"]


    where = folder + '/' + filename
    with open(where, 'r+') as file:
        file_data = json.load(file)
        file_data.append(results_dict)
        file.seek(0)
        json.dump(file_data, file, indent=4)

    return results_dict