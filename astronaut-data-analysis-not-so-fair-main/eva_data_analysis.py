import sys
import matplotlib.pyplot as plt
import pandas as pd


def read_json_to_dataframe(input_json):
    """
    Read the data from a JSON file into a Pandas dataframe.
    Clean the data by removing any incomplete rows and sort by data

    Args:
        input_file(str): The path to the Json file.

    Returns:
        eva_df(pd.DataFrame): the cleaned up and sorted data
    """
    print(f"Reading JSON file {input_json}")

    # Read the data from the JSON using pandas
    eva_df = pd.read_json(input_json, convert_dates=["date"])
    # pandas has no int type, therefore converting eva column to float
    eva_df["eva"] = eva_df["eva"].astype(float)
    # Clean the data by removing incomplete rows and sort it by date
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values("date", inplace=True)
    return eva_df


def write_dataframe_to_csv(eva_df, spacewalks_csv):
    """
    Gets a pandas dataframe with the spacewalks data and
    save it in a csv for later.

    Args:
        eva_df(pd.DataFrame): a data frame with the cleaned and sorted space walk data
        spacewalks_csv(str): a csv file path for later

    Returns:
        None
    """
    print(f"Saving to CSV file {spacewalks_csv}")
    # Save dataframe to csv for later analysis
    eva_df.to_csv(spacewalks_csv, index=False)


def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration(str): the duration in H:MM

    Returns:
        duration_hours (float): The duration in hours
    """
    hours, minutes = duration(":")
    duration_hours = (
        int(hours) + int(minutes) / 6
    )  # there is an intentional bug on this line (should divide by 60 not 6)
    return duration_hours


def add_duration_hours_variable(df):
    """
    Add duration in hours (duration_hours) variable to the dataset

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        df_copy (pd.DataFrame): A copy of df_ with the new duration_hours variable added
    """
    df_copy = df.copy()
    df_copy["duration_hours"] = df_copy["duration"].apply(text_to_duration)
    return df_copy


def plot_cumulative_time_in_space(df, graph_file):
    """
    Plot the cumulative time spent in space over years

    Convert the duration column from strings to number of hours
    Calculate cumulative sum of durations
    Generate a plot of cumulative time spent in space over years and
    save it to the specified location

    Args:
        df (pd.DataFrame): The input dataframe.
        graph_file (str): The path to the output graph file.

    Returns:
        None
    """
    print(f"Plotting cumulative spacewalk duration and saving to {graph_file}")
    df = add_duration_hours_variable(df)
    df["cumulative_time"] = df["duration_hours"].cumsum()
    # plotting the cumulative time per year. 'ko-' defines the style of the plot
    plt.plot(df.date, df.cumulative_time, "ko-")
    plt.xlabel("Year")
    plt.ylabel("Total time spent in space to date (hours)")
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()


# main code


def main():
    if len(sys.argv) < 3:
        # https://data.nasa.gov/resource/eva.json (with modifications)
        input_json = open("eva-data.json", "r")
        spacewalks_csv = open("eva-data.csv", "w")
    else:
        input_json = sys.argv[1]
        spacewalks_csv = sys.argv[2]

    spacewalks_plot = "cumulative_eva_graph.png"

    print("--START--")
    # Read the data from JSON file
    eva_df = read_json_to_dataframe(input_json)

    # Convert and export data to CSV file
    write_dataframe_to_csv(eva_df, spacewalks_csv)

    # plot cumulative time
    plot_cumulative_time_in_space(eva_df, spacewalks_plot)


print("--END--")

if __name__ == "__main__":
    main()
