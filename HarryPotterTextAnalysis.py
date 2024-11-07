# Harry Potter Script Analysis
# HarryPotterTextAnalysis.py
# Author: Mason Lee

import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from pandasql import sqldf
from PIL import Image
import base64
import CleanHPData
import GenerateVisualizations


# Grab data from CleanHPData.py
hp1 = getHP1()
hp2 = getHP2()
hp3 = getHP3()
# Creating dataframe for all three movies combined (hp123)
hp123 = pd.concat([hp1, hp2, hp3])


# Streamlit components
st.set_page_config(page_title="Harry Potter Text Analysis", layout="wide") # Setting page title

# Displaying the HogwartsLogo.png at the top of the page
with open("HogwartsLogo.png", "rb") as file:
    contents = file.read()
    imgurl = base64.b64encode(contents).decode("utf-8")
st.markdown(f'<center><img src="data:image/gif;base64,{imgurl}" alt="Hogwarts Logo"></center>', unsafe_allow_html=True)


# This bit of markdown is really just the intro of why this project, what is the data, and what is my question
st.markdown("<h3 style='text-align: center; color: #000000;'>An Analysis of the First Three Harry Potter Movie Scripts by Mason Lee</h3>", unsafe_allow_html=True)
st.markdown('##### Why this project?')
st.markdown("As a kid, I was always a big fan of the Harry Potter movies. It was something about the idea of magic, the worldbuilding, and the aesthetic that came with the movies that was really enjoyable as a kid, and it was something I never really stopped enjoying. With that in mind, I figured it could be fun to do some sort of analysis of the movies. This is a fun project I put together primarily leaning on the streamlit Python library!")
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
        st.altair_chart(linesPerCharacter(hp1, 1100, 630), use_container_width=True)
    
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
        st.altair_chart(numWordsPerLineJP(hp1, 1100, 630), use_container_width=True)
    
    st.altair_chart(numWordsPerLineHM(hp1, 1350, 400), use_container_width=True)
    st.button('New random sample', key='hp1')
    st.markdown("This heatmap is the last visualization about the number of words per line. There's a color scale on the right that says that the sentences with more words are darker, and the lighter ones have fewer words per line. This can generally be interpreted as the darker spots tending to be more dense with content, meaning more coming from that character, which is a representation of the house they are a part of. Keep in mind that this plot comes from a random sample of 25 lines from each house, so results can vary based on the sample. Feel free to press the button below a couple times to get a feel for the data using different samples!")
    
    st.markdown("<h3 color: #000000;'>Conclusions</h3>", unsafe_allow_html=True)
    st.markdown("This movie overall mostly just does a good job of representing Gryffindor. This is to be expected, especially considering it's still the first movie and we're just starting to get to know the characters. This being said, there was still some decent representation of other houses in this movie. Not a great amount, but definitely some. Slytherin had a pretty great introduction, mostly featuring Draco Malfoy and Professor Snape, and there were a couple Ravenclaws that had a decent amount of lines in the movie too. Muggles also made up a decent portion of the lines in this movie, which is largely due to the beginning of the movie taking place in the muggle world. Overall, I think there definitely could have been more representation of other houses, especially Hufflepuff, but Slytherin and Ravenclaw still managed to make an impression in this one!")

  
  
with tab2:
    st.title("Analysis of Harry Potter and the Chamber of Secrets")
    
    col1, col2 = st.columns([4,1])
    with col1:
        st.altair_chart(linesPerHouse(hp2, 1100, 630), use_container_width=True)
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
        st.altair_chart(linesPerCharacter(hp2, 1100, 630), use_container_width=True)
    
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
        st.altair_chart(numWordsPerLineJP(hp2, 1100, 630), use_container_width=True)
    
    st.altair_chart(numWordsPerLineHM(hp2, 1350, 400), use_container_width=True)
    st.button('New random sample', key='hp2')
    st.markdown("This heatmap is the last visualization about the number of words per line. There's a color scale on the right that says that the sentences with more words are darker, and the lighter ones have fewer words per line. This can generally be interpreted as the darker spots tending to be more dense with content, meaning more coming from that character, which is a representation of the house they are a part of. Keep in mind that this plot comes from a random sample of 25 lines from each house, so results can vary based on the sample. Feel free to press the button below a couple times to get a feel for the data using different samples!")
   
    st.markdown("<h3 color: #000000;'>Conclusions</h3>", unsafe_allow_html=True)
    st.markdown("I would say that this movie has the most representation of different houses across the first three movies. Most notably, we got our first Hufflepuff lines in this movie, and while it wasn't a lot, it's still a step up from 0 Hufflepuff lines! Aside from that, I feel like the representation of the other two houses was pretty good in this movie. Each house got a fair amount of lines, while the story still stayed mostly focused on Gryffindor, as it was meant to be. Both Slytherin and Ravenclaw, while not having a ton of lines each, had a lot to say in the lines that they did have! One thing to note in this movie, though, is that while Ravenclaw did have a lot of lines, the majority of those lines were said by Gilderoy Lockhart, which, on one hand, would have been cool to hear from more than him in terms of Ravenclaws; however, on the other hand, it's cool because it really gave a good amount of time for that one character from a different house to develop into a more important character!")

  
  
