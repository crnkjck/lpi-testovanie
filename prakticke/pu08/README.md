Cvičenie 8
==========

**Riešenie odovzdávajte podľa
[pokynov na konci tohoto zadania](#technické-detaily-riešenia)
do stredy 22.4. 23:59:59.**

Súbory potrebné pre toto cvičenie si môžete stiahnuť ako jeden zip
[`pu08.zip`](https://github.com/FMFI-UK-1-AIN-412/lpi/archive/pu08.zip).

SAT solver
----------------------

Naprogramujte SAT solver, ktorý zisťuje, či je
vstupná formula (v konjunktívnej normálnej forme) splniteľná.

Na prednáške ste videli základnú kostru metódy DPLL, ktorej hlavnou ideou je
propagácia klauzúl s iba jednou premennou (_jednotková klauzula_,
<i lang="en">unit clause</i>). Tá ale hovorí o veciach ako _vymazávanie
literálov_ z klauzúl a _vymazávanie klauzúl_, čo sú veci, ktoré nie je také
ľahké efektívne (či už časovo alebo pamäťovo) implementovať, hlavne ak počas
<i lang="en">backtrack</i>ovania treba zmazané literály resp. klauzuly správne
naspäť obnovovať.

Použite teda techniku _sledovaných literálov_ z [predchádzajúceho cvičenia](../pu07/)
na implementáciou DPLL solvera.

## Implementácia

Základná kostra DPLL je nasledujúca:

1.  [Inicializujeme sledované literály](../pu07/#inicializácia).
    Výsledkom tejto operácie je aj zoznam jednotkových klauzúl vo vstupe.
2.  Unit propagate: Kým je nejaká jednotková klauzula,
    [nastavíme](../pu07/#vplyv-nastavovania-literálov-na-sledovanie) jej
    posledný nenastavený literál na `true`. Toto samozrejme spôsobí presun
    niektorých sledovaných literálov a tiež môže pridať nové jednotkové
    klauzuly.
3.  Ak už nemáme žiadnu jednotkovú klauzulu, vyberieme si nejaký literál
    a postupne skúsime tento literál a potom jeho negáciu nastaviť na
    `true`, pričom zakaždým rekurzívne pokračujeme od kroku 2.
    Samozrejme potom zase všetky nastavené literály „odnastavíme".    
    **Pozor:** „Odnastavíme" aj literály, ktoré sme nastavili v rámci
    propagácie jednotkových klauzúl (viď [backtrackovanie](#backtrackovanie)
    nižšie).

Prehľadávanie môžeme ukončiť, ak nájdeme spĺňajúce ohodnotenie (t.j.
ohodnotíme všetky premenné a nenájdeme konflikt, teda nesplnenú klauzulu).

### Backtrackovanie

Na jednej „úrovni“ backtrackovania môže byť nastavených viacero literálov:
jeden keď zavoláme `setLiteral` a potom možno ďalšie v rámci propagácie
jednotkových klauzúl. Pri návrate ich treba všetky odnastaviť.
Najjednoduchšie sa to robí tak, že si na každej úrovni zapamätáme počet
už nastavených literálov a potom voláme `unsetLiteral` až kým sa nedostaneme
na rovnakú úroveň:

```
back = number of assigned literals
...
setLiteral
unit propagate
...
while (number of assigned literals > back)
    unsetLiteral
```

*Poznámka*: V knižnici [`Theory.java`](java/Theory.java) je metóda
[`int nAssigned()`](java/Theory.java#L343).

## Technické detaily riešenia

Riešenie odovzdajte do vetvy `pu08` v adresári `prakticke/pu08`.

Odovzdávajte súbory [`Theory.java`](java/Theory.java)
a [`SatSolver.java`](java/SatSolver.java).
Program [`SatSolverTest.java`](java/SatSolverTest.java)
musí korektne zbehnúť s vašou knižnicou.

Či ste správne vytvorili pull request si môžete overiť
v [tomto zozname PR pre pu08](https://github.com/pulls?utf8=%E2%9C%93&q=is%3Aopen+is%3Apr+user%3AFMFI-UK-1-AIN-412+base%3Apu08).

Odovzdávanie riešení v iných jazykoch konzultujte s cvičiacimi.
