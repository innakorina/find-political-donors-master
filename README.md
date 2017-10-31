# The summary of my approach
1. Load first line and convert it into a single row data frame.
2. Load next line and convert it into a single row data frame as well, and concatenate them together.
3. Keep reading new lines as data frames and continue to stack/append them into one big data frame.
4. At each iteration calculate running median, number of occurrences and sum for each ID-zip pairs.
5. Compare results of step 4 with the previous values (from previous iteration). Check for updates, if any changes- append changes to "medianvals_by_zip.txt".
6. From the last iteration use final data frame to calculate the median, number of occurrences and sum for each pair ID-date and save results into the "medianvals_by_date.txt".

# Libraries
[Pandas](http://pandas.pydata.org/)
Sys

# Tools
Pandas.groupby() - for grouping ID-Zip, ID-date pairs.

# How to run
Put “itcont.txt” file containing  raw data into “input” subfolder.
Run the “run.sh” shell command.

