import pandas as pd
import datetime

def main():
    now = datetime.datetime.now()
    title = "Data on killed and injured Palestinians in Gaza since 07/10/23"
    subtitle = f"Data captured on {now}"

    print(f"<h1>{title}</h1>")
    print(f"<h2>{subtitle}</h2>")

    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv("data.csv")
        f = open("index.html", "w")
        f.write(data.to_html(index=False)) 
        f.close()
    except Exception as e:
        print(f"Error reading data: {e}")

if __name__ == "__main__":
    main()
