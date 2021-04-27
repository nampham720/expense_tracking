import data_to_file
import visualise_budget
import statistics
import pandas as pd

txt_file = "Apr.txt"
data_to_file.display_categories(out=True)
data_to_file.write_data(txt_file)
visualise_budget.visualise(txt_file)
statistics.stats_generate(txt_file)
