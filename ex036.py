#representando no código ANSI para cor cor em PYTHON: \033[CÓDIGODACORm]
#exemplo: \003[STYLEtextBACKm]
# \003[0;33;44m] == [sem estilo; nome33; fundo44m]
#style: 0(sem estilo), 1(negrito), 4(sublinhado), 7(negativo)
#text: 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(azul claro), 37(cinza)
#cor de fundo: 40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul), 45(roxo), 46(azul claro), 47(cinza)

print('\033[1;31;43mOlá, Mundo!\033[m')
