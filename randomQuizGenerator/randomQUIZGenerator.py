import random


#Random DATA from Source Tutorial#
capitals = {
   'Alabama': 'Montgomery',
   'Alaska': 'Juneau',
   'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock',
   'California': 'Sacramento',
   'Colorado': 'Denver',
   'Connecticut': 'Hartford',
   'Delaware': 'Dover',
   'Florida': 'Tallahassee',
   'Georgia': 'Atlanta',
   'Hawaii': 'Honolulu',
   'Idaho': 'Boise',
   'Illinois': 'Springfield',
   'Indiana': 'Indianapolis',
   'Iowa': 'Des Moines',
   'Kansas':'Topeka',
   'Kentucky': 'Frankfort',
   'Louisiana': 'Baton Rouge',
   'Maine': 'Augusta',
   'Maryland': 'Annapolis',
   'Massachusetts': 'Boston',
   'Michigan': 'Lansing',
   'Minnesota': 'Saint Paul',
   'Mississippi': 'Jackson',
   'Missouri': 'Jefferson City',
   'Montana': 'Helena',
   'Nebraska': 'Lincoln',
   'Nevada': 'Carson City',
   'New Hampshire': 'Concord',
   'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
   'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
   'Ohio': 'Columbus',
   'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
   'Pennsylvania': 'Harrisburg',
   'Rhode Island': 'Providence',
   'South Carolina': 'Columbia',
   'South Dakota': 'Pierre',
   'Tennessee': 'Nashville',
   'Texas': 'Austin',
   'Utah': 'Salt Lake City',
   'Vermont': 'Montpelier',
   'Virginia': 'Richmond',
   'Washington': 'Olympia',
   'West Virginia': 'Charleston',
   'Wisconsin': 'Madison',
   'Wyoming': 'Cheyenne'}


for randomQuiz in range(35):
   quizFile = open('Questions\\Question no- %s.txt ' % (randomQuiz + 1), 'w')
   answerFile = open("Answers\\Answer no- %s.txt " % (randomQuiz + 1) , "w" )

########## HEADER CONFIG #############
   quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
   quizFile.write((' ' * 25) + 'State Capitals Quiz (Form %s)' % (randomQuiz + 1))
   quizFile.write("\n\n")

   states = list(capitals.keys())
   random.shuffle(states)

   for questionNum in range(50):
      correctAnswer = capitals[states[questionNum]]
      wrongAnswer = list(capitals.values())
      del wrongAnswer[wrongAnswer.index(correctAnswer)]
      wrongAnswer = random.sample(wrongAnswer, 3)
      
      answerOptions = [correctAnswer] + wrongAnswer
      random.shuffle(answerOptions)

      quizFile.write("%s. What is the capital of %s?\n" % (questionNum + 1, states[questionNum]))
      for i in range(4):
         quizFile.write('  %s. %s\n' % ("ABCD"[i] , answerOptions[i]))
      quizFile.write("\n")

      answerFile.write("%s.%s\n" % (questionNum + 1, "ABCD"[answerOptions.index(correctAnswer)]))

 


