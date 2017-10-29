import csv
import pickle


myfile = '/Users/omardiab/Documents/University/atc-20121114.csv'
# Remember to close data after opening it

def Get_Trajectory(file, Person_ID):
	data = open(file)
	reader = csv.reader(data)
	xpos = []
	ypos = []
	for row in reader:
		if Person_ID in row:
			xpos.append(float(row[2]) / 100.0)
			ypos.append(float(row[3]) / 100.0)
	return [xpos, ypos]

def Get_Pedestrian_IDs(file):
	data = open(file)
	reader = csv.reader(data)
	Pedestrian_IDs = []
	for row in reader:
		if row[1] not in Pedestrian_IDs:
			Pedestrian_IDs.append(row[1])
	print ("This Dataset contains {} unique pedestrians".format(len(Pedestrian_IDs)))
	return Pedestrian_IDs

Pedestrian_IDs = Get_Pedestrian_IDs(myfile)


# Generate Dictionary Entries for first 15 Pedestrian IDs
# Use Pickle to save the really large Dictionary and load back into memory
def Generate_Tracjectories():
	Trajectory_Dict = {}
	c = 0
	for i in Pedestrian_IDs:
		Trajectory_Dict[i] = Get_Trajectory(myfile, i)
		c += 1
		print(c)
	return Trajectory_Dict

# My_Trajectory_Dict = Generate_Tracjectories()
# pickle_out = open("mydict.pickle", "wb")
# pickle.dump(My_Trajectory_Dict, pickle_out)
# pickle_out.close()

pickle_in = open("mydict.pickle", "rb")
My_Trajectory_Dict = pickle.load(pickle_in)
# print (len(My_Trajectory_Dict.keys()))



