## deg
Program för att skapa degrecept.
Tänkt att köra från kommandoraden.

----

### Historia

Har ni någon gång varit med om att byta en mjölsort mot en annan och så blir resultatet en betongklump?
Syftet med programmet "deg" är att motverka detta beteende.

### Baker's percentage

I en del nyare recept så presenteras mängderna i procent i förhållande till mjölvikten.
Summan av mjölet är då 100%
Alla övriga ingredienser anges sedan som en procentsats i förhållande till summan av mjölet.
Även om detta är en bra metod för att dela med sig av ett recept så lider det utav samma betongproblem när man börjar byta ut ingredienser.
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
Ifall man inte vill använda ICA's mjöl som standard så finns parametern --goto som då blir den mjölsort som används för att fylla upp till 100%

## Exempel

Alla mjölegenskaper som är inmatade är tänkta för att man kalljäser över natten.
Så man rör ihop allt tills det ser jämnt fördelat ut.
Man behöver inte bearbeta degen länge i någon maskin.

Limpa för en 2 pound's form (rymmer 1.7 liter)

~~~
$ deg --vatten 385 --vete12 28 --rågsikt 25 --havregryn 15
Ingredienser            =    Vikt    Bagarprocent  Pris 
Vatten                  =  385 gram   74 Procent  0.01 kr
Salt                    =   12 gram    2 Procent  0.14 kr
Jäst                    =    5 gram    1 Procent  0.38 kr
ICA Havregryn           =   57 gram   11 Procent  0.85 kr
ICA Specialvetemjöl 12% =  150 gram   29 Procent  1.87 kr
ICA Rågsikt             =  135 gram   26 Procent  1.58 kr
ICA Vetemjöl 10%        =  181 gram   35 Procent  1.59 kr
Totalvikt               =  924 gram, mjöl 522 gram, pris 6.42 kr, total hydrering 0.737
~~~

Frallor med grovt rågmjöl

~~~
$ deg --vatten 500 --rågsikt 30 --råggrov 10
Ingredienser                =    Vikt    Bagarprocent  Pris 
Vatten                      =  500 gram   70 Procent  0.01 kr
Salt                        =   16 gram    2 Procent  0.19 kr
Jäst                        =    7 gram    1 Procent  0.51 kr
Kungsörnen Grovmalt rågmjöl =   62 gram    9 Procent  1.04 kr
ICA Rågsikt                 =  210 gram   29 Procent  2.47 kr
ICA Vetemjöl 10%            =  441 gram   62 Procent  3.86 kr
Totalvikt                   = 1237 gram, mjöl 714 gram, pris 8.08 kr, total hydrering 0.701
~~~

Baguetter

~~~
$ deg --vatten 400 --hyd 0.68 --vete12 41
Ingredienser            =    Vikt    Bagarprocent  Pris 
Vatten                  =  400 gram   70 Procent  0.01 kr
Salt                    =   13 gram    2 Procent  0.15 kr
Jäst                    =    6 gram    1 Procent  0.41 kr
ICA Specialvetemjöl 12% =  228 gram   40 Procent  2.84 kr
ICA Vetemjöl 10%        =  347 gram   60 Procent  3.04 kr
Totalvikt               =  993 gram, mjöl 575 gram, pris 6.45 kr, total hydrering 0.696
~~~

Pizzadeg till två pizzor
~~~
$ deg --vatten 250 --hyd 0.64 --goto vete13
Ingredienser      =    Vikt    Bagarprocent  Pris 
Vatten            =  250 gram   71 Procent  0.01 kr
Salt              =    8 gram    2 Procent  0.09 kr
Jäst              =    4 gram    1 Procent  0.25 kr
Finax TIPO 00 13% =  352 gram  100 Procent  5.45 kr
Totalvikt         =  613 gram, mjöl 352 gram, pris 5.81 kr, total hydrering 0.710
~~~

## Hjälp

deg -h skriver ut vilka mjölsorter som för ögonblicket finns i csv-filerna och vad de har för relativ hydrering samt pris

~~~
deg -h
usage: deg [-h] [--hydrering] [--goto] [--vatten] [--mjölk] [--grädde] [--olja] [--smör] [--ister] [--äggvita]
           [--ägg] [--surdeg] [--socker] [--vitsirap] [--sirap] [--honung] [--solros] [--lingon] [--gräddfil]
           [--drav] [--pmjöl] [--havrekli] [--kruska] [--vetekli] [--vetegrodd] [--rågmjöl] [--rågkross]
           [--vetekross] [--havregryn] [--graham] [--fullkung] [--bulgur] [--råggrov] [--4säd] [--fullspec]
           [--vete13] [--durum] [--caputo] [--rågsikt] [--kungsikt] [--pizza] [--vete12] [--cream] [--kungspec]
           [--lanapoletana] [--dinkel] [--ekospec] [--vete10] [--veteun] [--wapnö] [--vete95] [--jäst] [--salt]

