def create_matrix(cols_count, rows_count):
   matrix = []
   i = 0
   for row_index in range(rows_count):
      row = []
      for col_index in range(cols_count):
         row.append(i)
         i += 1
      matrix.append(row)
   return matrix
   
def create_file(matrix, path):
   file = open(path, 'w')
   for row in matrix:
      line = ''
      for number in row:
         line += str(number) + '\t'
      line += '\n'
      file.write(line)
   file.close()

matrix = create_matrix(10,10)
create_file(matrix, 'Ваня.txt')