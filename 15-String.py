## String
##
long_string = "i will catch you if you fall - the floor"
print(long_string[0])  # first element
print(long_string[0:4]) #start from element 0 and continue 4 element
print(long_string[-5:]) #start from element -5 and continue until the end1
print(long_string[:-5]) #it will show everything except the last 5 charected
print(long_string[-9:-1]) #it will start at index -9 and until index -1
print(long_string[5:]) #show index 5 until the end
print(long_string[::2] # it will only show indexes in even number , 0,2,4,6,8
print(long_string[::-1]) #it will reverse the whole text

print(long_string[:4] + " extra text")
print(long_string.capitalize()) #capitilizaed the first charecter
print(long_string.lower()) #lower case all charecter
print(long_string.upper()) #upper case all charecter
print(long_string.find("floor")) #if can find floor then it bring back the index number
print(long_string.index("i")) #it show where is the location of i in index
print(long_string.count("i")) # it will count how many i is repeated in string
print(len(long_string)) # return the number of charecter
print(long_string.replace("Floor", "Ground")) #replace all floor with ground
print(long_string.replace(" ", ""))  # remove all space and replace with nothing
print(long_string.endswith("e")) #if the letter ends with "e" it will show true or false
print(long_string.startswith("e")) #if the letter start with "e" it will show true or false
print(long_string.strip()) #remove all spaces before and after the text only, not between the text
print(long_string.strip("$"))  # remove all $ before and after the text
print("_".join(long_string)) #it will add _ after every charecter = i_ _w_i_l_l_ _c_a_t_c_h_ _y_o_u_ _i_f_ _y_o_u_ _f_a_l_l_ _-_ _t_h_e_ _f_l_o_o_r

quote_list = long_string.split(" ") #it will take space out and convert it to list
quote_list = long_string.split(",") #it will take , out and convert it to list
