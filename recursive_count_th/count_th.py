'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# word inputted can be of any length, including only 1 letter. If it is 1 letter, return 0
# if it is 2 letters, check to see if it is equal to th


def count_th(word, th=0):
    if len(word) <= 1:
        return th
    if word[0:2] == "th":
        th+=1
        return count_th(word[1:], th)
    else:
        return count_th(word[1:], th)