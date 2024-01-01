#!/usr/bin/python3

import random, time, sys, csv, re, os, ezgmail

exercises = {
    "abs": 
        ["Abs bike", "Alternating heel touches", "Bicycle crunch", "Bird dog", "Cable crunch", 
        "Cable wood chop", "Cocoon crunch", "Crab reach", "Cross-body mountain climber", 
        "Crunches", "Dead bug", "Dumbell halo to oblique crunch", "Dumbell side bend", 
        "Dumbell v-sit cross jab", "Elbow to knee crunch", "Elevated plank", "Elevated plank w/ mountain climber",
        "Extended plank", "Handle band crunch", "High butt bear crawl", "High plank arm reach",
        "Hip lift march", "Jackknife sit-up", "Dumbell sit up and press", "Raised dumbell toe touches", 
        "Lying knee raises", "Kneeling cable wood chop", "L-sit", "Dumbell core rotation", "Leg pull-in", 
        "Leg raises", "Plank cable row", "Plank cable side row", "Russian twists", "Mini-cable around the world plank", 
        "Oblique crunch", "Open book stretch", "Opposing leg toe touch", "Plank", "Plank body saw", 
        "Plank hip dip", "Plank jack", "Plank jack on elbows", "Plank shoulder taps", "Plank jack", 
        "Quad plank with leg extensions", "Reverse crunch", "Reverse plank", "Reverse plank on elbows", 
        "Scissor cross-over kick", "Scissor kicks", "Sit-up", "Stance jack", "Standing elbow to knee crunch", 
        "Standing oblique crunch", "Tuck crunch", "Up dog", "V-sit", "V-ups", "Windmill", "Windshield-wiper"],
    
    "back": 
        ["Cable v-fly", "Bench T-Spine Stretch", "Bird dog rows", "Cable cossover lat pulldown", "Cable row", 
        "Dumbell bent over reverese fly", "Dumbell bent over row", "Dumbell row", "Gorilla rows", 
        "Handle band bent over row", "Handle band lat pulldown", "Hand band rear deltoid fly", 
        "Handle band row", "Handle band straight arm pulldown", "Landmine row", "Loop band shoulder squeeze", 
        "Prone arm raises", "Prone side arm raises", "Prone wing arm raises", "Prone Y arm raises", 
        "Plank dumbell raises", "Cable lay-back pull ups", "Floor to shoulder cable pulls"],
    
    "biceps": 
        ["Half-way curls", "Behind the back bicep curl", "Bicep curl to shoulder press", "Cable bicep curl", 
        "Cable side bicep curls", "Cable preacher curl", "Floor to throat double curls", 
        "Concentration curl", "Cross-body curls", "Dumbell bicep curls", "Dumbell drag curls", 
        "Dumbell drag pause curl", "Dumbell cross-body curls with pause", "Dumbell bicep curls with pause" , 
        "Dumbell no money curls", "Dumbell hammer curls", "Dumbell hammer curls with press", "Dumbell wide curls", 
        "Hand band bicep curl", "Incline dumbell curl", "Incline hammer curls", "Bicep curl hold", 
        "Overhead cable bicep curl", "Zottman Curl", "Push up"], 
    
    "chest": 
        ["Alternating dumbell bench press", "Around benched the worlds", "Cable chest press", "Cable crossover fly", 
        "Chest doorway stretch", "Crab pose", "Decline push up", "Dumbell fly", "Dumbell incline bench press", 
        "Dumbell incline fly", "Dumbell pull over", "Dumbell squeeze press", "Shoulder to floor cable chest press", 
        "Incline cable chest press", "Chest push up", "Floor to shoulder incline chest press", 
        "Low cable chest fly", "Single arm cable crossover"],
    
    "glutes": 
        ["Stair drops", "Cable leg pull extensions", "Dumbell glute bridge", "Dumbell hip thrust", 
        "Elevated hip bridge", "Hip thrust", "Frog pump", "Dumbell crotch to press swings", 
        "Knee ups", "Loop band glute kickback", "Loop band side step", "Standing leg flys", 
        "Mini-band standing leg flys", "Pigeon pose", "Prone flutter kicks", "Seated figure four", 
        "Side leg hip circle", "Side leg kick", "Single leg glute bridge", "Single leg hip thrust", 
        "Single leg kickback", "Stair steps", "Standing leg side circle", "Standing side leg hold"],
    
    "hamstrings": 
        ["Airplane", "Alternating single arm dumbell swing", "Bear crawl", "Stair jumps", 
        "Cable row with squat", "Crossover standing forward bend", "Double dumbell snatch", 
        "Downward dog", "Dumbell clean", "Dumbell romanian deadlift", "Dumbell deadlift to bent over row", 
        "Dumbell deadlift to calf raise", "Dumbell deadlift to high pull", "Dumbell deadlift to shrug", 
        "Dumbell stiff legged deadlift", "Inchworm", "Lunges", "Glute bridge", "Glute thrust", 
        "Pancake", "Reverse bear crawl", "Seated forward bend", "Single leg dumbell deadlift", "Standing splits", 
        "Tuck jump", "Walking front kicks"],  
    
    "lower back": 
        ["Alternating superman", "Australian crawl", "Bridge", "Cat cow poses", "Child's pose",
        "Dumbell superman", "Wide superman cross leg-overs", "Seated twist", "Superman", "Superman hold", 
        "Supine back stretch"], 
    
    "shoulders": 
        ["Arnold dumbell press", "Backward arm circles", "Behind the back lateral raises", "Cable face pull", 
        "Cable front raise", "Cable lateral raise", "Cable shoulder external rotation", 
        "Cable external shoulder rotation at 90deg", "Cable shoulder internal rotation", 
        "Cable shoulder interal rotation at 90deg", "Dumbell cuban shoulder rotations", "Dumbell front raise", 
        "Dumbell hanging lateral raise", "Dumbell shoulder raise", "Dumbell lateral raise to front raise", 
        "Dumbell punches", "Dumbell rear delt raise", "Dumbell single arm shoulder press", 
        "Dumbell shoulder press", "Dumbell shoulder raise", "Dumbell standing front press", 
        "Dumbell standing single front arm press", "Dumbell underhand front raise", "Elbows out bent over dumbell row", 
        "Forward arm circle", "Handle band forward raise", "Handle band lateral raise", "Handle band shoulder press", 
        "Handle band upright row", "Iron Cross", "Mini loop band alternating lateral shoulder raise", 
        "Mini loop band lateral shoulder raise", "Mini loop band overhead fly", "Mini loop band reverse fly", 
        "Mini loop band scapular retraction", "Seated dumbell front press", "Seated dumbell rear delt raise", 
        "Seated single arm dumbell front press", "Side laterals to front raise", "Single arm overhead press", 
        "Standng arnold press", "Standing dumbell shoulder press", "Standing single arm dumbell shoulder press", 
        "Underhand rear delt raise"],  
    
    "triceps": 
        ["Bench dip", "Cable one arm tricep side extension", "Cable one arm underhand tricep extension", 
        "Cable overhead tricep extension", "Cable rope tricep extension", "Cable tricep pushdown", 
        "Cable underhand tricep pushdown", "Cobra tricep extension", "Diamond push up", "Dumbell kickbacks", 
        "Dumbell skullcrusher", "Dumbell tricep extension", "Handle band tricep extension", 
        "Incline dumbell skullcrusher", "Lateral cable tricep extension", "Loop band single arm tricep extension", 
        "Loop band standing tricep extension", "Mini loop band tricep press", "Seated tricep press", 
        "Single arm dumbell tricep extension", "Single arm high cable tricep extension", 
        "Standing dumbell tricep extension", "Tate press"], 
    
    "quads": 
        ["Stair jumps", "Air squats", "Alternating lunge jumps", "Banded leg drive", "Stair shuffle", 
        "Bulgarian split jumps", "Burpee", "Butt kicks", "Butt scoot", "Curtsy lunge", "Deficit reverse lunge", 
        "Double dumbell power snatch", "Duck walk", "Dumbell bulgarian split jumps", "Dunbell bulgarian split squat", 
        "Dumbell curtsy lunge", "Dumbell deficit reverse lunge", "Dumbell goblet squat", "Dumbell hand power clean", 
        "Dumbell kneel to stand", "Dumbell lunge", "Dumbell overhead kneel to stand", "Dumbell squat", 
        "Dumbell squat to shoulder press", "Dumbell step up", "Dumbell sumo squat", "Dumbell thruster", "Dumbell walking lunge", 
        "Handle band squat", "Hand band squat to press", "High depth jump", "Jump squat", "Kneel to stand", 
        "Lateral stair shuffle", "Lateral stair shuffle with knee drive", "Hand band deadlift", "Lunge", "Lunge jump", 
        "lunge twist", "Lunge with ankle grab", "Mini loop band alternating leg raises", "Mini loop band hip flexor", 
        "Mini loop band lunge", "Mini loop band standing hip flexion", "Mountain climber", "Overhead dumbell lunge", 
        "Pause squat", "Pistol squat", "Pulse lunge", "Reverse lunge", "Side lunge", "Single arm overhead dumbell lunge", 
        "Single arm overhead dumbell squat", "Wall sit"],       
}

