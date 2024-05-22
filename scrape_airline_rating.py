from bs4 import BeautifulSoup
import csv

# data scraped from https://www.worldairlineawards.com/worlds-top-100-airlines-2023/
with open("airline_rating.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")
airline_divs = soup.find_all("div", class_="row mb-2 awards-list")

rank = []

for div in airline_divs:
    ranking = div.find(
        "h6", class_="mb-0 text-responsive-h4 font-weight-regular"
    ).text.strip()
    airline_name = div.find("h4", class_="mb-0 text-responsive-h4").text.strip()
    rank.append(airline_name)

"""
store the airline rank as a score as csv.
the score will be generated from 100 to 1.
airline with rank 1 will have score 100, and so on.
"""


def calculate_score(rank, total_ranks):
    return 101 - ((rank - 1) / total_ranks) * 100


with open("airline_scores.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["airline_name", "rank", "score"])

    total_ranks = len(rank)

    for i, airline in enumerate(rank, 1):
        score = calculate_score(i, total_ranks)
        writer.writerow([airline, i, score])

print("Scores saved to airline_scores.csv")
