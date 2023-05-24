## deg
Program för att skapa degrecept

----

### Historia

Har ni någon gång varit med om att byta en mjölsort mot en annan och så blir resultatet en betongklump?
Syftet med programmet "deg" är att motverka detta beteende.

### Baker's percentage

En del nyare recept så presenteras mängderna i procent i förhållande till mjölvikten.
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
Konfigfilerna är csv-filer som man kan lägga till fler ingredienser till.

Syftet med programmet är inte att visa vad som blir bra eller gott, utan ett verktyg som gör att man kan byta ut en mjölsort mot en annan och brödet kommer att få liknande egenskaper.

## Exempel

Alla mjölegenskaper som är inmatade är tänkta för att man kalljäser över natten.
Så man rör ihop allt tills det ser jämnt fördelat ur.
Man behöver inte bearbeta degen länge i någon maskin.

Limpa för en 2 pound's form (rymmer 1.7 liter)

deg --vatten 385 --hyd 0.68 --vete12 28 --rågsikt 25 --havregryn 15

Bullar med grovt rågmjöl

deg --hyd 0.68 --vatten 500 --rågsikt 30 --råggrov 10

Baguetter

deg --vatten 400 --hyd 0.68 --vete12 51.22

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

