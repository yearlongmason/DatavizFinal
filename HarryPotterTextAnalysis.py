import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from pandasql import sqldf
import streamlit as st
from PIL import Image
import base64


#Data cleaning

#Harry Potter and the Sorcerer's Stone (hp1) data cleaning
hp1 = pd.read_csv('HarryPotter1.csv', sep=';')

#Normalizing text (all lowercase, no special characters)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',\
         '0','1','2','3','4','5','6','7','8','9', '-'] #Defines all characters I want to keep
hp1['normText']=[x.lower() for x in hp1['Sentence']] #Sets normalized text to the lowercase Sentence
for i in range(len(hp1)): #Gets rid of all special characters
    hp1.at[i, 'normText'] = ''.join([str(x.lower()) if x in alphabet else '' for x in hp1.iloc[i]['normText']])

#fixes some mistakes in name formatting
hp1['Character'] = [x.replace(' ', '') for x in hp1['Character']] #Remove spaces from Character names
hp1['Character'] = ['Barkeep' if x=='Barkeep\xa0Tom' else x for x in hp1['Character']]
hp1['Character'] = ['Train Master' if x=='Trainmaster' else x for x in hp1['Character']]
hp1['Character'] = ['Sorting Hat' if x=='SortingHat' else x for x in hp1['Character']]
hp1['Character'] = ['Sir Nicholas' if x=='SirNicholas' else x for x in hp1['Character']]
hp1['Character'] = ['Man in Painting' if x=='Maninpaint' else x for x in hp1['Character']]
hp1['Character'] = ['Fat Lady' if x=='FatLady' else x for x in hp1['Character']]
hp1['Character'] = ['Madam Hooch' if x=='MadamHooch' else x for x in hp1['Character']]
hp1['Character'] = ['Ron and Harry' if x=='RonandHarry' else x for x in hp1['Character']]
hp1['Character'] = ['Oliver Wood' if x=='OIiver' else x for x in hp1['Character']]
hp1['Character'] = ['Oliver Wood' if x=='Oliver' else x for x in hp1['Character']]
hp1['Character'] = ['Harry, Ron, and Hermione' if x=='All3' else x for x in hp1['Character']]
hp1['Character'] = ['Hermione' if x=='Hermoine' else x for x in hp1['Character']]
hp1['Character'] = ['Draco' if x=='Malfoy' else x for x in hp1['Character']]
hp1['Character'] = ['Students' if x=='Class' else x for x in hp1['Character']]
hp1['Character'] = ['Trolley Witch' if x=='Woman' else x for x in hp1['Character']]
hp1.at[729, 'Character'] = 'Harry, Ron, and Hermione' #Very specific case that I researched
hp1.at[928, 'Character'] = 'Crowd' #Very specific case that I researched
hp1.at[463, 'Character'] = 'Neville'
#People I would classify as a general "Other" category
backgroundCharacters=['Someone', 'Man', 'Witch', 'Boy', 'Girl', 'Crowd', 'Gryffindors', 'Goblin']
hp1['Character'] = ['Background Character' if x in backgroundCharacters else x for x in hp1['Character']]

#Creating column for number of words per sentence
hp1['numWords'] = [len(x.split(' ')) for x in hp1['Sentence']]

#Defining houses
Gryffindor=['Dumbledore', 'McGonagall', 'Hagrid', 'Harry', 'Mrs.Weasley', 'George', 'Fred', 'Ginny', 'Ron',\
           'Hermione', 'Neville', 'Seamus', 'Percy', 'Sir Nicholas', 'Fat Lady', 'Dean', 'Harry, Ron, and Hermione',\
           'Oliver Wood', 'Ron and Harry', 'LeeJordan']
Slytherin=['Draco', 'Snape', 'Flint', 'Voldemort']
Ravenclaw=['Quirrell', 'Ollivander', 'Madam Hooch', 'Flitwick']
Hufflepuff=[]
Other=['Petunia', 'Dudley', 'Vernon', 'Snake', 'Background Character', 'Barkeep', 'Griphook', 'Train Master',\
      'Trolley Witch', 'Sorting Hat', 'Man in Painting', 'Students', 'Filch', 'Firenze']

#Making a list of all housing assignments per line
hp1House=[]
for i in hp1['Character']:
    if i in Gryffindor:
        hp1House.append('Gryffindor')
    elif i in Slytherin:
        hp1House.append('Slytherin')
    elif i in Ravenclaw:
        hp1House.append('Ravenclaw')
    elif i in Hufflepuff:
        hp1House.append('Hufflepuff')
    else:
        hp1House.append('Muggle')
hp1['House'] = hp1House

#Creates movie name and movie number column for when all dataframes are combined
hp1['MovieName'] = 'Harry Potter and the Sorcerer\'s Stone'
hp1['MovieNumber'] = 1


#Harry Potter and the Chamber of Secrets (hp2) data cleaning
hp2 = pd.read_csv('HarryPotter2.csv', sep=';')

#Normalizing text (all lowercase, no special characters)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',\
         '0','1','2','3','4','5','6','7','8','9', '-'] #Defines all characters I want to keep
hp2['normText']=[x.lower() for x in hp2['Sentence']] #Sets normalized text to the lowercase Sentence
for i in range(len(hp2)): #Gets rid of all special characters
    hp2.at[i, 'normText'] = ''.join([str(x.lower()) if x in alphabet else '' for x in hp2.iloc[i]['normText']])

