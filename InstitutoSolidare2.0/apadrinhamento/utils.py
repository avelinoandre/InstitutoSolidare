def calcular_compatibilidade(apadrinhado, padrinho):
    gostos_apadrinhado = [
        apadrinhado.area_escolar,
        apadrinhado.profissao_desejada,
        apadrinhado.hobby,
        apadrinhado.inspiracoes,
        apadrinhado.valores,
    ]

    gostos_padrinho = [
        padrinho.area_escolar,
        padrinho.profissao_desejada_quando_crianca,
        padrinho.hobby,
        padrinho.inspiracoes,
        padrinho.valores,
    ]

    total = 0
    iguais = 0

    for gosto_apad, gosto_pad in zip(gostos_apadrinhado, gostos_padrinho):
        if gosto_apad is not None and gosto_pad is not None:
            total += 1
            if gosto_apad == gosto_pad:
                iguais += 1

    if total == 0:
        return 0

    return round((iguais / total) * 100, 2)