def workoutchoice():
    abschoice = random.choice(exercises["abs"])
    absSelection = 'Abs, ' + abschoice

    backchoice = random.choice(exercises["back"])
    backSelection = 'Back, ' + backchoice

    bicepschoice = random.choice(exercises["biceps"])
    bicepsSelection = 'Biceps, ' + bicepschoice

    chestchoice = random.choice(exercises["chest"])
    chestSelection = 'Chest, ' + chestchoice

    gluteschoice = random.choice(exercises["glutes"])
    glutesSelection = 'Glutes, ' + gluteschoice

    hamstringschoice = random.choice(exercises["hamstrings"])
    hamstringsSelection = 'Hamstrings, ' + hamstringschoice

    lowbackchoice = random.choice(exercises["lower back"])
    lowbackSelection = 'Lower Back, ' + lowbackchoice

    shoulderschoice = random.choice(exercises["shoulders"])
    shouldersSelection = 'Shoulders, ' + shoulderschoice

    tricepschoice = random.choice(exercises["triceps"])
    tricepsSelection = 'Triceps, ' + tricepschoice

    quadschoice = random.choice(exercises["quads"])
    quadsSelection = 'Quads, ' + quadschoice

    global finalChoice
    finalChoice = str(str(absSelection) + '\n' 
                    + str(backSelection) + '\n' 
                    + str(bicepsSelection) + '\n' 
                    + str(chestSelection) + '\n'
                    + str(glutesSelection) + '\n'
                    + str(hamstringsSelection) + '\n'
                    + str(lowbackSelection) + '\n'
                    + str(shouldersSelection) + '\n'
                    + str(tricepsSelection) + '\n'
                    + str(quadsSelection))

    save()

def save():
        with open('FitJoe.csv', 'r') as FitJoe_File:
            FitJoe_Reader = csv.reader(FitJoe_File)
            for line in FitJoe_Reader:
                line
        while True:
            if str(finalChoice) == str(line[1]):
                workoutchoice()
            elif str(finalChoice) != str(line[1]):
                FitJoeFile = open(r'C:\Users\User\Documents\Coding Projects\Completed Apps\FitJoe\FitJoe.csv', 'r')
                FitJoeFile = open(r'C:\Users\User\Documents\Coding Projects\Completed Apps\FitJoe\FitJoe.csv', 'w')
                FitJoeFile.write(str(finalChoice))
                FitJoeFile.close()
                print('Your workout schedule has been saved to the "FitJoe" file. And sent to josephgrant666@gmail.com')
                time.sleep(2)
                ezgmail.send('josephgrant666@gmail.com','Today: FitJoe Workout Plan','Find todays workout attached',['FitJoe.csv'])
                sys.exit()

workoutchoice()
