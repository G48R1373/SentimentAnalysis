#Librerie per Sentiment Analysis e Traduzione
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator, LANGUAGES
#Definizione degli oggetti
analyzer = SentimentIntensityAnalyzer()
translator = Translator()
#Intestazione
def starter():
	print("**********************")
	print("* Sentiment Analysis *")
	print("*  (Based on VADER)  *")
	print("**********************")
#Acquisizione del messaggio dal corrispettivo file di testo message.txt
def getMessage():
	f = open("message.txt", "r")
	message = ""
	for line in f.readlines():
		message += line
	f.close()
	return message
#Attraverso una funzione della classe SentimentIntensityAnalyzer analizzo il messaggio 
def analyze(message):
	scores = analyzer.polarity_scores(message)
	return scores
#Interpretazione dei risultati ottenuti secondo la documentazione della libreria vaderSentiment
def interpretation(x):
	if x > 0.05:
		return "Positività"
	elif x < -0.05:
		return "Negatività"
	else:
		return "Neutralità"
#Traduzione del messaggio dall'italiano all'inglese
def translate(message):
	return translator.translate(message, src = "it", dest = "en").text
#Output dei risultati ottenuti e del sentimento prevalente
def show(scores, sentiment):
	print("* Risultati *")
	print("*************")
	print("<Negatività: " + str(scores["neg"]) + "/1.0>")
	print("<Neutralità: " + str(scores["neu"]) + "/1.0>")
	print("<Positività: " + str(scores["pos"]) + "/1.0>")
	print("*******************************")
	print("* Legenda per il valore Media *")
	print("*    -1.0 <= Media <= 1.0     *")
	print("**************************************")
	print("* Media > 0.5 -> Positività          *")
	print("* Media < -0.5 -> Negatività         *")
	print("* -0.5 <= Media <= 0.5 -> Neutralità *")
	print("**************************************")
	print("<Media: " + str(scores["compound"]) + ">")
	print("*****************************************")
	print("*Sentimento prevalente: " + sentiment + "      *")
	print("*****************************************")
#Main
def main():
	starter()
	message = getMessage()
	message = translate(message)
	scores = analyze(message)
	sentiment = interpretation(scores["compound"])
	show(scores, sentiment)
#Esecuzione
if __name__ == "__main__":
	main()