Räkna ut mjölmängder.

options:
  -h, --help       show this help message and exit
  --hydrering      Hydrering 0.68
  --goto           Defaultmjöl = vete10
  --vatten         Vatten
  --mjölk          Mjölk
  --grädde         Grädde
  --olja           Matolja
  --smör           Smör eller margarin
  --ister          Ister
  --äggvita        Äggvita
  --ägg            Ägg
  --surdeg         Surdeg 100% hydrering
  --socker         Strösocker
  --vitsirap       Vit Sirap
  --sirap          Sirap
  --honung         Honung
  --solros         ICA Solroskärnor
  --lingon         Lingonsylt
  --gräddfil       Gräddfil
  --drav           Drav från ölbryggning
  --pmjöl          Potatismjöl
  --havrekli       Kungsörnen Havrekli, hydrering 2.5, 56.5kr/kg
  --kruska         Kungsörnen Kruskakli, hydrering 2.44, 24.29kr/kg
  --vetekli        Kungsörnen Vetekli, hydrering 2.4, 23.9kr/kg
  --vetegrodd      Risenta vetegroddar, hydrering 1.9, 75.9kr/kg
  --rågmjöl        Kungsörnen Fint rågmjöl, hydrering 1.6, 16.63kr/kg
  --rågkross       Kungsörnen rågkross, hydrering 1.53, 25.9kr/kg
  --vetekross      Kungsörnen vetekross, hydrering 1.5, 27.9kr/kg
  --havregryn      ICA Havregryn, hydrering 1.5, 15.0kr/kg
  --graham         ICA Finkornigt graham, hydrering 1.34, 14.95kr/kg
  --fullkung       Kungsörnen Graham, hydrering 1.25, 16.98kr/kg
  --bulgur         ICA Bulgur, hydrering 1.2, 33.0kr/kg
  --råggrov        Kungsörnen Grovmalt rågmjöl, hydrering 1.18, 16.63kr/kg
  --4säd           Lantbrödsmjöl 4 Sädesslag, hydrering 1.18, 13.25kr/kg
  --fullspec       Kungsörnen Vetemjöl Special Fullkorn, hydrering 1.12, 17.48kr/kg
  --vete13         Finax TIPO 00 13%, hydrering 1.11, 15.5kr/kg
  --durum          Kungsörnen Durumvete, hydrering 1.1, 31.5kr/kg
  --caputo         Caputo Pizzeria 00, hydrering 1.1, 32.0kr/kg
  --rågsikt        ICA Rågsikt, hydrering 1.1, 11.75kr/kg
  --kungsikt       Rågsikt Kungsörnen, hydrering 1.07, 12.48kr/kg
  --pizza          Kungsörnen Pizzamjöl, hydrering 1.07, 16.63kr/kg
  --vete12         ICA Specialvetemjöl 12%, hydrering 1.06, 12.475kr/kg
  --cream          Manitoba Cream, hydrering 1.05, 14.25kr/kg
  --kungspec       Kungsörnen Vetemjöl Special, hydrering 1.04, 16.0kr/kg
  --lanapoletana   LaNapoletana, hydrering 1.03, 30.0kr/kg
  --dinkel         ICA Ekologisk dinkel 11%, hydrering 1.03, 25.95kr/kg
  --ekospec        ICA Special EKO KRAV, hydrering 1.02, 13.475kr/kg
  --vete10         ICA Vetemjöl 10%, hydrering 1.0, 9.25kr/kg
  --veteun         United Gross 9.5%, hydrering 0.97, 15.98kr/kg
  --wapnö          Wapnö Vetemjöl siktat, hydrering 0.95, 16.0kr/kg
  --vete95         Finax Pâtisserie 9.5%, hydrering 0.95, 18.5kr/kg
  --jäst           Jäst, hydrering 0.0, 70.0kr/kg
  --salt           Salt, hydrering 0.0, 12.0kr/kg
~~~

# Installation

Installationen kräver Python3 (minimum 3.8) samt git

#### Ubuntu
~~~
sudo apt install python3-pip git
pip install git+https://github.com/magjo67/deg.git

Nyare Ubuntu ogillar att man installerar saker med pip för att inte bryta beroende mellan olika program.
Rekommendationen då är att installera i en virtuell environment.
Då fungerar:

sudo apt install pipx git
pipx install git+https://github.com/magjo67/deg.git
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
#### Lokal installation

Ifall man vill justera mjölsorter så är det enklare att först checka ut så man får ett lokalt repo.
~~~
git clone https://github.com/magjo67/deg.git
Information om mjölsorterna finns i filen ing_proc.csv som ligger i katalogen deg.
Efter att man justerat den så kan man låta pip installera från den katalogen man checkade ut.

pip install .
~~~
#### Uppgradering

pip install --upgrade deg

#### Avinstallation

pip uninstall deg

### Förbättringar

Jag mottar gärna förslag på fler mjölsorter eller andra ingredienser.
