import pandas as pd
import datetime


def main():
    now = datetime.datetime.now()
    title = "Data on killed and injured Palestinians in Gaza since 07/10/23"
    subtitle = f"Data captured on {now}"

    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv("data.csv")
        with open(
            "index.html", "w"
        ) as f:  # with avoids needing to explicitly close file
            f.write(f"<h1>{title}</h1>")
            f.write(f"<h2>{subtitle}</h2>")
            f.write(data.to_html(index=False))
    except Exception as e:
        print(f"Error reading data: {e}")


if __name__ == "__main__":
    main()
