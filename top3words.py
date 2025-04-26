from mrjob.job import MRJob
from mrjob.step import MRStep

class MRTop3WordsFiltered(MRJob):

    # Define stopwords (you can expand this list!)
    STOPWORDS = {
        'the', 'and', 'a', 'an', 'in', 'on', 'of', 'to', 'for', 'with', 'at', 'by', 'from',
        'after', 'is', 'it', 'this', 'that', 'these', 'those',
        'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
        'but', 'if', 'or', 'because', 'as', 'until', 'while', 'than', 'so', 'such', 'too', 'very',
        'can', 'will', 'just'
    }

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   reducer=self.reducer_count_words),
            MRStep(mapper=self.mapper_prepare_for_sort,
                   reducer=self.reducer_output_top3)
        ]

    def mapper_get_words(self, _, line):
        # Normalize: lowercase + remove punctuation
        for word in line.strip().lower().replace(',', '').replace('.', '').replace('"', '').split():
            if word and word not in self.STOPWORDS:
                yield word, 1

    def reducer_count_words(self, word, counts):
        yield word, sum(counts)

    def mapper_prepare_for_sort(self, word, count):
        yield None, (count, word)

    def reducer_output_top3(self, _, count_word_pairs):
        top3 = sorted(count_word_pairs, reverse=True)[:3]
        for count, word in top3:
            yield word, count

if __name__ == '__main__':
    MRTop3WordsFiltered.run()
