import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

VIS_ZERO_CRASH = "vis_zero_crash_rec.csv"

def read_data(file): 
    df = pd.read_csv(file)
    return df
    # aaaaaaaaaaaaaaaaaaaaaaa
# ishani was here
def main(): 
    vis_crash = read_data(VIS_ZERO_CRASH)
    print(vis_crash)
main()
