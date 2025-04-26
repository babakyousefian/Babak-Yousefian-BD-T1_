from mrjob.job import MRJob

class MRMatrixTranspose(MRJob):

    def mapper(self, _, line):
        parts = line.strip().split(',')
        if len(parts) == 4:
            matrix_id, row, col, value = parts
            yield (matrix_id, col, row), value

    def reducer(self, key, values):
        for value in values:
            matrix_id, col, row = key
            yield matrix_id, (col, row, value)

if __name__ == '__main__':
    MRMatrixTranspose.run()