#Fixing any name irregularities as well as categorizing background characters
hp2['Character'] = [x.title().replace(' ', '') for x in hp2['Character']] #Remove spaces from Character names
hp2['Character'] = ['Vernon' if x=='UncleVernon' else x for x in hp2['Character']]
hp2['Character'] = ['Petunia' if x=='AuntPetunia' else x for x in hp2['Character']]
hp2['Character'] = ['Petunia & Dudley' if x=='Aunt\xa0Petunia\xa0&Dudley' else x for x in hp2['Character']]
hp2['Character'] = ['Lucius' if x=='LuciusMalfoy' else x for x in hp2['Character']]
hp2['Character'] = ['Ron and Harry' if x=='HarryAndRon' else x for x in hp2['Character']]
hp2['Character'] = ['Professor Sprout' if x=='ProfessorSprout' else x for x in hp2['Character']]
hp2['Character'] = ['Penelope Clearwater' if x=='PenelopeClearwater' else x for x in hp2['Character']]
hp2['Character'] = ['Sir Nicholas' if x=='SirNicholas' else x for x in hp2['Character']]
hp2['Character'] = ['Lockhart' if x=='GilderoyLockhart' else x for x in hp2['Character']]
hp2['Character'] = ['Cornish Pixies' if x=='CornishPixies' else x for x in hp2['Character']]
hp2['Character'] = ['Oliver Wood' if x=='Wood' else x for x in hp2['Character']]
hp2['Character'] = ['Madam Pomfrey' if x=='MadamPomfrey' else x for x in hp2['Character']]
hp2['Character'] = ['Moaning Myrtle' if x=='MoaningMyrtle' else x for x in hp2['Character']]
hp2['Character'] = ['Justin Finch-Fletchley' if x=='JustinFinch-Fletchley' else x for x in hp2['Character']]
hp2['Character'] = ['Sorting Hat' if x=='SortingHat' else x for x in hp2['Character']]
hp2['Character'] = ['Tom Riddle' if x=='TomRiddle' else x for x in hp2['Character']]
hp2['Character'] = ['McGonagall' if x=='Mcgonagall' else x for x in hp2['Character']]
hp2['Character'] = ['Harry, Ron, and Hermione' if x=='Harry-Ron-Hermione' else x for x in hp2['Character']]
#People I would classify as a general "Other" category
backgroundCharacters = ['Witch', 'Man', 'Photographer', 'Trainmaster', 'Class', 'Voice', 'Boy', 'Picture',\
                       'Slytherins', 'Diary', 'Student']
hp2['Character'] = ['Background Character' if x in backgroundCharacters else x for x in hp2['Character']]

#Creating column for number of words per sentence
hp2['numWords'] = [len(x.split(' ')) for x in hp2['Sentence']]

#Defining houses
Gryffindor=['Dumbledore', 'McGonagall', 'Hagrid', 'Harry', 'Mrs.Weasley', 'George', 'Fred', 'Ginny', 'Ron',\
           'Hermione', 'Neville', 'Seamus', 'Percy', 'Sir Nicholas', 'Fat Lady', 'Dean', 'Harry, Ron, and Hermione',\
           'Oliver', 'Ron and Harry', 'LeeJordan', 'Mr.Weasley', 'Fred,George,Ron', 'Fred,George,Ron,Harry', 'Colin',\
           'Oliver Wood']
Slytherin=['Draco', 'Snape', 'Flint', 'Voldemort', 'Mr.Borgin', 'Lucius', 'Crabbe', 'Tom Riddle', 'Fudge']
Ravenclaw=['Quirrell', 'Ollivander', 'Madam Hooch', 'Flitwick', 'Lockhart', 'Penelope Clearwater', 'Moaning Myrtle']
Hufflepuff=['Professor Sprout', 'Madam Pomfrey', 'Justin Finch-Fletchley']
Other=['Petunia', 'Dudley', 'Vernon', 'Snake', 'Background Character', 'Barkeep', 'Griphook', 'Train Master',\
      'Trolley Witch', 'Sorting Hat', 'Man in Painting', 'Students', 'Filch', 'Firenze', 'Dobby', 'Petunia & Dudley',\
      'Cornish Pixies', 'Aragog']

#Making a list of all housing assignments per line
house=[]
for i in hp2['Character']:
    if i in Gryffindor:
        house.append('Gryffindor')
    elif i in Slytherin:
        house.append('Slytherin')
    elif i in Ravenclaw:
        house.append('Ravenclaw')
    elif i in Hufflepuff:
        house.append('Hufflepuff')
    else:
        house.append('Muggle')
hp2['House'] = house

#Creates movie name and movie number column for when all dataframes are combined
hp2['MovieName'] = 'Harry Potter and the Chamber of Secrets'
hp2['MovieNumber'] = 2


#Harry Potter and the Prisoner of Azkaban (hp3) data cleaning
hp3 = pd.read_csv('HarryPotter3.csv', sep=';')

#Renaming columns to be consistent with the other 2 dataframes
hp3.rename(columns = {'CHARACTER':'Character', 'SENTENCE':'Sentence'}, inplace=True)

#Normalizing text (all lowercase, no special characters)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',\
         '0','1','2','3','4','5','6','7','8','9', '-'] #Defines all characters I want to keep
hp3['normText']=[x.lower() for x in hp3['Sentence']] #Sets normalized text to the lowercase Sentence
for i in range(len(hp3)): #Gets rid of all special characters
    hp3.at[i, 'normText'] = ''.join([str(x.lower()) if x in alphabet else '' for x in hp3.iloc[i]['normText']])

#Fixing any name irregularities as well as categorizing background characters
hp3['Character'] = [x.title() for x in hp3['Character']]
hp3['Character'] = ['Petunia' if x == 'Aunt Petunia' else x for x in hp3['Character']]
hp3['Character'] = ['Vernon' if x == 'Uncle Vernon' else x for x in hp3['Character']]
hp3['Character'] = ['Stan Shunpike' if x == '\nStan Shunpike' else x for x in hp3['Character']]
hp3['Character'] = ['Mrs.Weasley' if x == 'Mrs. Weasley' else x for x in hp3['Character']]
hp3['Character'] = ['Mr.Weasley' if x == 'Mr. Weasley' else x for x in hp3['Character']]
hp3['Character'] = ['McGonagall' if x == 'Mcgonagall' else x for x in hp3['Character']]
hp3['Character'] = ['Fred and George' if x == 'Fred & George' else x for x in hp3['Character']]
hp3['Character'] = ['Peter Pettigrew' if x == 'Pettigrew' else x for x in hp3['Character']]
#People I would classify as a general "Other" category
backgroundCharacters = ['Tom', 'Vendor', 'Housekeeper', 'Boy', 'Class', 'Teacher', 'Crowd', 'Man', 'Witch',\
                       'Shrunken Head 1', 'Shrunken Head 2', 'Voice', 'Boy 1', 'Boy 2']
hp3['Character'] = ['Background Character' if x in backgroundCharacters else x for x in hp3['Character']]

