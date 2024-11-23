# Harry Potter Script Analysis
# GenerateVisualizations.py
# Author: Mason Lee

import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

def linesPerHouse(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return an altair chart that shows the total number of lines in each house from that data"""
    
    houseLines = data.groupby('House', as_index=False).count() # Groups data by house
    houseLines['Number of Lines'] = houseLines['Sentence'] # Saved for the tooltip later

    # Logging data in order to normalize it, otherwise it's very skewed
    houseLines['Sentence'] = [np.around(np.log10(x),2) for x in houseLines['Sentence']]

    # Keeps Hufflepuff in the chart even if they have no lines
    if 'Hufflepuff' not in houseLines['House']:
        # Adds the housename + rest of the colunms as 0 (weird numpy workaround due to varying dataframe sizes)
        houseLines.loc[len(houseLines.index)] = ['Hufflepuff'] + list(np.zeros(len(data.columns)))
        
    # Define color parameters based on whether or not Hufflepuff has any lines
    if 'Hufflepuff' in list(data['House']):
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'Muggle']
        colors = ['#be0119', '#009500', '#069af3', '#feb308', '#5f6b73']
    else:
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Muggle', 'Hufflepuff']
        colors = ['#be0119', '#009500', '#069af3', '#5f6b73', '#feb308']
    
    # Setting axis labels [weird javascript thing >:(]
    axisLabels = "datum.label == 1 ? '10 lines' : datum.label == 2 ? '100 lines' : '1000 lines'"
    labelVals = [1,2,3]
    
    # Create chart
    chart = alt.Chart(houseLines, title = 'Number of Lines per House').mark_bar().encode(
        alt.X('House', sort=houses,\
             axis=alt.Axis(labelAngle=0, titleColor = 'black')),
        alt.Y('Sentence', title='Number of Lines (log10 scale)',\
              scale=alt.Scale(domain=[0, houseLines['Sentence'].max()+houseLines['Sentence'].max()*.007]),\
              axis=alt.Axis(labelExpr=axisLabels, values=labelVals, titleColor = 'black')),
        color = alt.Color('House', scale=alt.Scale(domain = houses, range=colors)),
        tooltip=['House', 'Number of Lines']
    )
    chart = chart.properties(width=width, height=height) # Set figure size w685 h475
    chart = chart.configure_axis(labelFontSize=15, titleFontSize=18) # Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20) # Sets title size
    chart = chart.configure_legend(titleColor='black', titleFontSize=17, labelFontSize=15) # Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2) # Sets a border around the chart
    
    return chart


def linesPerCharacter(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return an altair chart that shows the top 11 most speaking characters colored by their house"""

    # Defining houses
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

    # Getting new data that's grouped by the character
    spokenLines=data.drop(['normText', 'House', 'MovieName', 'MovieNumber', 'numWords'], axis=1) # Drops unnecessary cols
    spokenLines = spokenLines.groupby('Character', as_index=False).count() # Groups by Character and counts the lines
    spokenLines.sort_values('Sentence', ascending=False, inplace=True) # Sorts values
    spokenLines = spokenLines[spokenLines['Character'] != 'Background Character'] # Removing background character becasue it doesn't make much sense in this visualization

    # Getting the house for each character
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

    # Adding columns that couldn't be aggregated in groupby
    spokenLines['House'] = house
    
    # Defining these for setting color
    houseColors = {'Gryffindor':'#be0119', 'Slytherin':'#009500', 'Ravenclaw':'#069af3', 'Muggle':'#5f6b73'}

    # Creating the chart
    chart = alt.Chart(spokenLines.head(11), title = 'Number of Lines per Character').mark_bar().encode(
        alt.X('Character', sort=alt.EncodingSortField(field="Character", op="count", order='ascending'),\
              axis=alt.Axis(labelAngle=0, titleColor='black')), #Character sorted by number of lines
        alt.Y('Sentence', title='Number of Lines', axis=alt.Axis(titleColor='black')), #Number of lines
        color = alt.Color('House', scale=alt.Scale(domain=list(houseColors.keys()), range=list(houseColors.values()))),
        tooltip = ['Character', 'House', alt.Tooltip('Sentence', title='Number of Lines')] #Adds tooltip
    )
    chart = chart.properties(width=width, height=height) # Set figure size w690 h518
    chart = chart.configure_axis(labelFontSize=14, titleFontSize=18) # Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20) # Sets title size
    chart = chart.configure_legend(titleColor='black', titleFontSize=17, labelFontSize=15) # Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2) # Sets a border around the chart 
    
    return chart


def numWordsVP(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return a matplotlib figure that has seaborn violin plots on it representing the number of words per line by house"""
    
    # Creating the figure
    fig, ax = plt.subplots(figsize=(width, height))
    fig.set_facecolor('White')
    
    # Setting colors according to whether or not Hufflepuff has any lines 
    houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Muggle']
    colors = ['#be0119', '#009500', '#069af3', '#5f6b73']
    if 'Hufflepuff' in list(data['House']):
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'Muggle']
        colors = ['#be0119', '#009500', '#069af3', '#feb308', '#5f6b73']
        
    # Creating the actual plot
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
    
    # Setting house colors
    houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'Muggle']
    colors = ['#be0119', '#009500', '#069af3', '#feb308', '#5f6b73']
    
    # Getting x-axis values (jittered within .35)
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
    
    # Setting axis labels [weird javascript thing >:(] Based on whether or not Hufflepuff has any lines
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
    chart = chart.properties(width=width, height=height) # Set figure size w750 h600
    chart = chart.configure_axis(labelFontSize=15, titleFontSize=18) # Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20) # Sets title size
    chart = chart.configure_legend(titleColor='black', titleFontSize=17, labelFontSize=15) # Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2) # Sets a border around the chart
    chart = chart.interactive()

    return chart


def numWordsPerLineHM(data, width, height):
    """This takes in data that is one of the hpn dataframes, and the width and height of the figure
    It should return an altair chart that shows a heatmap that takes a random sample of 25 lines per house and colors them by number of words per sentence"""
    
    # Gets length of a sentence in characters as a potential sorting feature for a less consistent looking sort (aestetic purposes) not used currently, but I like to have as an option
    data['sentenceLen'] = [len(x) for x in data['Sentence']]
    
    # Randomizes the lines displayed by picking a random 34 lines from each house
    sortby = 'numWords'
    gryf = data[data['House']=='Gryffindor'].sample(25).sort_values(by=sortby, ascending = False)
    slyth = data[data['House']=='Slytherin'].sample(25).sort_values(by=sortby, ascending = False)
    raven = data[data['House']=='Ravenclaw'].sample(25).sort_values(by=sortby, ascending = False)
    if 'Hufflepuff' in list(data['House']): 
        huffle = data[data['House']=='Hufflepuff'].sample(25).sort_values(by=sortby, ascending = False)
    muggle = data[data['House']=='Muggle'].sample(25).sort_values(by=sortby, ascending = False)
    
    # Concat's all dataframes
    if 'Hufflepuff' in list(data['House']):
        data = pd.concat([gryf, slyth, raven, huffle, muggle]) #Makes a dataframe from random samples
    else:
        data = pd.concat([gryf, slyth, raven, muggle])
    
    # Creates house specific indexes for each house so that it can display nicely on the heatmap
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