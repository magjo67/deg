import deg
import os
import argparse
import pandas as pd
class Ingredienser:
    def __init__(self, kort, long, vikt, pris):
        self.kort = kort
        self.long = long
        self.vikt = vikt
        self.pris = pris


def do_deg():
    ing_vikt_csv = deg.__path__[0] + '/ing_vikt.csv'
    ing_proc_csv = deg.__path__[0] + '/ing_proc.csv'

    ing_vikt = pd.read_csv(ing_vikt_csv, index_col='kort')
    ing_proc = pd.read_csv(ing_proc_csv, index_col='kort')
    ing_proc.sort_values(by='hydrering', inplace=True, ascending=False)

    parser = argparse.ArgumentParser(description='Räkna ut mjölmängder.')
    # Argument för konfig
    parser.add_argument(
            '--hydrering', default=0.68, type=float, metavar='', help="Hydrering 0.68")
    parser.add_argument(
            '--goto', default='vete10', metavar='', help="Defaultmjöl = vete10")
    # Lista av ickeingredienser
    skiplist = [ 'hydrering', 'goto' ]
    # Argument för fasta vikter
    for kort in ing_vikt.index:
        long = ing_vikt.long[kort].replace("%", "%%")
        parser.add_argument(
            "--"+kort, default=ing_vikt.default[kort], type=float, metavar='', help=long)
    # Argument för procentuella
    for kort in ing_proc.index:
        long = ing_proc.long[kort].replace("%", "%%") + ", hydrering " + str(
            ing_proc.hydrering[kort]) + ", "+str(ing_proc.pris[kort]) + "kr/kg"
        parser.add_argument(
            "--"+kort, default=ing_proc.default[kort], type=float, metavar='', help=long)
    args = parser.parse_args()
    vatten = args.vatten
    hydrering = args.hydrering
    goto = args.goto
    vtot = 0
    mtot = 0
    proctot = 0
    bill = []
    textlen = 0
    # Räkna fram mängd vatten
    for kort, vikt in vars(args).items():
        if kort in skiplist:
            continue
        if vikt > 0:
            try:
                vvikt = vikt * ing_vikt.fukt[kort]
                vtot += vvikt
                mvikt = vikt * ing_vikt.mjöl[kort]
                mtot += mvikt
                rad = Ingredienser(kort, ing_vikt.long[kort], vikt, vikt * ing_vikt.pris[kort])
                bill.append(rad)
                textlen = max(textlen,len(ing_vikt.long[kort]))
            except KeyError as e:
                None
    proctot=(mtot/vtot*100*hydrering)
    # Räkna fram mjölmängder
    for kort, procent in vars(args).items():
        if kort in skiplist:
            continue
        try:
            lhyd = ing_proc.hydrering[kort]
        except KeyError as e:
            lhyd = 0
        if procent > 0 and lhyd > 0:
            mvikt = vtot * procent / hydrering / ing_proc.hydrering[kort] / 100
            mtot += mvikt
            proctot += procent
            rad = Ingredienser(kort, ing_proc.long[kort], mvikt, mvikt * ing_proc.pris[kort])
            bill.append(rad)
            textlen = max(textlen,len(ing_proc.long[kort]))

    if proctot < 100:
        vete = vtot * (100 - proctot) / hydrering / ing_proc.hydrering[goto] / 100
        mtot += vete
        bill.append(Ingredienser(goto, ing_proc.long[goto], vete, vete * ing_proc.pris[goto]))
        textlen = max(textlen, len(ing_proc.long[goto]))
    if round(proctot,1) > 100:
        print(round(proctot,1), " är för många procent")
        exit()
    salt = (mtot + vtot) * args.salt / 100
    bill.insert(1, Ingredienser("salt", ing_proc.long["salt"], salt, salt * ing_proc.pris["salt"]))
    yeast = (mtot + vtot) * args.jäst / 100
    bill.insert(2, Ingredienser("jäst", ing_proc.long["jäst"], yeast, yeast * ing_proc.pris["jäst"]))

    print(f"{'Ingredienser':<{textlen + 1}}=    {'Vikt':<4}    {'Bagarprocent':<5}  {'Pris':<5}")
    pristot = 0
    vikttot = 0
    for rad in bill:
        pristot += rad.pris
        vikttot += rad.vikt
        print(f"{rad.long:<{textlen + 1}}={rad.vikt:5.0f} gram {rad.vikt/mtot*100:4.0f} Procent {rad.pris/1000:5.2f} kr")
    print(f"{'Totalvikt':<{textlen + 1}}={vikttot:5.0f} gram, mjöl {mtot:.0f} gram, pris {pristot/1000:.2f} kr, total hydrering {vtot/mtot:.3f}")
    print("")
