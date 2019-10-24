from string import punctuation
import xlsxwriter

def main():
	#check = 0
	workbook = xlsxwriter.Workbook("twitterData.xlsx")
	worksheet = workbook.add_worksheet()
	worksheet.write(0, 0, 'Name')
	worksheet.write(0, 1, 'Tweets')
	x = 1
	#while check == 0:
	i = 0
	y = 1
	#WHAT IS BEING SENT TO PYTHON CLEANER??
	fileName = input("Enter file name: ") #change to something like sys.argv[1]
	personName = input("Enter person's name/handle: ") #going to axe this probably
	inputFile = open(fileName, 'r', errors='replace')
	splitFile = inputFile.read().split("\"")
	#if recieving text is a block::
	#new code is probably something like:
	#splitFile = sys.argv[1].split("\"")
	#if recieving text is line by line::
	#change splitfile to split line and edit the file to clean line by line
	#tweet = ""
	ignoretweet = False
	worksheet.write(x, 0, personName) #figure out a way to get persons name from twitter scraper.
	while i < len(splitFile):
		s = splitFile[i]
		if (s == "quote" and splitFile[i+1] == ":{") or (s == "isRetweet" and splitFile[i+1] == ":true,"):
			ignoretweet = True
		elif s == "time" and splitFile[i+1] == ":":  # we're right before a time block
			i += 2  # go to time block
			continue
		elif s == "text" and splitFile[i+1] == ":":  # we're right before the first word of a text block
			i += 2
			if splitFile[i] == "":  # there is no text
				i += 1
				continue
			if ignoretweet:
				ignoretweet = False
			else:
				worksheet.write(x, y, splitFile[i])
				y+=1
				#print(splitFile[i])
		i += 1
		#check = int(input("Continue? (Enter 0 to continue): "))
		#if check == 0:
		#	x += 1
		#else:
		#	check = 1
	workbook.close()

def extractTime(s):
	# hi
	s = s.split("T")
	return s[0]
	# bye


def extractFromTextBlock(s):
	s = s.split("\"")
	return s[len(s)-1]


def extractFromUserMentionsBlock(s):
	s = s.split("\"")
	return s[0]


main()
