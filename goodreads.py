import pandas as pd
import math
import argparse

parser = argparse.ArgumentParser(description='Calculate some goodreads stats')
parser.add_argument('-f', '--file', metavar='F', type=str, default='./default.csv',
    help='a file path to a csv file exported from goodreads')

args = parser.parse_args()
file = args.file


df = pd.read_csv(file)
df = df[df['Exclusive Shelf'].eq('read')]
df = df[df['My Rating'].ge(1)]

average_rating = round(df['Average Rating'].mean(),2)
my_rating = round(df['My Rating'].mean(),2)

diff = df['Average Rating'] - df['My Rating']
outlier_positive_idx = diff.idxmax()
outlier_negative_idx = diff.idxmin()

print("Your average rating of books you've read:", average_rating)
print("Goodread users average rating of books you've read:", my_rating,'\n')

print("Most liked comparatively:", df['Title'][outlier_negative_idx], "-", df['Author'][outlier_negative_idx])
print("Most disliked comparatively:", df['Title'][outlier_positive_idx], "-", df['Author'][outlier_positive_idx],'\n')


## calculate the correlation between page size and rating
corr = df['My Rating'].corr(df['Number of Pages'])
tot_pages = df['Number of Pages'].sum()

if(abs(corr) < 0.2):
    print("No correlation found between page count and your rating:", round(corr,3))
else:
    print("There are some correlation between page count and your rating:", round(corr,3))

print('')
print("You've read a total of", math.floor(tot_pages), "pages")
hrs_read = math.floor(tot_pages * 2/60)
days_read = hrs_read / 24
print("Assuming a reading pace of 2 minutes per page, means you've read for", math.floor(tot_pages * 2/60) ,"hours, or", days_read, "days")