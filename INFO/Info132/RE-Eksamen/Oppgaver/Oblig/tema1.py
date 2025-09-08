# Tema 1
# Oppgave 1
print(f"******   *       *  ******   *******  *     *\n*     *  *       *  *     *  *        **    *\n*     *  *       *  *     *  *        * *   *\n******   *       *  ******   *****    *  *  *\n*    *   *       *  *     *  *        *   * *\n*     *   *     *   *     *  *        *    **\n*      *   *****    ******   *******  *     *")

# Oppgave 2
fornavn = "Ruben"
etternavn = "Nienhuis"

print(f"{fornavn} {etternavn}")
print(f"{etternavn}, {fornavn}")

# Oppgave 3
# a) og b)
def currencycalc():
    kroner = float(input("Antall kroner som skal gjøres om til Euro og Dollar: "))
    euro = kroner * 0.084
    dollar = kroner * 0.098

    print(f"{kroner:.0f} kroner tilsvarer {euro:.2f}\N{euro sign} og {dollar:.2f}\N{dollar sign}")

currencycalc()
