# 2021-01-16
def program(linje):
	points = 0
	hours = 0
	egenlin = {}
	if linje == "a":
		lin = natur
	elif linje == "b":
		lin = sam
	else:
		print("du får nu skriva in alla dina kurser och deras poäng")
		while True:
			kurs = input("Vilken kurs läste du? \n Om du är klar skriv \"Done\" \n ")
			if kurs == "Done":
				break
			egenlin.update({kurs: int(input("Hur många poäng var den? \n"))})
		lin = egenlin
	for kurs in lin:
		points = points + betyg[str(input("Vad fick du för betyg i " + kurs + "?: "))] * lin[kurs]
		hours = hours + lin[kurs]
	print("du fick " + str(round(points/hours + float(input("hur mycket bonuspoäng fick du? \n")), 2)) + " meritpoäng")

betyg = {
	"A": 20,
	"a": 20,
	"B": 17.5,
	"b": 17.5,
	"C": 15,
	"c": 15,
	"D": 12.5,
	"d": 12.5,
	"E": 10,
	"e": 10,
	"F": 0,
	"f": 0
}

natur = {
	"Matte 1": 100,
	"Matte 2": 100,
	"Matte 3": 100,
	"Matte 4": 100,
	"Kemi 1": 100,
	"kemi 2": 100,
	"fysik 1": 150,
	"fysik 2": 100,
	"Idrott 1": 100,
	"Svenska 1": 100,
	"Svenska 2": 100,
	"Svenska 3": 100,
	"Engelska 5": 100,
	"Engelska 6": 100,
	"Moderna språk": 100,
	"Historia 1": 100,
	"Samhällskunskap 1": 100,
	"Religion 1": 50,
	"Biologi 1": 100,
	"Biologi 2": 100,
	"Valfri kurs 1": 100,
	"Valfri kurs 2": 100,
	"Valfri kurs 3": 100,
	"Valfri kurs 4": 100
}
sam = {
	"Engelska 5": 100,
	"Engelska 6": 100,
	"Historia 1b": 100,
	"Historia 2": 100,
	"Idrott och hälsa 1": 100,
	"Matte 1b": 100,
	"Matte 2b": 100,
	"Naturvetenskap 1b": 100,
	"Samhällskunskap 1b": 100,
	"Samhällskunskap 2": 100,
	"Samhällskunskap 3": 100,
	"Religion 1": 50,
	"Religion 2": 50,
	"Svenska 1": 100,
	"Svenska 2": 100,
	"Svenska 3": 100,
	"Geografi 1": 100,
	"Moderna språk 1": 100,
	"Moderna språk 2": 100,
	"Psykologi 1": 50,
	"Filosofi 1": 50,
	"Valfri kurs 1": 100,
	"Valfri kurs 2": 100,
	"Valfri kurs 3": 100,
	"Valfri kurs 4": 100

}
program(input("Vilken linje gå du på?\n a - Natur natur \n b - sam sam \n c - något annat \n"))