with tab3:
    st.title("Analysis of Harry Potter and the Prizoner of Azkaban")

    col1, col2 = st.columns([4,1])
    with col1:
        st.altair_chart(linesPerHouse(hp3, 1100, 630), use_container_width=True)
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
        st.altair_chart(linesPerCharacter(hp3, 1100, 630), use_container_width=True)
    
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
        st.altair_chart(numWordsPerLineJP(hp3, 1100, 630), use_container_width=True)
    
    st.altair_chart(numWordsPerLineHM(hp3, 1350, 400), use_container_width=True)
    st.button('New random sample', key='hp3')
    st.markdown("This heatmap is the last visualization about the number of words per line. There's a color scale on the right that says that the sentences with more words are darker, and the lighter ones have fewer words per line. This can generally be interpreted as the darker spots tending to be more dense with content, meaning more coming from that character, which is a representation of the house they are a part of. Keep in mind that this plot comes from a random sample of 25 lines from each house, so results can vary based on the sample. Feel free to press the button below a couple times to get a feel for the data using different samples!")
    
    st.markdown("<h3 color: #000000;'>Conclusions</h3>", unsafe_allow_html=True)
    st.markdown("In my opinion, this movie takes a huge step backward in terms of the representation of different houses. Each house except Gryffindor had fewer lines than the last movie, and Hufflepuff is back to square one with 0 lines in this movie. Not only did Ravenclaw go from 147 lines in The Chamber of Secrets down to 39 lines in The Prisoner of Azkaban, but all of those lines were said by one character. While Slytherin still had fewer lines than the previous movie, it wasn't as bad as the number of Ravenclaw lines in this movie. Slytherin also had more people representing them than Ravenclaw did, with three of their top speaking characters making it to the top 11 most-spoken characters in the movie! However, I would say that this movie had the least representation of other houses of all three of the first three movies.")



with tab4:
    st.title("Analysis of Harry Potter and the Sorcerer's Stone, Chamber of Secrets, and Prizoner of Azkaban")

    col1, col2 = st.columns([4,1])
    with col1:
        st.altair_chart(linesPerHouse(hp123, 1100, 630), use_container_width=True)
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
        st.altair_chart(linesPerCharacter(hp123, 1100, 630), use_container_width=True)
    
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
        st.altair_chart(numWordsPerLineJP(hp123, 1100, 630), use_container_width=True)
    
    st.altair_chart(numWordsPerLineHM(hp123, 1350, 400), use_container_width=True)
    st.button('New random sample', key='hp123')
    st.markdown("This heatmap is the last visualization about the number of words per line. There's a color scale on the right that says that the sentences with more words are darker, and the lighter ones have fewer words per line. This can generally be interpreted as the darker spots tending to be more dense with content, meaning more coming from that character, which is a representation of the house they are a part of. Keep in mind that this plot comes from a random sample of 25 lines from each house, so results can vary based on the sample. Feel free to press the button below a couple times to get a feel for the data using different samples!")
    
    st.markdown("<h3 color: #000000;'>Conclusions</h3>", unsafe_allow_html=True)
    st.markdown("The first three movies as a whole are relatively diverse, but they definitely could have been more so. Of course the story is about Gryffindor, so the representation is bound to be heavily skewed toward them; however, there were definitely moments across the movies where some characters belonging to other houses got their fair share of time, whether that be a character like Draco who got a bit more time than a lot of the other characters, or if it were a character with some more in-depth lines than the majority of the Gryffindor lines. One of the most notable things is how little Hufflepuff shows up in the first three movies, with only 34 lines across all three movies, making up less than 1% of all lines across all three movies! That being said, Slytherin and Ravenclaw still managed to do a pretty good job of not letting Gryffindor completely rule the story!")
