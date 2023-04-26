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
hp2['Character'] = ['Lucius Malfoy' if x=='LuciusMalfoy' else x for x in hp2['Character']]
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
Slytherin=['Draco', 'Snape', 'Flint', 'Voldemort', 'Mr.Borgin', 'Lucius Malfoy', 'Crabbe', 'Tom Riddle', 'Fudge']
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
hp123 = pd.concat([hp1, hp2, hp3])





#Dataviz functions
def linesPerCharacter(data):
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
              axis=alt.Axis(labelAngle=-60)), #Character sorted by number of lines
        alt.Y('Sentence', title='Number of Lines'), #Number of lines
        color = alt.Color('House', scale=alt.Scale(domain=list(houseColors.keys()), range=list(houseColors.values()))),
        tooltip = ['Character', 'House', alt.Tooltip('Sentence', title='Number of Lines')] #Adds tooltip
    )
    chart = chart.properties(width=750, height=475) #Set figure size
    chart = chart.configure_axis(labelFontSize=12, titleFontSize=16) #Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20) #Sets title size
    chart = chart.configure_legend(titleColor='black', titleFontSize=14, labelFontSize=13) #Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2) #Sets a border around the chart 
    
    return chart






#Streamlit components
st.set_page_config(page_title="Harry Potter Text Analysis", layout="wide") #Setting page title

#Displaying the HogwartsLogo.png at the top of the page
with open("HogwartsLogo.png", "rb") as file:
    contents = file.read()
    imgurl = base64.b64encode(contents).decode("utf-8")
st.markdown(f'<center><img src="data:image/gif;base64,{imgurl}" alt="Hogwarts Logo"></center>', unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center; color: #000000;'>An analysis of the first three Harry Potter movies by Mason Lee</h3>", unsafe_allow_html=True)
st.markdown("As a kid, I was always a big fan of the Harry Potter movies. There was always something about the idea of magic, the worldbuilding, and the aesthetic that came with the movies that was something really enjoyable as a kid, and was something I never really stopped enjoying. With that in mind, I figured it could be fun to do some sort of analysis on them. While looking for available data about the movies to analyze as a fun side project, I stumbled across this dataset that contained every line from the first three movies. What started as a fun project to work on in my freetime ended up turning into my final project for my data visualization class!")
st.markdown("fundamental research question will go here")
st.markdown("Describe the data here")


tab1, tab2, tab3, tab4 = st.tabs(["First 3 Movies Combined", "Sorcerer's Stone", "Chamber of Secrets", "Prizoner of Azkaban"])

with tab1:
    st.title("Analysis of Harry Potter and the Sorcerer's Stone, Chamber of Secrets, and Prizoner of Azkaban")
    col1, col2 = st.columns(2)
    with col1:
        st.altair_chart(linesPerCharacter(hp123))
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
    with col2:
        image = Image.open('hpChart.png')
        st.image(image, caption='This will be a description of the chart')
        #fig, ax = plt.subplots()
        #st.pyplot(fig)
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
    
    st.markdown('This is just some text at the end of each page saying something about the findings of this tab in particular')
  
  
with tab2:
    st.title("Analysis of Harry Potter and the Sorcerer's Stone")
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('hpChart.png')
        st.image(image, caption='This will be a description of the chart')
    with col2:
        image = Image.open('hpChart.png')
        st.image(image, caption='This will be a description of the chart')
  
  
with tab3:
    st.title("Analysis of Harry Potter and the Chamber of Secrets")
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('hpChart.png')
        st.image(image, caption='This will be a description of the chart')
    with col2:
        image = Image.open('hpChart.png')
        st.image(image, caption='This will be a description of the chart')
  
  
with tab4:
    st.title("Analysis of Harry Potter and the Prizoner of Azkaban")
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('hpChart.png')
        st.image(image, caption='This will be a description of the chart')
    with col2:
        image = Image.open('hpChart.png')
        st.image(image, caption='This will be a description of the chart')
