import pandas as pd
import datetime

def main():
    now = datetime.datetime.now()
    title = "Data on killed and injured Palestinians in Gaza since 07/10/23"
    subtitle = f"Data captured on {now}"

    try:
        # Read the CSV file into a DataFrame
        data = pd.read_csv("data.csv")
        with open("index.html", "w") as f:
            f.write(f"<h1>{title}</h1>\n")
            f.write(f"<h2>{subtitle}</h2>\n")
            # Convert DataFrame to HTML and write it to file
            f.write(data.to_html(index=False))
            # Write explanatory text after the table
            f.write("<p>*Source: Ministry of Health in Gaza</p>\n")
            f.write("<p>Please note that any gaps or missing numbers are a result of unavailable corresponding data</p>\n")
            f.write("<p>Following the collapse of services and communications at hospitals in the North, the MoH in Gaza did not update casualty figures</p>\n")
    except Exception as e:
        print(f"Error reading data: {e}")

if __name__ == "__main__":
    main()
