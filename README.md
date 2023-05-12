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

# Installation

pip install git+https://github.com/magjo67/deg.git

