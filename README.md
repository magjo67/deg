## deg
Program för att skapa degrecept

----

### Historia

Har ni någon gång varit med om att byta en mjölsort mot en annan och så blir resultatet en betongklump?
Syftet med programmet "deg" är att motverka detta beteende.

### Baker's percentage

I en del nyare recept så presenteras mängderna i procent i förhållande till mjölvikten.
Summan av mjölet är då 100%
Alla övriga ingredienser anges sedan som en procentsats i förhållande till summan av mjölet.
Även om detta är en bra metod för att dela med sig av ett recept så lider det utav samma betongproblem när man börja byta ut ingredienser.
Baker's percentage fungerar om man vill skala upp (eller ner) ett recept, inte om man vill ändra på det.

### Vattenprocent

Min lösning på det hela är att istället att vända på logiken.
Om man utgår från mängden vatten och talar om hur många procent utav respektive mjölsort man vill ha.
Detta kräver att man har någon form av tabell med olika mjölsorters uppsugningsförmåga.
Tabellen som jag gjort utgår ifrån ICA's standardmjöl.
Alla övriga mjölsorter är uttestade så att man utav programmet får en lika "kladdig" deg.
Konfigfilerna är csv-filer där man kan lägga till fler ingredienser.

Syftet med programmet är inte att visa vad som blir bra eller gott, utan ett verktyg som gör att man kan byta ut en mjölsort mot en annan och brödet kommer att få liknande egenskaper.

När det gäller olja och övriga "blöta" ingredienser så räknar jag som om de innehåller en viss mängd vatten.
Det har inget med faktisk vattenhalt att göra utan är knutet till hur "kladdig" degen blir utav den ingrediensen.

Grundidén är att när man hittat en hydrering till en viss typ av bröd, så kan man behålla den hydreringen och ändra alla andra ingredienser varpå den räknar fram hur mycket som behövs av respektive sort.
Om inte summan av mjöl blir 100% så fyller den på med ICA Standardmjöl.

## Exempel

Alla mjölegenskaper som är inmatade är tänkta för att man kalljäser över natten.
Så man rör ihop allt tills det ser jämnt fördelat ut.
Man behöver inte bearbeta degen länge i någon maskin.

Limpa för en 2 pound's form (rymmer 1.7 liter)

deg --vatten 385 --hyd 0.68 --vete12 28 --rågsikt 25 --havregryn 15

Bullar med grovt rågmjöl

deg --hyd 0.68 --vatten 500 --rågsikt 30 --råggrov 10

Baguetter

deg --vatten 400 --hyd 0.68 --vete12 51.22

Pizzadeg till fyra pizzor

deg --vatten 500 --vete12 100 --hyd 0.6

## Hjälp

deg -h skriver ut vilka mjölsorter som för ögonblicket finns i csv-filerna och vad de har för relativ hydrering samt pris

~~~
deg -h
usage: deg [-h] [--hydrering] [--vatten] [--mjölk] [--olja] [--smör] [--äggvita] [--ägg] [--surdeg] [--socker]
           [--vitsirap] [--havrekli] [--kruska] [--vetekli] [--vetegrodd] [--havregryn] [--rågmjöl] [--rågkross]
           [--graham] [--fullkorn] [--råggrov] [--rågsikt] [--fullspec] [--fullkung] [--vete13] [--vete12]
           [--dinkel] [--vete10] [--veteun] [--jäst] [--salt]

Räkna ut mjölmängder.

options:
  -h, --help    show this help message and exit
  --hydrering   Hydrering 0.7
  --vatten      Vatten
  --mjölk       Mjölk
  --olja        Matolja
  --smör        Smör eller margarin
  --äggvita     Äggvita
  --ägg         Ägg
  --surdeg      Surdeg 100% hydrering
  --socker      Strösocker
  --vitsirap    Vit Sirap
  --havrekli    Kungsörnen Havrekli, hydrering 2.5, 17.0kr/kg
  --kruska      Kungsörnen Kruskakli, hydrering 2.44, 17.0kr/kg
  --vetekli     Kungsörnen Vetekli, hydrering 2.4, 17.0kr/kg
  --vetegrodd   Risenta vetegroddar, hydrering 2.1111, 30.0kr/kg
  --havregryn   ICA Havregryn, hydrering 1.75, 12.0kr/kg
  --rågmjöl     Kungsörnen Fint rågmjöl, hydrering 1.6, 13.0kr/kg
  --rågkross    Kungsörnen rågkross, hydrering 1.53, 16.0kr/kg
  --graham      ICA Finkornigt graham, hydrering 1.34, 15.0kr/kg
  --fullkorn    ICA fullkorn gramhamsmjöl, hydrering 1.25, 15.0kr/kg
  --råggrov     Kungsörnen Grovmalt rågmjöl, hydrering 1.18, 14.0kr/kg
  --rågsikt     ICA Rågsikt, hydrering 1.14, 12.0kr/kg
  --fullspec    Kungsörnen Vetemjöl Special Fullkorn, hydrering 1.12, 18.5kr/kg
  --fullkung    Kungsörnen Vetemjöl Fullkorn, hydrering 1.1, 16.0kr/kg
  --vete13      Finax TIPO 00 13%, hydrering 1.09, 15.5kr/kg
  --vete12      ICA Specialvetemjöl 12%, hydrering 1.05, 13.25kr/kg
  --dinkel      ICA Ekologisk dinkel 11%, hydrering 1.03, 32.0kr/kg
  --vete10      ICA Vetemjöl 10%, hydrering 1.0, 8.3kr/kg
  --veteun      United Gross 9.5%, hydrering 0.97, 14.0kr/kg
  --jäst        Jäst, hydrering 0.0, 64.0kr/kg
  --salt        Salt, hydrering 0.0, 16.0kr/kg
~~~

# Installation

Installationen kräver Python3 samt git

#### Ubuntu
~~~
sudo apt install python3-pip git
pip install git+https://github.com/magjo67/deg.git
~~~
#### Fedora
~~~
sudo yum install python3-pip git
pip install git+https://github.com/magjo67/deg.git
~~~
#### OpenSUSE
~~~
sudo zypper install python3-pip git
pip install git+https://github.com/magjo67/deg.git
~~~
#### Windows
Kräver att git och python är installerad innan.
Använd tex Chocolatey för att göra installationen.

Följ då https://chocolatey.org/install

~~~
Från powershell med adminrättigheter
choco install python --pre 
choco install git

Från en vanlig powershell
pip install git+https://github.com/magjo67/deg.git
~~~

#### Mac
Detta är inte testat då jag inte har någon Mac att testa på.

Många väljer att installera via Homebrew, så om Python3 och git saknas så kan det vara en variant:

~~~
Installera homebrew (från https://brew.sh/ )
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew update && brew upgrade
brew install python3 git

pip install git+https://github.com/magjo67/deg.git
~~~
#### Uppgradering

pip install --upgrade deg

### Förbättringar

Jag mottar gärna förslag på fler mjölsorter eller andra ingredienser.
