import json
import re

from mrjob.job import MRJob
from mrjob.step import MRStep


class ContadorPalavras(MRJob):
    def mapper(self, chave, valor):
        avaliacao = json.loads(valor)
        avaliacao_texto = avaliacao['reviewText']

        tokens = re.findall(r'\b\w+\b', avaliacao_texto.lower())

        for token in tokens:
            yield token, 1

    def combiner(self, chave, valor):
        yield chave, sum(valor)

    def reducer(self, chave, valor):
        yield None, (sum(valor), chave)

    def reducer_final(self, chave, valor):
        for contagem, chave in sorted(valor):
            yield contagem, chave

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                combiner=self.combiner,
                reducer=self.reducer
            ),
            MRStep(
                reducer=self.reducer_final
            )
        ]


if __name__ == '__main__':
    ContadorPalavras.run()
