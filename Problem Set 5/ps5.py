# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Palash Sharma
# Collaborators:
# Time: -> [30 min for NewsStory] + [FOREVER!]

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        """
        Constructor for initializing a NewsStory object
        
        guid (string): globally unique identifier (GUID)
        title (string): title of the new story
        decsription (string): description of the news story
        link (string): link to more content
        pubdate (datetime): publication date
        
        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate =  pubdate
        
    def get_guid(self):
        """
        Used to safely access self.guid outside the class
        
        Returns: self.guid
        """
        return self.guid
    
    def get_title(self):
        """
        Used to safely access self.title outside the class
        
        Returns: self.title
        """
        return self.title
    
    def get_description(self):
        """
        Used to safely access self.description outside the class
        
        Returns: self.description
        """
        return self.description
    
    def get_link(self):
        """
        Used to safely access self.link outside the class
        
        Returns: self.link
        """
        return self.link
    
    def get_pubdate(self):
        """
        Used to safely access self.pubdate outside the class
        
        Returns: self.pubdate
        """
        return self.pubdate
            


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        """
        Constructor to initialize a PhraseTrigger object
        
        phrase (string): a phrase to check if it is a trigger
        """
        self.phrase = phrase
        
    def is_phrase_in(self, text):
        no_punct_text = ''.join(ch if ch not in string.punctuation else ' ' for ch in text.upper())
        cleaned_text = ' '.join(no_punct_text.split()) + ' '
        no_punct_phrase = ''.join(ch if ch not in string.punctuation else ' '
                for ch in self.phrase.upper())
        cleaned_phrase = ' '.join(no_punct_phrase.split()) + ' '
        if cleaned_phrase not in cleaned_text:
            return False
        else:
            return True
        
        
# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())    


# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())
    
    
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
        
class TimeTrigger(Trigger):
    def __init__(self, str_time):
        """
        Constructor:
        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        Convert time from string to a datetime before saving it as an attribute.
        """
        time = datetime.strptime(str_time, "%d %b %Y %H:%M:%S")
        self.time = time

# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        try:
            result = story.get_pubdate() < self.time
        except TypeError:
            self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
            result = story.get_pubdate() < self.time
            
        return result
        

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        try:
            result = story.get_pubdate() > self.time
        except TypeError:
            self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
            result = story.get_pubdate() > self.time
            
        return result
        


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, Trig):
        self.Trig = Trig

    def evaluate(self, story):
        return not self.Trig.evaluate(story)
    
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, Trig1, Trig2):
        self.Trig1 = Trig1
        self.Trig2 = Trig2

    def evaluate(self, story):
        return self.Trig1.evaluate(story) and self.Trig2.evaluate(story)

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []
    for story in stories:
        if any([T.evaluate(story) for T in triggerlist]):
            filtered_stories.append(story) 
    
    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    t_map = {"TITLE": TitleTrigger,
            "DESCRIPTION": DescriptionTrigger,
            "AFTER": AfterTrigger,
            "BEFORE": BeforeTrigger,
            "NOT": NotTrigger,
            "AND": AndTrigger,
            "OR": OrTrigger
            }

    trigger_dict = {}
    trigger_list = [] 

    def line_reader(line):
        data = line.split(',')
        if data[0] != "ADD":
            if data[1] == "OR" or data[1] == "AND":
                trigger_dict[data[0]] = t_map[data[1]](trigger_dict[data[2]],
                        trigger_dict[data[3]])
            else:
                trigger_dict[data[0]] = t_map[data[1]](data[2])
        else: 
            trigger_list[:] += [trigger_dict[t] for t in data[1:]]

    for line in lines:
        line_reader(line)
    
    return trigger_list



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