#Creating column for number of words per sentence
hp3['numWords'] = [len(x.split(' ')) for x in hp3['Sentence']]

#Defining houses
Gryffindor=['Dumbledore', 'McGonagall', 'Hagrid', 'Harry', 'Mrs.Weasley', 'George', 'Fred', 'Ginny', 'Ron',\
           'Hermione', 'Neville', 'Seamus', 'Percy', 'Sir Nicholas', 'Fat Lady', 'Dean', 'Harry, Ron, and Hermione',\
           'Oliver', 'Ron and Harry', 'LeeJordan', 'Mr.Weasley', 'Fred,George,Ron', 'Fred,George,Ron,Harry', 'Colin',\
           'Oliver Wood', 'Lupin', 'Bem', 'Parvati', 'Fred and George', 'Peter Pettigrew', 'Sirius']

Slytherin=['Draco', 'Snape', 'Flint', 'Voldemort', 'Mr.Borgin', 'Lucius Malfoy', 'Crabbe', 'Tom Riddle', 'Fudge',\
          'Stan Shunpike', 'Pansy Parkinson', 'Goyle']

Ravenclaw=['Quirrell', 'Ollivander', 'Madam Hooch', 'Flitwick', 'Lockhart', 'Penelope Clearwater', 'Moaning Myrtle',\
          'Trelawney']

Hufflepuff=['Professor Sprout', 'Madam Pomfrey', 'Justin Finch-Fletchley']

Other=['Petunia', 'Dudley', 'Vernon', 'Snake', 'Background Character', 'Barkeep', 'Griphook', 'Train Master',\
      'Trolley Witch', 'Sorting Hat', 'Man in Painting', 'Students', 'Filch', 'Firenze', 'Dobby', 'Petunia & Dudley',\
      'Cornish Pixies', 'Aragog', 'Aunt Marge', 'Shrunken Head', 'Madam Rosmerta']

#Making a list of all housing assignments per line
house=[]
for i in hp3['Character']:
    if i in Gryffindor:
        house.append('Gryffindor')
    elif i in Slytherin:
        house.append('Slytherin')
    elif i in Ravenclaw:
        house.append('Ravenclaw')
    elif i in Hufflepuff:
        house.append('Hufflepuff')
    else:
        house.append('Muggle')
hp3['House'] = house

#Creates movie name and movie number column for when all dataframes are combined
hp3['MovieName'] = 'Harry Potter and the Prisoner of Azkaban'
hp3['MovieNumber'] = 3


#Creating dataframe for all three movies combined (hp123)
query = """
SELECT * FROM hp1
UNION ALL
SELECT * FROM hp2
UNION ALL
SELECT * FROM hp3
ORDER BY MovieNumber;
""" #Using SQL commands to get the union of all three movies
hp123 = sqldf(query, globals())
#hp123 = pd.concat([hp1, hp2, hp3]) #This is pretty much the pandas equivalent of the above statement



