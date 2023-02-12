import numpy as np

def calculate(list):
    if (len(list) !=9):
      raise ValueError("List must contain nine numbers.")
    
    lst=np.array(list)
    print(lst)
  
    mean_row = [lst[[0,1,2]].mean(),lst[[3,4,5]].mean(),lst[[6,7,8]].mean()] 
    mean_column = [lst[[0,3,6]].mean(),lst[[1,4,7]].mean(),lst[[2,5,8]].mean()]
  
    variance_row = [lst[[0,1,2]].var(),lst[[3,4,5]].var(),lst[[6,7,8]].var()]
    variance_column = [lst[[0,3,6]].var(),lst[[1,4,7]].var(),lst[[2,5,8]].var()]
  
    sd_row = [lst[[0,1,2]].std(),lst[[3,4,5]].std(),lst[[6,7,8]].std()]
    sd_column = [lst[[0,3,6]].std(),lst[[1,4,7]].std(),lst[[2,5,8]].std()]
  
    max_row = [lst[[0,1,2]].max(),lst[[3,4,5]].max(),lst[[6,7,8]].max()]
    max_column = [lst[[0,3,6]].max(),lst[[1,4,7]].max(),lst[[2,5,8]].max()]
  
    min_row = [lst[[0,1,2]].min(),lst[[3,4,5]].min(),lst[[6,7,8]].min()]
    min_column = [lst[[0,3,6]].min(),lst[[1,4,7]].min(),lst[[2,5,8]].min()]
  
    sum_row = [lst[[0,1,2]].sum(),lst[[3,4,5]].sum(),lst[[6,7,8]].sum()]
    sum_column = [lst[[0,3,6]].sum(),lst[[1,4,7]].sum(),lst[[2,5,8]].sum()]
    
    return {
      'mean': [mean_column,mean_row,lst.mean()],
      'variance': [variance_column, variance_row, lst.var()],
      'standard deviation': [sd_column, sd_row, lst.std()],
      'max': [max_column, max_row, lst.max()],
      'min': [min_column, min_row, lst.min()],
      'sum': [sum_column, sum_row, lst.sum()]
    }