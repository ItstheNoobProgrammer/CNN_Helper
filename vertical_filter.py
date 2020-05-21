# Given Input Matrix and Filter Find the Output Matrix

#Input Matrix of size 6X6
mat = [[0,0,0,1,1,1],
       [0,0,0,1,1,1],
       [0,0,0,1,1,1],
       [0,0,0,1,1,1],
       [0,0,0,1,1,1],
       [0,0,0,1,1,1]]

#Filter Matrix of Size 4X4
ftr = [[1,0,-1],
       [2,0,-2],
       [1,0,-1]]
       
#Counter to move the filter virtically and horizontally       
col_inc = 0;
row_inc = 0;

#Variable to store result
res = 0

#iter for row movement 
#(o to 4 beacause last two rows are descarded when filter is placed)
for row_inc in range(0,4):
  #iter for col movment
  for col_inc in range(0,4):
    #iter to access row elements of 3X3 sub matrix
    for i in range(0+row_inc,3+row_inc):
      #iter to access col elements of 3X3 sub matrix
      for j in range (0+col_inc,3+col_inc):
        #nested loop because filter is at fixed pos so to reset index back to 0 to 3  
        if(row_inc != 0 and col_inc == 0):
          res = res + (mat[i][j]*ftr[i-row_inc][j])
        elif(row_inc == 0 and col_inc != 0):
          res = res + (mat[i][j]*ftr[i][j-col_inc])
        elif(row_inc != 0 and col_inc != 0):
          res = res + (mat[i][j]*ftr[i-row_inc][j-col_inc])
        else:
          res = res + (mat[i][j]*ftr[i][j])
    #print the result        
    print("res=",res)
    #reset the result
    res = 0
