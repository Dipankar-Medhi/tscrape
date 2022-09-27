from datetime import date, timedelta
import pandas as pd
import typer
from pathlib import Path
from scraper import Scraper

main = typer.Typer()

# save file to data dir
def save_file(tweet_list, filename):
    df = pd.DataFrame(tweet_list, columns=["Date", "User", "Tweet"])
    cwd = Path.cwd() / "data"
    cwd.mkdir(exist_ok=True)
    df.to_csv("data/{}".format(filename))


@main.command()
def scrape(
    # query: str = typer.Argument(
    #     ...,
    #     help="Query to scrape from Twitter."
    # ),
    keyword: str = typer.Option(
        "", help="Keyword to search tweets.", prompt="Enter keyword: "
    ),
    user: str = typer.Option(
        "",
        help="Tweets by a user.",
        prompt="Tweets by username [eg: username]: ",
    ),
    mention: str = typer.Option(
        "",
        help="Get tweets by mentions.",
        prompt="Username mentioned in tweets [eg: username]: ",
    ),
    startdate: str = typer.Option(
        str(date.today() - timedelta(days=365)),
        help="Start scrapping from this day.",
        prompt="Scrape since: ",
    ),
    enddate: str = typer.Option(
        str(date.today()),
        help="Scrape till date.",
        prompt="Scrape till: ",
    ),
    rows: int = typer.Option(
        200,
        help="Number of tweets to scrape from Twitter.",
        prompt="Number of tweets to scrape [eg: 200]: ",
    ),
    filename: str = typer.Option(
        "scrape.csv",
        help="Name of the csv file.",
        prompt="Name of the file [eg: example.csv]: ",
    ),
):
    """Scrape tweets from Twitter."""

    ## custom query
    if user == "":
        query = f"{keyword} (@{mention}) lang:en until:{enddate} since:{startdate}"
    else:
        query = f"{keyword} (from:{user}) (@{mention}) lang:en until:{enddate} since:{startdate}"

    typer.echo("-" * 30)
    typer.echo("Scrapping tweets...")
    typer.echo("-" * 30)

    scraper = Scraper()
    tweet_list = scraper.get_tweets(query, rows)
    print(tweet_list)

    save_file(tweet_list, filename)

    typer.echo("File saved!!!")


if __name__ == "__main__":
    main()
