'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''
import math

EARTH_GRAVITY = 9.81  # ? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62  # ? měsíční gravitace
SPEED_OF_LIGHT = 299792458  # ? m/s rychlost světla ve vakuu
SPEED_OF_SOUND = 343  # ? m/s rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.   
'''


def drop_time(a, s):
    return math.sqrt(2 * s * a) / a


def compare_drop_with_constant(a, s, constant, sentence, where):
    drop_t = drop_time(a, s)
    drop_at_top = (s / constant) + drop_t
    print(f'Object {where} will fall {s}m in {round(drop_t, 3)}s, drop will be {sentence} (at top) after'
          f' {round(drop_at_top, 3)}s, there is {s / constant}s difference')
