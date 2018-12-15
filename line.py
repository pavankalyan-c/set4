word_count = 0
file_name = "pk"
with open(file_name,'r') as file:
  for line in file:
    word_count += len(line.split())
print ("number of words : ",word_count)
