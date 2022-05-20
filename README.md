# goodreads_stats

Tool for generating some goodreads stats. Just follow https://help.goodreads.com/s/article/How-do-I-import-or-export-my-books-1553870934590 to download .csv file and see if you rate books higher than the average goodreads reader.

```
goodreads-stats ❯ python3 goodreads.py -f ./default.csv
Your average rating of books you've read: 3.93
Goodread users average rating of books you've read: 3.64

Most liked comparatively: The Undefeated - Ernest Hemingway
Most disliked comparatively: Quidditch Through the Ages (Hogwarts Library) - J.K. Rowling

No correlation found between page count and your rating: -0.018

You've read a total of 41408 pages
Assuming a reading pace of 2 minutes per page, means you've read for 1380 hours, or 57.5 days
```
