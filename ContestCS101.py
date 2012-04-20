

# This work is licensed under a Creative Commons CC BY-NC-SA License



def tone_distance(original, check):                         # To find tone distance between notes
    former = 0                                              # Both input are single letter string
    latter = 0

    if original < check:
        if original == 'A':
            former = 1
        if original == 'Ab':
            former = 0.5
        if original == 'A#':
            former = 1.5
        if original == 'B':
            former = 2
        if original == 'Bb':
            former = 1.5
        if original == 'B#':
            former = 2.5
        if original == 'C':
            former = 3
        if original == 'Cb':
            former = 2.5
        if original == 'C#':
            former = 3.5
        if original == 'D':
            former = 4
        if original == 'Db':
            former = 3.5
        if original == 'D#':
            former = 4.5
        if original == 'E':
            former = 5
        if original == 'Eb':
            former = 4.5
        if original == 'E#':
            former = 5.5
        if original == 'F':
            former = 6
        if original == 'Fb':
            former = 5.5
        if original == 'F#':
            former = 6.5
        if original == 'G':
            former = 7
        if original == 'Gb':
            former = 6.5
        if original == 'G#':
            former = 7.5

        if check == 'A':
            latter = 1
        if check == 'Ab':
            latter = 0.5
        if check == 'A#':
            latter = 1.5
        if check == 'B':
            latter = 2
        if check == 'Bb':
            latter = 1.5
        if check == 'B#':
            latter = 2.5
        if check == 'C':
            latter = 3
        if check == 'Cb':
            latter = 2.5
        if check == 'C#':
            latter = 3.5
        if check == 'D':
            latter = 4
        if check == 'Db':
            latter = 3.5
        if check == 'D#':
            latter = 4.5
        if check == 'E':
            latter = 5
        if check == 'Eb':
            latter = 4.5
        if check == 'E#':
            latter = 5.5
        if check == 'F':
            latter = 6
        if check == 'Fb':
            latter = 5.5
        if check == 'F#':
            latter = 6.5
        if check == 'G':
            latter = 7
        if check == 'Gb':
            latter = 6.5
        if check == 'G#':
            latter = 7.5

        distance = abs(latter - former)

    elif original > check:
        if original == 'A':
            former = 7
        if original == 'Ab':
            former = 6.5
        if original == 'A#':
            former = 7.5
        if original == 'B':
            former = 6
        if original == 'Bb':
            former = 5.5
        if original == 'B#':
            former = 6.5
        if original == 'C':
            former = 5
        if original == 'Cb':
            former = 4.5
        if original == 'C#':
            former = 5.5
        if original == 'D':
            former = 4
        if original == 'Db':
            former = 3.5
        if original == 'D#':
            former = 4.5
        if original == 'E':
            former = 3
        if original == 'Eb':
            former = 2.5
        if original == 'E#':
            former = 3.5
        if original == 'F':
            former = 2
        if original == 'Fb':
            former = 1.5
        if original == 'F#':
            former = 2.5
        if original == 'G':
            former = 1
        if original == 'Gb':
            former = 0.5
        if original == 'G#':
            former = 1.5

        if check == 'A':
            latter = 7
        if check == 'Ab':
            latter = 6.5
        if check == 'A#':
            latter = 7.5
        if check == 'B':
            latter = 6
        if check == 'Bb':
            latter = 5.5
        if check == 'B#':
            latter = 6.5
        if check == 'C':
            latter = 5
        if check == 'Cb':
            latter = 4.5
        if check == 'C#':
            latter = 5.5
        if check == 'D':
            latter = 4
        if check == 'Db':
            latter = 3.5
        if check == 'D#':
            latter = 4.5
        if check == 'E':
            latter = 3
        if check == 'Eb':
            latter = 2.5
        if check == 'E#':
            latter = 3.5
        if check == 'F':
            latter = 2
        if check == 'Fb':
            latter = 1.5
        if check == 'F#':
            latter = 2.5
        if check == 'G':
            latter = 1
        if check == 'Gb':
            latter = 0.5
        if check == 'G#':
            latter = 1.5

        distance = abs(latter - former)

    elif former == latter:
        distance = 0


    return distance

def disparity_check(original, check):                               # Checks if value of both inputs are the same
    i = 0                                                           # Both inputs are in lists
    j = 0                                                           # Returns boolean
    i2 = 0
    result = False

    while i < len(original):
        while j < len(check):

            if original[i] == check[j]:
                i2 = i + 1
                j = j + 1
                result= True

                if i2 >= len(original):
                    result = False

                    return result

                while result == True:

                    if j < len(check):
                        if i2 < len(original):
                            if original[i2] == check[j]:

                                i2 = i2 + 1
                                j = j + 1

                                result= True

                            else:
                                result = False

                    if j == len(check):
                        return result
            else:
                break

        j = 0
        i2 = 0
        i = i + 1

    return  result


def split_string_into_list(stuff):                              # Makes string input into list
    string = []                                                 # Returns a list
    i = 0

    while i < len(stuff):
        if (i + 1) < len(stuff):
            if stuff[i+1] == 'b':
                add = stuff[i] + stuff[i+1]
                string.append(add)
                i = i + 2

            elif stuff[i+1] == '#':
                add = stuff[i] + stuff[i+1]
                string.append(add)
                i = i + 2

            else:
                string.append(stuff[i])
                i = i + 1

        else:
            string.append(stuff[i])
            i = i + 1

    return string



def note_distance_list(notes):                                      # Find distance between notes
    i = 0                                                           # Takes string input
    list = []                                                       # Output numbers in list

    while i < (len(notes) - 1):
        distance = tone_distance(notes[i], notes[i+1])
        list.append(distance)

        i = i + 1

    return list

