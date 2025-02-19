# #How to solve any pattern programs in python.
# #Requirements to print the patterns.
# '''
# 1.	First we have to follow orderly for row by row. When row completes there is no possibility to go back to that row.
# 2.	Second decide how many rows of pattern you want to print. (Ex: n=5 then range is(1,6)).
# 3.	If we want to print one “*” then we give (print(“*”)) or if we want to print n number of “*” the we give (print(“*” * n)).
# By range like below.'''

# #Stage 1
# n=5
# for j in range(n):
#     print("*")
    
# '''
# *
# *
# *
# *
# *
# '''

# #Stage 2
# #But if we want to print horizontally then we use like below.
# n=5
# for j in range(n):
#     print("*",end=" ")
    
# '''
# * * * * *
# '''

# #Stage 3
# #If we want to run the above pattern multiple times we have to use another loop.
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
       
# '''* * * * * * * * * * * * * * * * * * * * * * * * *'''

# #But they print in same line then we use print() to break the row.
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()
        
# '''
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# '''

# #If we want to print increasing triangle patter then we have to set the inner loop. The outer loop pattern indicates no.of rows.

# #LOW TO HIGH
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
        
# '''
# * 
# * * 
# * * * 
# * * * * 
# * * * * *  
# '''

# #If we want to print decreasing triangle patter then we have to set the inner loop. The outer loop pattern indicates no.of rows.

# #HIGH TO LOW
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
        
# '''
# * * * * * 
# * * * * 
# * * * 
# * * 
# *  
# '''

# #Right sided Low to High Triangle:
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
    
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
    
# '''
#           * 
#         * * 
#       * * * 
#     * * * * 
#   * * * * * 
# '''

# #Right sided High to low Triangle:
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
    
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# '''
#   * * * * * 
#     * * * *
#       * * *
#         * *
#           *
# '''

# #WAP to print the pyramid pattern
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# '''
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
# '''

# #Hill Pattern:
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# '''
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
# '''

# #Reverse Hill Pattern:
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
    
#     for j in range(i,n):
#         print("*",end=" ")
    
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()

# '''
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 
# '''

# #Diamond Pattern:
# #Hill Pattern + Reverse Hill Pattern = Diamond Pattern

# n=5
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
    
#     for j in range(i,n):
#         print("*",end=" ")
    
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()

# '''
#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *
# '''

# ###Wap to print first row and last row *'s and middle are spaces
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# '''
# * * * * * 



# * * * * *
# '''

# ###Wap to print first column and last column *'s and middle are spaces
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# '''
# *       * 
# *       * 
# *       * 
# *       * 
# *       *
# '''

# ###Wap to print Middle column and Middle row as like + print the  *'s.
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# '''
#     *     
#     *     
# * * * * * 
#     *     
#     *     
# '''

# ###Wap to print Middle diagonals as like X print the  *'s.
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# '''
# *       * 
#   *   *   
#     *     
#   *   *   
# *       *     
# '''

# #Wap to print zero shape *'s
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# '''
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 
# '''

# ###Wap to print below pattern.
# '''
# * 
# * * 
# *   * 
# *     * 
# * * * * * 
# '''
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==4 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# #Wap to print below pattern
# '''
# * * * * * 
# *     *
# *   *
# * *
# *
# '''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==i or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# ###WAP to print below pattern
# '''
#           * 
#         *   * 
#       *       * 
#     *           * 
#   *               * 
# '''
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         if j==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     for j in range(i+1):
#         if i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 
    
# #Wap to print below pattern
# '''
#   *                   *   
#     *               *   
#       *           *   
#         *       *   
#           *   *   
#             *
# '''
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         if j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     for j in range(i,n):
#         if j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()