#Inference Engine
def Rec_Search(Topics,Theory,Knowledge_Base):
	Areas = []
	Condition = 0
	for item in Topics:
		for thing in Knowledge_Base:
			if item in thing:
				foo = thing[1]
				if foo == Theory:
					Condition = 1
				if foo != item:
					Areas.append(foo)
	return Areas, Condition

def Feed_Forward_Search(Subject,Theory,Knowledge_Base):
	Topics = []
	KB_Size = len(Knowledge_Base)
	Condition = 0
	Counter = 0

	for item in Knowledge_Base:
		if Subject in item:
			thing = item[1]
			Topics.append(thing)
			if thing == Theory:
				Condition = 1


	while (Condition != 1) and (Counter != KB_Size):
		Topics, Condition = Rec_Search(Topics,Theory, Knowledge_Base)
		Counter = Counter + 1

	if Condition == 1:
		print Subject ,"=", Theory	
	elif Condition == 0:
		print Subject ,"!=", Theory	