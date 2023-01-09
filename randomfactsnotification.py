import time as time
import random as rd
import plyer as pl

facts = [
    "Elephants are the only animals that can't jump",
    "Like fingerprints, everyone's tongue print is different",
    "The only food that doesn't spoil is Honey",
    "You can't kill yourself by holding your breath",
    "TYPEWRITER is the longest word that can be made using the letters only on one row on the keyboard",
    "People say, 'Bless You' when you sneeze because when you sneeze,your heart stops for a millisecond",
    "The longest muscle in the body is the tongue",
    "The most common name in the world is Mohammed",
    "Carbon monoxide can kill a person in less than 15 minutes",
    "The blood of mammals is red, the blood of insects is yellow in colour, and the blood of lobster is blue",
    "The hummingbird, the loon, the swift, the kingfisher, and the greb are all birds that cannot walk",
    "The fastest bird is the Peregrine falcon, clocked at speeds of up to 240 miles per hour",
    "Dragonflies are one of the fastest insects, flying 50 to 60 mph",
    "The electric chair was invented by a dentist",
    "A cat's tail contains nearly 10 percent of all the bones in its body",
    "Corn is grown on every continent except antarctica",
    "Hearing is the fastest human sense. a person can recognize a sound in as little as 0.05 seconds",
    "'Rhythm' is the longest English word without a vowel",
    "Human thigh bones are stronger than concrete",
    "Earth is the only planet not named after a god"
    ]

if __name__=="__main__" :
    while True:
        pl.notification.notify(
            title = "Do you know !!",
            message = rd.choice(facts),
            app_icon = None,
            timeout = 5
        )
        time.sleep(30)