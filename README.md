![tscrape.png](images/tscrape.png)

A simple command line tool for Data Scientists to scrape tweets without using the Twitter API.

---

## Tools and libraries used
- [typer](https://typer.tiangolo.com/)
- pandas
- [snscrape](https://github.com/JustAnotherArchivist/snscrape)

## How to use
1. Clone the repository into your local machine.
   ```
   git clone https://github.com/Dipankar-Medhi/tscrape.git
   ```

2. Make a virtual environemnt.
   ```
   python -m venv venv
   ```
3. Activate the virtual environment
   ```
   venv/Scripts/activate
   ```
4. Install the dependencies.
    ```
    pip install -r requirements.txt
    ```
5. Open a terminal inside the current directory and run
    ```
    $ python main.py
    ```
6. Enter the optional arguments.
   ```
   $ python main.py

   Enter the keyword: <keyword>
   Tweets by username: <username>
   Username mentioned in the tweets: <mentioned-usermane>
   Scrape since: <start-date>
   Scrape till: <end-date>
   Number of tweets to scrape: <tweets-number>
   Name of the file: <output-file-name.csv>
   ```
7. All the downloaded tweets will be saved inside the `data` directory as `csv` files.
8. CSV file contains the `date`, `username` and `tweets` columns.
