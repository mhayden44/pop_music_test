from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import random

class Frames(object):

    #Callback function that closes all windows
    def exitWindows(self):
        if master is not None and master.winfo_exists():
            master.destroy()
        if windowThree is not None and windowThree.winfo_exists():
            windowThree.destroy()
        if windowTwo is not None and windowTwo.winfo_exists():
            windowTwo.destroy()

    #Window Two (Results and comparison sheet)
    def openNewWindow(self):
        mainPopArtists=["Taylor Swift", "Justin Bieber", "Katy Perry", "Harry Styles", "The Weeknd", "Selena Gomez", "Lady Gaga", "Britney Spears", "Ariana Grande", "Rihanna", "Adele", "Dua Lipa"]
        indiePopArtists=["Billie Eilish", "MGMT", "Lorde", "Poppy", "Carly Rae Jepsen", "Charli XCX","Empire of the Sun",  "The Neighbourhood", "Gorillaz", "Grimes", "Lana Del Rey", "Marina", "Tame Impala", "Beach House"]
        originalPopArtistList=self.popArtistList
        windowTwo = Toplevel()
        windowTwo.title("Results")
        windowTwo.geometry("550x395+1130+300")
        windowTwo.resizable(False, False)
        popArtistOne=self.entryOne.get()
        popArtistTwo=self.entryTwo.get()
        popArtistThree=self.entryThree.get()

        
        #Returns an error window if the user does not enter valid entries.
        if popArtistOne not in originalPopArtistList:
            windowTwo.destroy()
            messagebox.showerror("Error","First entry is invalid.")
        elif popArtistTwo not in originalPopArtistList:
            windowTwo.destroy()
            messagebox.showerror("Error","Second entry is invalid.")
        elif popArtistThree not in originalPopArtistList:
            windowTwo.destroy()
            messagebox.showerror("Error","Third entry is invalid.")
        #Returns an error window if the user trys to enter the same artist in two or more of the entry boxes.
        elif popArtistOne == popArtistTwo:
            windowTwo.destroy()
            messagebox.showerror("Error","Cannot have two identical entries.")
        elif popArtistOne == popArtistThree:
            windowTwo.destroy()
            messagebox.showerror("Error","Cannot have two identical entries.")
        elif popArtistTwo == popArtistThree:
            windowTwo.destroy()
            messagebox.showerror("Error","Cannot have two identical entries.")
        else:
            pass
        
        #Initializes two new empty lists to be filled
        newMainPopList=[]
        newIndiePopList=[]
        #Filters out any "mainstream" pop artists enterred by the user and inputs them into a new list.
        for mainPopArtist in mainPopArtists:
            if mainPopArtist != popArtistOne and mainPopArtist != popArtistTwo and mainPopArtist != popArtistThree:
                newMainPopList.append(mainPopArtist)
        
        #Filters out any "indie" pop artists enterred by the user and inputs them into a new list.
        for indiePopArtist in indiePopArtists:
            if indiePopArtist != popArtistOne and indiePopArtist != popArtistTwo and indiePopArtist != popArtistThree:
                newIndiePopList.append(indiePopArtist)

        #Checks to see if each enterred pop artist is "mainstream" or "indie"
        for x in mainPopArtists:
            if popArtistOne in x:
                popArtistOneGenre = "Mainstream"
        for x in indiePopArtists:
            if popArtistOne in x:
                popArtistOneGenre = "Indie"
        for x in mainPopArtists:
            if popArtistTwo in x:
                popArtistTwoGenre = "Mainstream"
        for x in indiePopArtists:
            if popArtistTwo in x:
                popArtistTwoGenre = "Indie"
        for x in mainPopArtists:
            if popArtistThree in x:
                popArtistThreeGenre = "Mainstream"
        for x in indiePopArtists:
            if popArtistThree in x:
                popArtistThreeGenre = "Indie"
                
        #Initializes three empty lists to be filled randomly depending on what each artist's genre that the user enterred is.
        popArtistOneSuggested=[]
        popArtistTwoSuggested=[]
        popArtistThreeSuggested=[]
        
        #Checks what genre each enterred pop artist is and returns three randomly selected artists of the same genre.
        if popArtistOneGenre == "Mainstream":
            popArtistOneSuggested = random.sample(newMainPopList,3)
        elif popArtistOneGenre == "Indie":
            popArtistOneSuggested = random.sample(newIndiePopList,3)
        if popArtistTwoGenre == "Mainstream":
            popArtistTwoSuggested = random.sample(newMainPopList,3)
        elif popArtistTwoGenre == "Indie":
            popArtistTwoSuggested = random.sample(newIndiePopList,3)
        if popArtistThreeGenre == "Mainstream":
            popArtistThreeSuggested = random.sample(newMainPopList,3)
        elif popArtistThreeGenre == "Indie":
            popArtistThreeSuggested = random.sample(newIndiePopList,3)
            
        #Format and label column titles.
        artistLabel= Label(windowTwo,font='Helvetica 9 bold',width =25, height=6, borderwidth = 1,relief="solid", text=("Artist")).grid(row=0,column=1,padx=2,pady=2)
        genreLabel= Label(windowTwo,font='Helvetica 9 bold',width =25, height=6, borderwidth = 1,relief="solid", text=("Genre")).grid(row=0,column=2,padx=2,pady=2)
        similarArtistLabel= Label(windowTwo,font='Helvetica 9 bold',width =25, height=6, borderwidth = 1,relief="solid", text=("Similar Artists")).grid(row=0,column=3,padx=2,pady=2)
        
        #Each pop artist that the user enterred is displayed along the first column.
        popArtistOneLabel = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid", text=popArtistOne).grid(row=1,column=1,padx=2,pady=2)
        popArtistTwoLabel = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid",text=popArtistTwo).grid(row=2,column=1,padx=2,pady=2)
        popArtistThreeLabel = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid", text=popArtistThree).grid(row=3,column=1,padx=2,pady=2)
        
        #The corresponding genre of each enterred pop artist is displayed along the second column.
        popArtistOneGenreLabel = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid", text=popArtistOneGenre).grid(row=1,column=2,padx=2,pady=2)
        popArtistTwoGenreLabel = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid", text=popArtistTwoGenre).grid(row=2,column=2,padx=2,pady=2)
        popArtistThreeGenreLabel = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid", text=popArtistThreeGenre).grid(row=3,column=2,padx=2,pady=2)
        
        #The suggested artists are displayed along the third column.
        popArtistOneSuggestedLabelBox = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid", text="").grid(row=1,column=3,padx=2,pady=2)
        popArtistTwoSuggestedLabelBox = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid", text="").grid(row=2,column=3,padx=2,pady=2)
        popArtistThreeSuggestedLabelBox = Label(windowTwo, width =25, height=6,borderwidth = 1,relief="solid", text="").grid(row=3,column=3,padx=2,pady=2)
        
        #Formatting to display the suggested artists in a vertical list.
        artistOneSuggesteds=popArtistOneSuggested
        text1=Text(windowTwo, width = 16, height = 5,font='Helvetica, 9', bg='#F0F0ED',relief="flat")
        text1.grid(row=1,column=3,padx=2,pady=2)
        for artistOneSuggested in artistOneSuggesteds:
            text1.insert(END,artistOneSuggested + '\n'+'\n')
        
        artistTwoSuggesteds=popArtistTwoSuggested
        text2=Text(windowTwo, width = 16, height = 5,font='Helvetica, 9', bg='#F0F0ED',relief="flat")
        text2.grid(row=2,column=3,padx=2,pady=2)
        for artistTwoSuggested in artistTwoSuggesteds:
            text2.insert(END,artistTwoSuggested + '\n'+'\n')

        artistThreeSuggesteds=popArtistThreeSuggested
        text3=Text(windowTwo, width = 16, height = 5,font='Helvetica, 9', bg='#F0F0ED',relief="flat")
        text3.grid(row=3,column=3,padx=2,pady=2)
        for artistThreeSuggested in artistThreeSuggesteds:
            text3.insert(END,artistThreeSuggested + '\n'+'\n')

    #Window Three (Artist List)
    def openArtistList(self):
        windowThree = Toplevel()
        windowThree.title("Pop Artist List")
        windowThree.geometry("250x475+250+300")
        windowThree.resizable(False, False)

        #Images
        image3 = Image.open("TaylorSwift.png")
        resize_image3=image3.resize((50,50))
        photo3 = ImageTk.PhotoImage(resize_image3)
        img_label3 = Label(windowThree,image=photo3)
        img_label3.image = photo3
        img_label3.place(x=25,y=420)
        
        image4 = Image.open("LanaDel.jpg")
        resize_image4=image4.resize((50,50))
        photo4 = ImageTk.PhotoImage(resize_image4)
        img_label4 = Label(windowThree,image=photo4)
        img_label4.image = photo4
        img_label4.place(x=100,y=420)

        image2 = Image.open("TameImpala.jpg")
        resize_image2=image2.resize((50,50))
        photo2 = ImageTk.PhotoImage(resize_image2)
        img_label2 = Label(windowThree,image=photo2)
        img_label2.image = photo2
        img_label2.place(x=175,y=420)
        
        #Basic loop to display the artist list in a vertical list.
        artists=self.popArtistList
        text=Text(windowThree, width = 30, height = 26)
        text.pack()
        for artist in artists:
            text.insert(END, artist +'\n')


    #Window One
    def windowOne(self,master):
        master.title("Top three pop artists")
        master.geometry("630x630+500+300")
        master.resizable(False, False)

        #Creates the background photo for the main window.
        image1 = Image.open("CarlyRae.jpg")
        photo = ImageTk.PhotoImage(image1)
        img_label = Label(master, image=photo)
        img_label.image = photo
        img_label.place(x=0,y=0)

        #Initializes three variables to be StringVars().
        self.entryOne = StringVar()
        self.entryTwo = StringVar()
        self.entryThree = StringVar()
        self.popArtistList=["Adele", "Ariana Grande", "Beach House", "Billie Eilish", "Britney Spears", "Carly Rae Jepsen", "Charli XCX", "Dua Lipa", "Empire of the Sun", "Gorillaz", "Grimes", "Harry Styles", "Justin Bieber", "Katy Perry",
                            "Lady Gaga", "Lana Del Rey", "Lorde", "Marina", "MGMT", "Rihanna", "Poppy", "Selena Gomez", "Tame Impala", "Taylor Swift", "The Neighbourhood", "The Weeknd" ]

        #Labels that ask the user what their top three favorite pop artists are.
        popArtistOneLabel = Label(text="Who is your favorite pop artist?", foreground="black",background="white",width=30,height=1)
        popArtistTwoLabel = Label(text="Who is your second favorite pop artist?",foreground="black",background="white",width=30,height=1)
        popArtistThreeLabel = Label(text="Who is your third favorite pop artist?",foreground="black",background="white",width=30,height=1)

        #Takes the input of the user and stores it into each ones' respective variable.
        popArtistOneEntry = Entry(master, borderwidth=3,relief="sunken", textvariable=self.entryOne)
        popArtistTwoEntry = Entry(master, borderwidth=3,relief="sunken", textvariable=self.entryTwo)
        popArtistThreeEntry = Entry(master, borderwidth=3,relief="sunken", textvariable=self.entryThree)

        #Button that takes the user to window three where they can view a list of the support pop artists to be inputted. Calls back to 'openArtistList'
        popArtistListButton = Button(master,borderwidth=5,relief="raised", text = "Click to view a list of supported pop artists", command = self.openArtistList)
        popArtistListButton.pack()
        
        popArtistOneLabel.pack()
        popArtistOneEntry.pack()
        popArtistTwoLabel.pack()
        popArtistTwoEntry.pack()
        popArtistThreeLabel.pack()
        popArtistThreeEntry.pack()

        #Button that takes the user to window two where they can view information related to their entries. Calls back to 'openNewWindow'
        windowOneButton = Button(master,borderwidth=5,relief="raised", text = "Click to submit", command = self.openNewWindow)
        windowOneButton.pack()

        #Button to close all windows that are open. Calls back to 'exitWindows'
        exitWindowsButton = Button(master, borderwidth=5,relief="raised", text = "Click to close all windows", command = self.exitWindows)
        exitWindowsButton.place(x=240, y=590)

master = Tk()
app = Frames()
app.windowOne(master)
master.mainloop()
