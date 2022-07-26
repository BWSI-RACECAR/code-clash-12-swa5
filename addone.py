"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #12 - One Up! (addone.py)


Author: Paul Thai

Difficulty Level: 6/10

Background: Do you know how to add? Good! I have just the question for you! 
Most people know how to add by one, but can you add by one in this problem???

Prompt: Given an array, add one to the ones column!

Constraints: You cannot map/join the list into a single number, add one, and then turn it back into a list. 
That's cheating (because I have done it before...) so you must modify the list itself. Be careful of place values! 

Test Cases:
a = [1, 2, 3]; output = [1, 2, 4]
a = [9]; output = [1,0]
a = [1, 4, 5, 9]; output = [1, 4, 6, 0]
"""

class Solution:
    def addOne(self,ary):
        # type ary: list
        # return type: list

        # TODO: Write code below to return a list "ary" with the solution to the prompt

        lnt = len(ary)-1 

        for i in range(lnt, -1, -1):
            if ary[i] == 9: 
                ary[i] = 0

                if i == 0: 
                    ary.insert(i,1)
                    return ary

            else: 
                ary[i] += 1
                return ary

            return ary

            



        # length = len(ary) - 1

        # if length == 0: 
        #     if ary[length] == 9: 
        #         return [1,0]
            
        #     else: 
        #         ary[length] += 1
        #         return ary
        # case = False 
        # change = True

        # while ary[length] == 9:
           
        #     ary[length] = 0

        #     length -= 1

        #     case = True
        #     change = False


        # if case: 
        #     ary[length] += 1

        # if change:
        #     ary[length] += 1

        # return ary

       
       
        # length = len(ary)
        # modify = False
        
        # if 9 in ary:
        #     modify = True

        # if modify: 
        #     index = ary.index(9)

        #     if index == (length-1):
        #         ary[index-1] += 1 
        #         holder = ary[index-1] 
        #         ary[index] = 0 

        #     iter = 1
        #     while True:
                
        #         if ary[iter] == holder: 
        #             break
        #         ary[iter] = 0 
        #         iter += 1

        #     return ary



        # ary[length-1] += 1

        # return ary 

        # length = len(ary) - 1

        # while(ary[length]==9):
        #     ary[length] = 0
        #     length -= 1

        
        # if length == 0:
        #     ary [1] + ary
        
        # else: 
        #     ary[length] += 1


        # return ary 


        



        
        
        

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.addOne(array)
    print(ans)

if __name__ == "__main__":
    main()