def add_to_index(index, title, notes):                              # Add title, notes and distance to index as a set
    string = split_string_into_list(notes)
    distance = note_distance_list(notes)

    stuffs = [title, notes, string, distance]
    index.append(stuffs)

def convert_search_format(search):                                  # Convert search string into note list and distance list

    notes = split_string_into_list(search)
    distance = note_distance_list(search)

    set = [notes, distance]

    return set

def edit_distance(s,t):
    if len(s) == 0:
        return len(t)
    if len(t) == 0:
        return len(s)
    if s[0] == t[0]:
        return edit_distance(s[1:], t[1:])
    else:
        return min(1 + edit_distance(s[1:], t[1:]), 1 + edit_distance(s, t[1:]), 1 + edit_distance(s[1:], t))

def sort(index):                                                    # To sort index based on rank
                                                                    # Arrange from smallest to largest rank
    smaller = []
    greater = []

    if len(index) <= 1:
        return index

    for i in index[1:]:

        if i[1] < index[0][1]:
            smaller.append(i)

        else:
            greater.append(i)

    return sort(smaller) + [index[0]] + sort(greater)

def ranked_search(index):                                               # Sorts the result by rank value
    result = []
    sorted = sort(index)

    for title in sorted:
#        result.append(title[0])                                ##### Activating this line will show only titles ####
        result.append(title)                                    ##### Activating this line will show titles and ranks ####

    return result

def find_music(index, input):
    i = 0
    title = []

    search = convert_search_format(input)

    while i < len(index):
        original = index[i]

        letter_check = disparity_check(original[2], search[0])
        distance_check = disparity_check(original[3], search[1])

        if letter_check == True:                                        # Music here have exact note matches
            add = [original[0], -2]                                     # So set rank value to lowest, -2
            title.append(add)

        elif distance_check == True:                                    # Music here have exact distance matches
            add = [original[0], -1]                                     # So set rank value to 2nd lowest, -2
            title.append(add)

        else:                                                           # Music here have variable note and distance matches
            edit_letter = edit_distance(original[1], input)             # So have the rank value adhere to comparative edit distance
            edit_dist = edit_distance(original[2], search[1])

            edit_letter = abs(len(original[1]) - len(search[0]) - edit_letter) + 1
            edit_dist = abs(len(original[2]) - len(search[1]) - edit_dist) + 1

            if edit_letter < edit_dist:

                edit_add = [original[0], edit_letter]
                title.append(edit_add)

            else:
                edit_add = [original[0], edit_dist]
                title.append(edit_add)

        i = i + 1

    result = ranked_search(title)                                   # Sorts the result by rank value

    return result


#################################################################################################

# Main code implementation

#####
# Adding music title and notes to index(database)
index = []
add_to_index(index,'Twinkle_Twinkle_Little_star','CCGGAAGFFEEDDCGGFFEEDGGFFEEDCCGGAAGFFEEDDC')

add_to_index(index, 'Mary_Had_a_Little_Lamb', 'EDCDEEEDDDEGGEDCDEEEEDDEDC')

add_to_index(index, 'Scarborough_Fair', 'DDAAAEFEDACDCABGADDCAAGFECDAGFEDCD')

add_to_index(index, 'Green_Sleeves','EGABCBAF#DEF#GEED#EF#D#BEGABCBAF#DEF#GF#ED#C#D#EEDDC#BAF#DEF#GEED#EF#D#BDDC#BAF#DEF#GF#ED#C#D#EE')

add_to_index(index, 'Star_Wars_Imperial_March_Simplified','EEECGECGEBBBCGEbCGE')

########
### Finding matches by inputting the search string as the second argument ###


# Exact Note Check #
print find_music(index, 'CCGG')
# ==> [['Twinkle_Twinkle_Little_star', -2], ['Scarborough_Fair', -1], ['Green_Sleeves', 1], ['Star_Wars_Imperial_March_Simplified', 1], ['Mary_Had_a_Little_Lamb', 2]]
## 'Twinkle_Twinkle_Little_star' is the only exact note match (value: -2)


# Exact Note-Distance Check #
print find_music(index, 'CEbG')
# ==> [['Green_Sleeves', -1], ['Twinkle_Twinkle_Little_star', 1], ['Mary_Had_a_Little_Lamb', 1], ['Scarborough_Fair', 1], ['Star_Wars_Imperial_March_Simplified', 2]]
## 'Green_Sleeves' is the only exact note-distance match (value: -1)


# Exact Note and Note-Distance Check #
print find_music(index, 'CBA')
# ==> [['Green_Sleeves', -2], ['Twinkle_Twinkle_Little_star', -1], ['Mary_Had_a_Little_Lamb', -1], ['Scarborough_Fair', -1], ['Star_Wars_Imperial_March_Simplified', -1]]
## Exact note match: 'Green_Sleeves' (value: -2)
## Exact note-distance match: 'Twinkle_Twinkle_Little_star', 'Mary_Had_a_Little_Lamb', 'Scarborough_Fair', 'Star_Wars_Imperial_March_Simplified' (value: -1)


# Neither Note nor Note-Distance Matches #
print find_music(index, 'DFA#')
# ==> [['Twinkle_Twinkle_Little_star', 1], ['Scarborough_Fair', 1], ['Green_Sleeves', 2], ['Mary_Had_a_Little_Lamb', 3], ['Star_Wars_Imperial_March_Simplified', 4]]
## No titles have value of exact matches, ie. -1 or -2