#Dataviz functions
def linesPerHouse(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return an altair chart that shows the total number of lines in each house from that data"""
    
    houseLines = data.groupby('House', as_index=False).count() #Groups data by house
    houseLines['Number of Lines'] = houseLines['Sentence'] #Saved for the tooltip later

    #Logging data in order to normalize it, otherwise it's very skewed
    houseLines['Sentence'] = [np.around(np.log10(x),2) for x in houseLines['Sentence']]

    #Keeps Hufflepuff in the chart even if they have no lines
    if 'Hufflepuff' not in houseLines['House']:
        #Adds the housename + rest of the colunms as 0 (weird numpy workaround due to varying dataframe sizes)
        houseLines.loc[len(houseLines.index)] = ['Hufflepuff'] + list(np.zeros(len(data.columns)))
        
    #Define color parameters based on whether or not Hufflepuff has any lines
    if 'Hufflepuff' in list(data['House']):
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'Muggle']
        colors = ['#be0119', '#009500', '#069af3', '#feb308', '#5f6b73']
    else:
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Muggle', 'Hufflepuff']
        colors = ['#be0119', '#009500', '#069af3', '#5f6b73', '#feb308']
    
    #setting axis labels [weird javascript thing >:(]
    axisLabels = "datum.label == 1 ? '10 lines' : datum.label == 2 ? '100 lines' : '1000 lines'"
    labelVals = [1,2,3]
    
    #Create chart
    chart = alt.Chart(houseLines, title = 'Number of Lines per House').mark_bar().encode(
        alt.X('House', sort=houses,\
             axis=alt.Axis(labelAngle=0, titleColor = 'black')),
        alt.Y('Sentence', title='Number of Lines (log10 scale)',\
              scale=alt.Scale(domain=[0, houseLines['Sentence'].max()+houseLines['Sentence'].max()*.007]),\
              axis=alt.Axis(labelExpr=axisLabels, values=labelVals, titleColor = 'black')),
        color = alt.Color('House', scale=alt.Scale(domain = houses, range=colors)),
        tooltip=['House', 'Number of Lines']
    )
    chart = chart.properties(width=width, height=height) #Set figure size w685 h475
    chart = chart.configure_axis(labelFontSize=15, titleFontSize=18) #Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20) #Sets title size
    chart = chart.configure_legend(titleColor='black', titleFontSize=17, labelFontSize=15) #Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2) #Sets a border around the chart
    
    return chart


def linesPerCharacter(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return an altair chart that shows the top 11 most speaking characters colored by their house"""

    #Defining houses
    Gryffindor=['Dumbledore', 'McGonagall', 'Hagrid', 'Harry', 'Mrs.Weasley', 'George', 'Fred', 'Ginny', 'Ron',\
               'Hermione', 'Neville', 'Seamus', 'Percy', 'Sir Nicholas', 'Fat Lady', 'Dean', 'Harry, Ron, and Hermione',\
               'Oliver', 'Ron and Harry', 'LeeJordan', 'Mr.Weasley', 'Fred,George,Ron', 'Fred,George,Ron,Harry', 'Colin',\
               'Oliver Wood', 'Lupin', 'Bem', 'Parvati', 'Fred and George', 'Peter Pettigrew', 'Sirius']
    Slytherin=['Draco', 'Snape', 'Flint', 'Voldemort', 'Mr.Borgin', 'Lucius', 'Crabbe', 'Tom Riddle', 'Fudge',\
              'Stan Shunpike', 'Pansy Parkinson', 'Goyle']
    Ravenclaw=['Quirrell', 'Ollivander', 'Madam Hooch', 'Flitwick', 'Lockhart', 'Penelope Clearwater', 'Moaning Myrtle',\
              'Trelawney']
    Hufflepuff=['Professor Sprout', 'Madam Pomfrey', 'Justin Finch-Fletchley']
    Other=['Petunia', 'Dudley', 'Vernon', 'Snake', 'Background Character', 'Barkeep', 'Griphook', 'Train Master',\
          'Trolley Witch', 'Sorting Hat', 'Man in Painting', 'Students', 'Filch', 'Firenze', 'Dobby', 'Petunia & Dudley',\
          'Cornish Pixies', 'Aragog', 'Aunt Marge', 'Shrunken Head', 'Madam Rosmerta']

    #Getting new data that's grouped by the character
    spokenLines=data.drop(['normText', 'House', 'MovieName', 'MovieNumber', 'numWords'], axis=1) #Drops unnecessary cols
    spokenLines = spokenLines.groupby('Character', as_index=False).count() #Groups by Character and counts the lines
    spokenLines.sort_values('Sentence', ascending=False, inplace=True) #Sorts values
    spokenLines = spokenLines[spokenLines['Character'] != 'Background Character'] #Removing background character becasue it doesn't make much sense in this visualization

    #Getting the house for each character
    house=[]
    for i in spokenLines['Character']:
        if i in Gryffindor:
            house.append('Gryffindor')
        elif i in Slytherin:
            house.append('Slytherin')
        elif i in Ravenclaw:
            house.append('Ravenclaw')
        elif i in Hufflepuff:
            house.append('Hufflepuff')
        else:
            house.append('Muggle')

    #Adding columns that couldn't be aggregated in groupby
    spokenLines['House'] = house
    
    #Defining these for setting color
    houseColors = {'Gryffindor':'#be0119', 'Slytherin':'#009500', 'Ravenclaw':'#069af3', 'Muggle':'#5f6b73'}

    #Creating the chart
    chart = alt.Chart(spokenLines.head(11), title = 'Number of Lines per Character').mark_bar().encode(
        alt.X('Character', sort=alt.EncodingSortField(field="Character", op="count", order='ascending'),\
              axis=alt.Axis(labelAngle=0, titleColor='black')), #Character sorted by number of lines
        alt.Y('Sentence', title='Number of Lines', axis=alt.Axis(titleColor='black')), #Number of lines
        color = alt.Color('House', scale=alt.Scale(domain=list(houseColors.keys()), range=list(houseColors.values()))),
        tooltip = ['Character', 'House', alt.Tooltip('Sentence', title='Number of Lines')] #Adds tooltip
    )
    chart = chart.properties(width=width, height=height) #Set figure size w690 h518
    chart = chart.configure_axis(labelFontSize=15, titleFontSize=18) #Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20) #Sets title size
    chart = chart.configure_legend(titleColor='black', titleFontSize=17, labelFontSize=15) #Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2) #Sets a border around the chart 
    
    return chart


def numWordsVP(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return a matplotlib figure that has seaborn violin plots on it representing the number of words per line by house"""
    
    #Creating the figure
    fig, ax = plt.subplots(figsize=(width, height))
    fig.set_facecolor('White')
    
    #setting colors according to whether or not Hufflepuff has any lines 
    houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Muggle']
    colors = ['#be0119', '#009500', '#069af3', '#5f6b73']
    if 'Hufflepuff' in list(data['House']):
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'Muggle']
        colors = ['#be0119', '#009500', '#069af3', '#feb308', '#5f6b73']
        
    #Creating the actual plot
    sns.violinplot(data=data, x='House', y='numWords', linewidth=1.5, palette=colors, order = houses)
    
    #ax.title not being used in streamlit implimentation becasue the title gets a little weird, so I manually add it in
    #ax.set_title('Number of Words Spoken Per Line by House', fontsize=18, fontweight='bold', loc='left', color='xkcd:grey')
    
    ax.set_ylabel('Number of Words per Line', fontsize=9)
    ax.set_xlabel('House', fontsize=9)
    ax.set_ylim([-4, 40])
    x=[t.set_color('xkcd:grey') for t in ax.xaxis.get_ticklabels()]
    x=[t.set_color('xkcd:grey') for t in ax.yaxis.get_ticklabels()]
    del x

    ax.tick_params(axis='y', width=1, length=5, labelsize=7, color='xkcd:grey')
    ax.tick_params(axis='x', width=1, length=5, labelsize=7, color='xkcd:grey')
    
    ax.spines['bottom'].set_color('xkcd:gray')
    ax.spines['top'].set_color('xkcd:white')
    ax.spines['left'].set_color('xkcd:gray')
    ax.spines['right'].set_color('xkcd:white')

    return fig


def numWordsPerLineJP(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return an altair chart that is a jitter plot that represents the number of words per sentence by house"""
    
    #Setting house colors
    houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'Muggle']
    colors = ['#be0119', '#009500', '#069af3', '#feb308', '#5f6b73']
    
    #Getting x-axis values (jittered within .35)
    houseInt = []
    for i in data['House']:
        if i == 'Gryffindor':
            if np.random.randint(-1,1):
                houseInt.append(1+np.random.normal()%.35)
            else:
                houseInt.append(1-np.random.normal()%.35)
        elif i == 'Slytherin':
            if np.random.randint(-1,1):
                houseInt.append(2+np.random.normal()%.35)
            else:
                houseInt.append(2-np.random.normal()%.35)
        elif i == 'Ravenclaw':
            if np.random.randint(-1,1):
                houseInt.append(3+np.random.normal()%.35)
            else:
                houseInt.append(3-np.random.normal()%.35)
        elif i == 'Hufflepuff':
            if np.random.randint(-1,1):
                houseInt.append(4+np.random.normal()%.35)
            else:
                houseInt.append(4-np.random.normal()%.35)
        else: #If muggle
            if 'Hufflepuff' in list(data['House']):
                if np.random.randint(-1,1):
                    houseInt.append(5+np.random.normal()%.35)
                else:
                    houseInt.append(5-np.random.normal()%.35)
            else:
                if np.random.randint(-1,1):
                    houseInt.append(4+np.random.normal()%.35)
                else:
                    houseInt.append(4-np.random.normal()%.35)
    data['houseInt'] = houseInt
    
    #Setting axis labels [weird javascript thing >:(] Based on whether or not Hufflepuff has any lines
    if 'Hufflepuff' in list(data['House']):
        axisLabels = "datum.label == 5 ? 'Muggle' : datum.label == 4 ? 'Hufflepuff' : datum.label == 3 ? 'Ravenclaw' : datum.label == 2 ? 'Slytherin' : 'Gryffindor'"
        axisVals = [1,2,3,4,5]
    else:
        axisLabels = "datum.label == 4 ? 'Muggle' : datum.label == 3 ? 'Ravenclaw' : datum.label == 2 ? 'Slytherin' : 'Gryffindor'"
        axisVals = [1,2,3,4]
        
    chart = alt.Chart(data, title='Number of Words Per Line by House').mark_circle(size=50).encode(
        alt.Y("numWords:Q", title = 'Number of Words Per Line', axis = alt.Axis(titleColor='black')),
        alt.X("houseInt:Q", axis=alt.Axis(labelExpr=axisLabels, values=axisVals, titleColor='black'), title='House',
              scale=alt.Scale(domain=[data['houseInt'].min()-.1, data['houseInt'].max()+.1])),
        color = alt.Color('House', scale=alt.Scale(domain = houses, range=colors)),
        tooltip = ['Character', 'House', alt.Tooltip('MovieName', title='Movie'),\
                   alt.Tooltip('Sentence', title='Line'), alt.Tooltip('numWords', title='Number of words')]
    )
    chart = chart.properties(width=width, height=height) #Set figure size w750 h600
    chart = chart.configure_axis(labelFontSize=15, titleFontSize=18) #Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20) #Sets title size
    chart = chart.configure_legend(titleColor='black', titleFontSize=17, labelFontSize=15) #Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2) #Sets a border around the chart
    chart = chart.interactive()

    return chart


def numWordsPerLineHM(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return an altair chart that shows a heatmap that takes a random sample of 25 lines per house and colors them by number of words per sentence"""
    
    #Gets length of a sentence in characters as a potential sorting feature for a less consistent looking sort (aestetic purposes) not used currently, but I like to have as an option
    data['sentenceLen'] = [len(x) for x in data['Sentence']]
    
    #Randomizes the lines displayed by picking a random 34 lines from each house
    sortby = 'numWords'
    gryf = data[data['House']=='Gryffindor'].sample(25).sort_values(by=sortby, ascending = False)
    slyth = data[data['House']=='Slytherin'].sample(25).sort_values(by=sortby, ascending = False)
    raven = data[data['House']=='Ravenclaw'].sample(25).sort_values(by=sortby, ascending = False)
    if 'Hufflepuff' in list(data['House']): 
        huffle = data[data['House']=='Hufflepuff'].sample(25).sort_values(by=sortby, ascending = False)
    muggle = data[data['House']=='Muggle'].sample(25).sort_values(by=sortby, ascending = False)
    
    #Concat's all dataframes
    if 'Hufflepuff' in list(data['House']):
        data = pd.concat([gryf, slyth, raven, huffle, muggle]) #Makes a dataframe from random samples
    else:
        data = pd.concat([gryf, slyth, raven, muggle])
    
    #Creates house specific indexes for each house so that it can display nicely on the heatmap
    gryf, slyth, raven, huffle, muggle = 0,0,0,0,0
    houseIndexes = []
    for i in data['House']:
        if i == 'Gryffindor':
            gryf+=1
            houseIndexes.append(gryf)
        elif i == 'Slytherin':
            slyth+=1
            houseIndexes.append(slyth)
        elif i == 'Ravenclaw':
            raven+=1
            houseIndexes.append(raven)
        elif i == 'Hufflepuff':
            huffle+=1
            houseIndexes.append(huffle)
        else:
            muggle+=1
            houseIndexes.append(muggle)
    data['houseIndexes'] = houseIndexes
    
    chart = alt.Chart(data, title='Number of Words Per Line').mark_rect().encode(
        alt.X('houseIndexes:N', axis=alt.Axis(values=[]), title = ''),
        alt.Y('House:N', sort=['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'Muggle'], axis = alt.Axis(titleColor='black')),
        alt.Color('numWords', title='Number of Words', scale=alt.Scale(scheme='greenblue')),
        tooltip = ['Character', 'House', alt.Tooltip('MovieName', title='Movie'),\
                   alt.Tooltip('Sentence', title='Line'), alt.Tooltip('numWords', title='Number of words')]
    )
    chart = chart.properties(width=width, height=height) #1350, 400
    chart = chart.configure_axis(labelFontSize=15, titleFontSize=18) #Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20)
    chart = chart.configure_legend(titleColor='black', titleFontSize=16, labelFontSize=15) #Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2)
         
    return chart



#Streamlit components
st.set_page_config(page_title="Harry Potter Text Analysis", layout="wide") #Setting page title

#Displaying the HogwartsLogo.png at the top of the page
with open("HogwartsLogo.png", "rb") as file:
    contents = file.read()
    imgurl = base64.b64encode(contents).decode("utf-8")
st.markdown(f'<center><img src="data:image/gif;base64,{imgurl}" alt="Hogwarts Logo"></center>', unsafe_allow_html=True)


#This bit of markdown is really just the intro of why this project, what is the data, and what is my question
st.markdown("<h3 style='text-align: center; color: #000000;'>An analysis of the first three Harry Potter movies by Mason Lee</h3>", unsafe_allow_html=True)
st.markdown('##### Why this project?')
st.markdown("As a kid, I was always a big fan of the Harry Potter movies. It was something about the idea of magic, the worldbuilding, and the aesthetic that came with the movies that was really enjoyable as a kid, and it was something I never really stopped enjoying. With that in mind, I figured it could be fun to do some sort of analysis of the movies. What started as a fun project to work on in my free time ended up turning into my final project for my data visualization class!")
st.markdown('##### The Data')
st.markdown("What is this data about, anyway? The data to start off with contained every line from the first three Harry Potter movies as well as the character that said it. This was not a whole lot of information; however, it offered a lot of potential for creating new data, such as \"numWords\", which is the number of words in the sentence and should ideally give insight into the amount of content in a specific line, and \"House\", which is just what house the character is in. As a disclaimer, when separating characters into their respective houses, I created a \"muggle\" category as a catchall for characters that were not sorted into a house. This means that there are some characters (Dobby and Griphook) that are not technically muggles but do not have a house associated with them, and because of that, they were placed in the \"muggle\" category. That being said, what am I trying to do with all of this information? It's no secret that the Harry Potter movies are mostly dominated by Gryffindor. Gryffindor is cool and all, but wouldn't it be cool to hear from some of the other houses too? I'm hoping to explore and learn more about how different houses are represented across the first three Harry Potter movies. More specifically, I would like to show how the representation of houses in the Harry Potter movies evolves and changes as we progress further into the wizarding world!")


#Creating all tabs that actually contain data and descriptions for each movie
tab1, tab2, tab3, tab4 = st.tabs(["Sorcerer's Stone", "Chamber of Secrets", "Prizoner of Azkaban", "First 3 Movies Combined"])
         
    
with tab1:
    st.title("Analysis of Harry Potter and the Sorcerer's Stone")
    
    col1, col2 = st.columns([4,1])
    with col1:
        st.altair_chart(linesPerHouse(hp1, 1100, 630), use_container_width=True)
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("This is a great start to understanding what the rest of the data will start to look like. Of course, without surprise, Gryffindor has the most lines. This is to be expected, as the movies are first and foremost about them. The house with the second-most lines is Slytherin, and it has less than a tenth of what Gryffindor has! Ravenclaw has a surprising amount of representation in this movie, but not from the students. Ravenclaw's lines in this movie are actually largely made up of professors such as Quirrell and Professor Flitwick. Aside from houses, muggles account for about 12% of all lines in the first movie, and Hufflepuff has no lines, which does not bode well for the diversity between houses in this movie!")
    
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown('This chart is where we can start to see why the previous one, representing the number of lines per house, is so skewed toward Gryffindor. The first important thing to note is that Harry alone has 330 lines, which makes up about 20% of all lines in the movies. Aside from that, all six of the top six characters with the most lines are all in Gryffindor, and their lines make up about 67% of all lines! Besides Gryffindor, the next four characters on the chart are all outside of Gryffindor and offer a little bit of exploration into different houses. Slytherin definitely has two very important characters, Draco and Snape, who both made it into the top 11 most frequently spoken characters. Additionally, Quirrell makes a decent-sized dent in the Ravenclaw representation in this movie.')
    with col2:
        st.altair_chart(linesPerCharacter(hp1, 1100, 630))
    
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown('##### Number of Words Spoken Per Line by House')
        st.pyplot(numWordsVP(hp1, 10, 5), use_container_width=True)
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("These violin plots are where we take our first dive into the number of words per sentence. Instead of telling us how many total lines each house has, this metric should explain how much content is actually in each line. From these plots, we can see that while Gryffindor has a lot of lines, however a lot of them do not have a lot of words in them, so it's very dense towards the bottom. Meanwhile, Slytherin didn't manage to beat Gryffindor's record of most words per line, but it looks like towards the top of the plot it's thicker than Gryffindor, which leads me to believe that while Slytherin had fewer lines than Gryffindor, it's possible that their lines had a lot more content to them, and I would argue the same for Ravenclaw!")
    
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("The first thing that really stands out in this jitter plot is that for the houses with more lines, such as Gryffindor, the points can get very dense, especially toward the bottom. Feel free to zoom in to get a closer view and explore some of the data on your own! (Double-click the plot to reset the view!). Here we can see that each house is more dense towards the bottom, but for Slytherin and Ravenclaw, it looks like they tend to have more to say in relation to the number of lines they have in total. Also, it looks like muggles in this movie tend to say a lot less per line than some of the houses. These findings lead me to believe that Slytherins and Ravenclaws have fewer lines in total, but the lines they do have are often more meaningful!")
    with col2:
        st.altair_chart(numWordsPerLineJP(hp1, 1100, 630))
    
    st.altair_chart(numWordsPerLineHM(hp1, 1350, 400))
    st.button('New random sample', key='hp1')
    st.markdown("This heatmap is the last visualization about the number of words per line. There's a color scale on the right that says that the sentences with more words are darker, and the lighter ones have fewer words per line. This can generally be interpreted as the darker spots tending to be more dense with content, meaning more coming from that character, which is a representation of the house they are a part of. Keep in mind that this plot comes from a random sample of 25 lines from each house, so results can vary based on the sample. Feel free to press the button below a couple times to get a feel for the data using different samples!")
    
    st.markdown("<h3 color: #000000;'>Conclusions</h3>", unsafe_allow_html=True)
    st.markdown("This movie overall mostly just does a good job of representing Gryffindor. This is to be expected, especially considering it's still the first movie and we're just starting to get to know the characters. This being said, there was still some decent representation of other houses in this movie. Not a great amount, but definitely some. Slytherin had a pretty great introduction, mostly featuring Draco Malfoy and Professor Snape, and there were a couple Ravenclaws that had a decent amount of lines in the movie too. Muggles also made up a decent portion of the lines in this movie, which is largely due to the beginning of the movie taking place in the muggle world. Overall, I think there definitely could have been more representation of other houses, especially Hufflepuff, but Slytherin and Ravenclaw still managed to make an impression in this one!")

  
  
with tab2:
    st.title("Analysis of Harry Potter and the Chamber of Secrets")
    
    col1, col2 = st.columns([4,1])
    with col1:
        st.altair_chart(linesPerHouse(hp2, 1100, 630))
    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("This is a great start to understanding what the rest of the data will start to look like. Of course, without surprise, Gryffindor has the most lines. This is to be expected, as the movies are first and foremost about them. A very exciting development in this movie is the introduction of Hufflepuff characters that speak! While it's not much, Hufflepuffs have a total of 34 lines in The Chamber of Secrets! Another cool thing to be noted in this chart is that Slytherin and Ravenclaw lines went up by a lot, while the number of Gryffindor lines actually went down. Slytherin came in with a total of 251 lines in this movie, which is about 2.5 times more than they had in The Sorcerer's Stone!")
    
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("This chart is where we can start to see why the previous one, representing the number of lines per house, is so skewed toward Gryffindor. While, much like the last movie, it's still heavily skewed toward Gryffindor, it made significant progress toward the representation of other houses! One of the big things that can't go unnoticed in this chart is the appearance and significance of Gilderoy Lockhart in this movie. Lockhart provided the majority of Ravenclaw lines in this movie, contributing a total of 121 lines, with the only other major contributor being Moaning Myrtle. Slytherin has a couple characters that made it into the top 11 with the most lines this time, including two Malfoys (Lucius and Draco) and Tom Riddle, who collectively made up a good portion of the movie's lines.")
    with col2:
        st.altair_chart(linesPerCharacter(hp2, 1100, 630))
    
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown('##### Number of Words Spoken Per Line by House')
        st.pyplot(numWordsVP(hp2, 10, 5), use_container_width=True)
    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("These violin plots are where we take our first dive into the number of words per sentence. Instead of telling us how many total lines each house has, this metric should explain how much content is actually in each line. It looks like in this movie, Slytherin has the line with the most words in it rather than Gryffindor, which is very cool to see! Additionally, it looks like Ravenclaw once again tends to have a higher word density per line than some of the other houses! This leads me to believe that while they don't have as many lines as Gryffindor, they have a lot to say in the ones they do have. Hufflepuff looks like it's pretty dense towards the bottom, which implies that they don't really say too much in the few lines that they do have.")
    
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("The first thing that really stands out in this jitter plot is that for the houses with more lines, such as Gryffindor, the points can get very dense, especially toward the bottom. Feel free to zoom in to get a closer view and explore some of the data on your own! (Double-click the plot to reset the view!) One of the things that I saw in the violin plot that is also prevalent here is the Ravenclaw lines and how their distribution doesn't tend towards the bottom as much as some of the others do, partially because there's less data but also because they just generally say more than others do with their lines. Another notable thing about this plot is that Slytherin got the sentence with the largest number of words in this movie at 36 words!")
    with col2:
        st.altair_chart(numWordsPerLineJP(hp2, 1100, 630))
    
    st.altair_chart(numWordsPerLineHM(hp2, 1350, 400))
    st.button('New random sample', key='hp2')
    st.markdown("This heatmap is the last visualization about the number of words per line. There's a color scale on the right that says that the sentences with more words are darker, and the lighter ones have fewer words per line. This can generally be interpreted as the darker spots tending to be more dense with content, meaning more coming from that character, which is a representation of the house they are a part of. Keep in mind that this plot comes from a random sample of 25 lines from each house, so results can vary based on the sample. Feel free to press the button below a couple times to get a feel for the data using different samples!")
   
    st.markdown("<h3 color: #000000;'>Conclusions</h3>", unsafe_allow_html=True)
    st.markdown("I would say that this movie has the most representation of different houses across the first three movies. Most notably, we got our first Hufflepuff lines in this movie, and while it wasn't a lot, it's still a step up from 0 Hufflepuff lines! Aside from that, I feel like the representation of the other two houses was pretty good in this movie. Each house got a fair amount of lines, while the story still stayed mostly focused on Gryffindor, as it was meant to be. Both Slytherin and Ravenclaw, while not having a ton of lines each, had a lot to say in the lines that they did have! One thing to note in this movie, though, is that while Ravenclaw did have a lot of lines, the majority of those lines were said by Gilderoy Lockhart, which, on one hand, would have been cool to hear from more than him in terms of Ravenclaws; however, on the other hand, it's cool because it really gave a good amount of time for that one character from a different house to develop into a more important character!")

  
  
with tab3:
    st.title("Analysis of Harry Potter and the Prizoner of Azkaban")

    col1, col2 = st.columns([4,1])
    with col1:
        st.altair_chart(linesPerHouse(hp3, 1100, 630))
    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("This is a great start to understanding what the rest of the data will start to look like. Of course, without surprise, Gryffindor has the most lines. This is to be expected, as the movies are first and foremost about them. It looks like we're back to square one in terms of house representation. Hufflepuff is back to having zero lines, and Ravenclaw even went back a step! With the absence of Gilderoy Lockhart, Ravenclaw has suffered a massive hit in the number of lines spoken in this movie. Ravenclaw only has a total of 39 lines, and all of them were said by one person: Professor Trelawney. However, Slytherin still manages to keep up its numbers a bit, at least more than the first movie, despite being knocked down a bit in numbers since the last movie.")
    
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("This chart is where we can start to see why the previous one, representing the number of lines per house, is so skewed toward Gryffindor. In this chart, we can see that pretty much all of the characters with the most lines are in Gryffindor. All seven of the top seven characters with the most lines are in Gryffindor and account for about 67 percent of the total lines in the movie. With that in mind, we still have some other characters that managed to get into the top 11 characters with the most lines. Three of the four characters left are in Slytherin: Snape, Cornelius Fudge, and Draco Malfoy, two of whom have been in the top 11 most-spoken characters for all three of the first three movies! Also on that list is the only speaking Ravenclaw in the movie: Professor Trelawney!")
    with col2:
        st.altair_chart(linesPerCharacter(hp3, 1100, 630))
    
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown('##### Number of Words Spoken Per Line by House')
        st.pyplot(numWordsVP(hp3, 10, 5), use_container_width=True)
    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("These violin plots are where we take our first dive into the number of words per sentence. Instead of telling us how many total lines each house has, this metric should explain how much content is actually in each line. These plots look like they're all pretty consistently dense at the bottom, around the five-word mark. From the looks of the Ravenclaw violin plot, it seems like there's a bit more density at the top, but considering there's only one Ravenclaw in the movie and there are only 39 lines, I'd say that it's more than likely just due to an outlier or two. The other thing that I notice in these plots is that even though Slytherin maybe doesn't consistently make it to a very high number of words per sentence, they still manage to get the record for this movie too!")
    
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('The first thing that really stands out in this jitter plot is that for the houses with more lines, such as Gryffindor, the points can get very dense, especially toward the bottom. Feel free to zoom in to get a closer view and explore some of the data on your own! (Double-click the plot to reset the view!) One of the main things that I notice initially in this plot is how often Slytherin makes it towards the top, mostly due to Fudge and Snape having a couple of lines that make it pretty high. Ravenclaw also makes it pretty high a couple times despite having very few lines! As for the muggles in this movie, it seems like they pretty much all stay towards the bottom of the plot, with most of their lines being less than 10 words.')
    with col2:
        st.altair_chart(numWordsPerLineJP(hp3, 1100, 630))
    
    st.altair_chart(numWordsPerLineHM(hp3, 1350, 400))
    st.button('New random sample', key='hp3')
    st.markdown("This heatmap is the last visualization about the number of words per line. There's a color scale on the right that says that the sentences with more words are darker, and the lighter ones have fewer words per line. This can generally be interpreted as the darker spots tending to be more dense with content, meaning more coming from that character, which is a representation of the house they are a part of. Keep in mind that this plot comes from a random sample of 25 lines from each house, so results can vary based on the sample. Feel free to press the button below a couple times to get a feel for the data using different samples!")
    
    st.markdown("<h3 color: #000000;'>Conclusions</h3>", unsafe_allow_html=True)
    st.markdown("In my opinion, this movie takes a huge step backward in terms of the representation of different houses. Each house except Gryffindor had fewer lines than the last movie, and Hufflepuff is back to square one with 0 lines in this movie. Not only did Ravenclaw go from 147 lines in The Chamber of Secrets down to 39 lines in The Prisoner of Azkaban, but all of those lines were said by one character. While Slytherin still had fewer lines than the previous movie, it wasn't as bad as the number of Ravenclaw lines in this movie. Slytherin also had more people representing them than Ravenclaw did, with three of their top speaking characters making it to the top 11 most-spoken characters in the movie! However, I would say that this movie had the least representation of other houses of all three of the first three movies.")



with tab4:
    st.title("Analysis of Harry Potter and the Sorcerer's Stone, Chamber of Secrets, and Prizoner of Azkaban")

    col1, col2 = st.columns([4,1])
    with col1:
        st.altair_chart(linesPerHouse(hp123, 1100, 630))
    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown('This is a great start to understanding what the rest of the data will start to look like. Of course, without surprise, Gryffindor has the most lines, more than six times as many as the house with the second-most lines, Slytherin. This is, of course, to be expected, as the movies are first and foremost about them. That being said, Slytherin and muggles come in with pretty close numbers. Muggles are only off by 19 lines! Next in the ranking of houses with the most lines is Ravenclaw, with 280 lines, with about 43% of all of those lines coming from Gilderoy Lockhart. Then, not very surprisingly, Hufflepuff comes in last with only 34 lines across all three movies.')
    
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("This chart is where we can start to see why the previous one, representing the number of lines per house, is so skewed toward Gryffindor. The first seven characters with the most lines alone are all in Gryffindor and make up more than 60% of all lines spoken across all three movies! Aside from the top seven that make it so skewed, we have a bit of a mix in the houses of the last four characters. Keeping with the trend of the other movies, both Snape and Draco are keeping up the Slytherin numbers, both making it to the top 11 most frequently speaking characters! The last two characters are Gilderoy Lockhart, who had almost all of the Ravenclaw lines in the Chamber of Secrets, and Uncle Vernon, who had a total of 90 lines.")
    with col2:
        st.altair_chart(linesPerCharacter(hp123, 1100, 630))
    
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown('##### Number of Words Spoken Per Line by House')
        st.pyplot(numWordsVP(hp123, 10, 5), use_container_width=True)
    with col2:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("These violin plots are where we take our first dive into the number of words per sentence. Instead of telling us how many total lines each house has, this metric should explain how much content is actually in each line. From the looks of it, Slytherin and Gryffindor are the houses that share the record for the most number of words in a sentence; however, it looks like Gryffindor is more dense toward the bottom of their plot, which leads me to believe that Gryffindor lines tend to be a little shorter than Slytherin lines. I would also argue the same for Ravenclaw. If you look at the other three plots, you can notice that they're thicker toward the bottom than Slytherin and Ravenclaw, which would imply that they typically have shorter lines than Slytherin and Ravenclaw!")
    
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown('')
        st.markdown('')
        st.markdown('')
        st.markdown("The first thing that really stands out in this jitter plot is that for the houses with more lines, such as Gryffindor, the points can get very dense, especially toward the bottom. Feel free to zoom in to get a closer view and explore some of the data on your own! (Double-click the plot to reset the view!). From this plot, we can see that some of the ideas from the violin plots about Slytherin and Ravenclaw having more words per line tend to be true here too. They're still dense towards the bottom, but they do a pretty good job of having more content in their sentences too! As for Hufflepuff, it looks like they do a decent job of getting a decent amount of words in, especially considering the number of lines they have.")
    with col2:
        st.altair_chart(numWordsPerLineJP(hp123, 1100, 630))
    
    st.altair_chart(numWordsPerLineHM(hp123, 1350, 400))
    st.button('New random sample', key='hp123')
    st.markdown("This heatmap is the last visualization about the number of words per line. There's a color scale on the right that says that the sentences with more words are darker, and the lighter ones have fewer words per line. This can generally be interpreted as the darker spots tending to be more dense with content, meaning more coming from that character, which is a representation of the house they are a part of. Keep in mind that this plot comes from a random sample of 25 lines from each house, so results can vary based on the sample. Feel free to press the button below a couple times to get a feel for the data using different samples!")
    
    st.markdown("<h3 color: #000000;'>Conclusions</h3>", unsafe_allow_html=True)
    st.markdown("The first three movies as a whole are relatively diverse, but they definitely could have been more so. Of course the story is about Gryffindor, so the representation is bound to be heavily skewed toward them; however, there were definitely moments across the movies where some characters belonging to other houses got their fair share of time, whether that be a character like Draco who got a bit more time than a lot of the other characters, or if it were a character with some more in-depth lines than the majority of the Gryffindor lines. One of the most notable things is how little Hufflepuff shows up in the first three movies, with only 34 lines across all three movies, making up less than 1% of all lines across all three movies! That being said, Slytherin and Ravenclaw still managed to do a pretty good job of not letting Gryffindor completely rule the story!")
