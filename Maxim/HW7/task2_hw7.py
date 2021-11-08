# Task 2
# There are two character strings of lowercase and uppercase Latin
# letters and numbers. Develop a program that builds and prints in
# alphabetical order the set of letters that are in both arrays and the
# set of letters of the first and second arrays separately.

str1 = "slfSA2UJnms4vASDFDS1cxzcDSxcl"
str2 = "mvslfXGV98SDF23SDFmvnboa45250"

setStr1, setStr2 = set(str1), set(str2)
setIntersected = setStr1.intersection(setStr2)

# print("{}\n{}".format(str1, str2))
print("{}".format(sorted(setIntersected)))
print("{}\n{}".format(sorted(setStr1), sorted(setStr2)))
