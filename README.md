# PesScraper

## Overview
PesScraper is a Python script designed to scrape data of PES University students based on specified parameters such as campus, branch, join date, and a range of student SRNs. The scraped data includes student names, PRNs, sections, and semesters. The information is then saved in a CSV file for easy analysis and reference.

## How to Use

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/ExIntercept/PesScraper.git
    cd PesScraper
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Script:**
    ```bash
    python scraper.py
    ```

4. **Enter the Required Information:**
   - Choose the campus (EC or RR).
   - Specify the branch.
   - Enter the join date.
   - Define the range of student SRNs (start and stop).

5. **Results:**
   The script will scrape the specified data and save it in a CSV file named `output_data.csv` in the same directory.

## Parameters

- **Campus Options:**
  - EC
  - RR

- **Branch Options:**
  - Specify the branch of interest (e.g., CS, EC, ME, etc.).

- **Join Date:**
  - Enter the join year in the format requested (e.g.21,22,23).

- **Range of Student SRNs:**
  - Define the range of SRNs to scrape (.e.g., 1 to 112)
-**Example**
  -Run the python script. If the input for campus is RR, Date is 23, Branch is CS, Start is 1 and Stop is 112, it will scrape IDs from PES1UG23CS001 to PES1UG23CS112

## Output
The scraped data will be saved in a CSV file named `output_data.csv` in the same directory as the script.

## Support and Contribution
For issues or feature requests, please open an issue on the [GitHub repository](https://github.com/ExIntercept/PesScraper). Contributions are welcome!

## License
This project is licensed under the [MIT License](LICENSE).
