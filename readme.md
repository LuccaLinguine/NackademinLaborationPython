# Laboration 1

## LÄS DETTA FÖRST

**Betyg**: U, G. För att bli godkänd måste samtliga uppgifter besvaras, samt program_1 och program_2 ska implementeras. Fokusera på att LÄRA DIG, inte på att bli färdig fort.

## Inlämning

Inlämning görs på läroplattformen. Ni lägger in en länk till en google-drive-folder.
Dvs.
1. Skapa en folder i google drive
2. Högerklicka på den och tryck share/dela
3. Skriv in tobias@utvecklarakademin.se 
4. Kopiera länken och klistra in den på inlämningen.

Det ska sägas att jag föredrar att använda github classroom för att administrera inlämningsuppgifter, men eftersom kursen är mycket kort försöker jag ta bort så mycket komplexitet som möjligt, därav varför vi gör så här. Enklare att dela en google-drivelänk, än att ni ska klona ett repository, göra commits, etc).

## Regler

Laborationen är individuell, och du ska inte använda AI-assisterad hjälp för att lösa uppgiften, men däremot kan du nyttja AI för att få fler exempel, förklaringar, och helt enkelt för att maximera din inlärning. Att däremot skicka in en hel uppgift och be om en lösning är strikt förbjudet - detta hjälper dig inte träna på egen problemlösning, eftersom du deligerar tänkandet till någon annan. Jag märker väldigt enkelt när svar är AI-genererade, och jag märker generellt sätt om din kod inte matchar kunskapen jag upplever från dig på lektionstid. Vi utnyttjar mer AI för labb 2.

## Introduktion:

Du ska svara på frågorna. Tanken är att detta blir en lätt intro till pythons syntax, dvs. det formella (och tyvärr tråkiga).
När du svarar frågorna så uppmuntrar jag starkt till att fråga en chattbott om förklaringar - detta är en övning, ditt betyg är irrelevant, du kan max uppnå G.
Om du råkar vara kunnig inom python kan du avklara övningen på ca 30min.
När du gjort övningen föreslår jag att du försöker hitta något mindre projekt för inlärning, tex. via mina förslag här:
https://utvecklarakademin.notion.site/Project-ideas-ed2cb5530db54af3ba963c16e7a3981d?source=copy_link

Eller be en chattbot om enklare uppgifter / projekt att lösa.
Att lära sig python handlar om att börja greppa fundamentan:
- variables
- data types, int, string, booleans
- if-statements
- for-loops / looping
- lists, dictionaries
- functions
- error handling with if-statements and try-except
- classes & object oriented programming
- using and installing external packages with pip

Glöm aldrig: Programmering lär du dig endast genom att sätta dig ner, fokusera, och bara koda. Ingen lär sig att koda genom att läsa, eller bara genom att AI-prompta. Denna lilla övning kan anses vara mer av en uppvärmning.

## Beskrivning
Du kommer antingen behöva svara med text, kod eller båda samtidigt.
Du kan utnyttja kommentarer i python för att skriva text med # (hashtag-symbolen)
Eller så kan du skapa ett markdown-block och sedan skriva text.
För att sedan lägga till kod kan du skriva

\```python

Kod här inne

\```

# Exempelfråga & Exempelsvar:

Vad är en lista, och varför är den viktig? Svara med text och kod.

Svar:
Listor är användbara eftersom vi kan gruppera data på ett logiskt sätt. Utan listor hade vi behövt spara allt i enskilda variabler, vilket inte är skalbart för en applikation. Vad händer om vi exempelvis har 100000 studenter och alla behöver en variabel?

```python
# Idiotiskt:
student_1 = "Tobias"
student_2 = "Alfred"
student_3 = "Elina"
student_4 = "Jessica"

# Bra
students = ["Tobias", "Alfred", "Elina", "Jessica"]
student_1 = students[0]
```
