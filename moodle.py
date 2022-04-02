import requests
from pprint import pprint
import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
num = 50
page_num = -1
for x in range(num):
  page_num = page_num + 1
  cookies = {
      '__utmz': '149981482.1647630036.12.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
      '__utmc': '149981482',
      'MoodleSession': '180teguakvhhf3q0nf9r3umqov',
      'MOODLEID1_': '%2588%25A8%25BF%25E9%2596%255C%25D1%252F%253C%251D',
      '__utma': '149981482.1187086106.1647268433.1648835129.1648840073.18',
      '__utmt': '1',
      '__utmb': '149981482.4.10.1648840073',
  }
  headers = {
      'authority': 'moodle.gpb-berlin.de',
      'cache-control': 'max-age=0',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'referer': 'https://moodle.gpb-berlin.de/mod/quiz/attempt.php?attempt=152143&cmid=276889',
      'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
      # Requests sorts cookies= alphabetically
      # 'cookie': '__utmz=149981482.1647630036.12.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=149981482; MoodleSession=180teguakvhhf3q0nf9r3umqov; MOODLEID1_=%2588%25A8%25BF%25E9%2596%255C%25D1%252F%253C%251D; __utma=149981482.1187086106.1647268433.1648835129.1648840073.18; __utmt=1; __utmb=149981482.4.10.1648840073',
  }
  params = {
      'attempt': '152840',
      'cmid': '276815',
      'page' : page_num,
  }

  response = requests.get('https://moodle.gpb-berlin.de/mod/quiz/attempt.php', headers=headers, params=params, cookies=cookies)
  soup = BeautifulSoup(response.content, 'html.parser')
  #print(soup.prettify())

  Question_html = soup.find("div", class_="qtext").get_text()
  #Question_text = Question_html.get_text()
  print (Question_html)
  # print (params['page'])









  f = open('Ques.txt', 'r', encoding="utf-8", errors='ignore')
  line_num = 0
  Question = Question_html
  if Question == "Kreuzen Sie die korrekten Antworten bezüglich Digitalisierung von Audio-Signalen an":
    print("5\n6")
    option = input("Wie viele Antwortmöglichkeiten gibt es?:\n")
    if option == "5":
      print("Die richtigen Antworten sind: Abtastrate und Sampling-Rate ist das gleiche, Sampling-Tiefe bestimmt die Menge an Bit pro Abtastung")
    else:
      print("Die richtigen Antworten sind: Bei der Messung der Rohdaten von Sound Amplituden werden alle Kanäle einzeln gemessen, Um Sound zu messen und zu digitalisieren werden Tonhöhe und Lautstärke berücksichtigt, Die Sampling-Rate legt die Menge an Messungen pro Sekunde fest")
  elif Question == "Ordnen Sie korrekt zu":
    print("1. Display Port, DVI-I, VGA\n2.GPU\n3.Bildschirme\n4.Grafikkarte")
    option = input("Bitte wählen sie: (1, 2, 3, oder 4)")
    if option == "1":
      print("Die richtige Antwort ist: Display Port → unterstützt das reihenweise Verketten von Displays, DVI-I → unterstützt teilweise analoge Videosignale, VGA → unterstützt rein analoge Videosignale")
    elif option == "2":
      print("Die richtige Antwort ist: GPU ist nicht Teil einer Erweiterungskarte und nicht Teil des Prozessors → OnBoard, Im Allgemeinen leistungsstärkste Lösung → Grafikkarte, GPU ist Teil des Hauptprozessors → APU")
    elif option == "3":
      print("Die richtigen Antworten sind: Plasma Bildschirme arbeiten mit Gas, LED Bildschirme arbeiten mit LCD, CRT Bildschirme schießen mit Elektronen")
    elif option == "4":
      print("Die richtige Antwort ist: Verbund mehrerer Grafikkarten → SLI, Alter Grafikkarten-Bus → AGP, Grafikkarte Teil des Prozessors → APU")
  elif Question == "Markieren Sie die korrekten Antworten":
    print("1.CPU\n2.Audio")
    option = input("Bitte wählen sie: (1, oder 2)")
    if option == "1":
      print("Die richtigen Antworten sind: Der DAC wandelt digitale in analoge Daten, Der ADC wandelt analoge in digitale Daten")
    elif option == "2":
      print("Die richtigen Antworten sind: HD Audio ist der Nachfolger von AC'97, HD Audio und AC'97 sind Standards für eine Audioarchitektur von Intel")
  elif Question == "Wählen Sie die korrekten Aussagen:":
    print("1. Land / Pit\n2.Musik-CDs")
    option = input("Bitte wählen sie: (1, oder 2)")
    if option == "1":
      print("Die richtigen Antworten sind: Land ist hoch, Pit ist tief, Pit ist 0")
    elif option == "2":
      print("Die richtigen Antworten sind: Musik-CDs haben eine Abtastrate von 44,1 kHz, Musik-CDs haben eine Auflösung von 16 Bit, Die Auflösung bestimmt die Menge an Bit pro Abtastung")
  elif Question == "Welchem Zeichenfolge entspricht folgende Bytefolge (8 Bit/Byte)":
    print("1. 01100101011000110110100001101111\n2. 01110100011100100110100101101101")
    option = input("Bitte wählen sie: (1, oder 2)")
    if option == "1":
      print("Die richtige Antwort ist: echo")
    elif option == "2":
      print("Die richtige Antwort ist: trim")
  else:
    search_phrase = Question
    for line in f.readlines():
      line_num += 1
      if line.find(search_phrase) >= 0:
      #print(line_num)
        answer = line_num
    #print(answer)
    file = open('Ques.txt', encoding="utf-8", errors='ignore')
    all_lines = file.readlines()
    print(all_lines[answer])
    print("____________________________________________________")