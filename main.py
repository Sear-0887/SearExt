def isInt(t):
  i = 0 #Reset
  try:
    i = int(t) #INT DETECT
  except:
    return False #String / List / Tuples
  else:
    if len(str(t)) == len(str(i)):
      return True 
    else:
      return False #Float
