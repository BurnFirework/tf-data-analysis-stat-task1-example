import pandas as pd
import numpy as np


chat_id = 860138765

def solution(x: np.array) -> float:
    t = 66.0
    l = np.sum(x) / (t * len(x))
    return l
