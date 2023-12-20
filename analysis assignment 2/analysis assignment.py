import numpy as np

def highest_scoring_alignment(x, y, scoring_matrix):
    n = len(x)
    m = len(y)

    alignment_matrix = np.zeros((n + 1, m + 1))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match_score = alignment_matrix[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]
            gap_x_score = alignment_matrix[i - 1][j] + scoring_matrix[x[i - 1]]['-']
            gap_y_score = alignment_matrix[i][j - 1] + scoring_matrix['-'][y[j - 1]]

            alignment_matrix[i][j] = max(match_score, gap_x_score, gap_y_score)

    align_x, align_y = '', ''
    i, j = n, m

    while i > 0 or j > 0:
        current_score = alignment_matrix[i][j]
        diagonal_score = alignment_matrix[i - 1][j - 1] if i > 0 and j > 0 else float('-inf')
        up_score = alignment_matrix[i - 1][j] if i > 0 else float('-inf')
        left_score = alignment_matrix[i][j - 1] if j > 0 else float('-inf')

        if current_score == diagonal_score + scoring_matrix[x[i - 1]][y[j - 1]]:
            align_x = x[i - 1] + align_x
            align_y = y[j - 1] + align_y
            i -= 1
            j -= 1
        elif current_score == up_score + scoring_matrix[x[i - 1]]['-']:
            align_x = x[i - 1] + align_x
            align_y = '-' + align_y
            i -= 1
        else:
            align_x = '-' + align_x
            align_y = y[j - 1] + align_y
            j -= 1

    alignment_score = alignment_matrix[n][m]
    return align_x, align_y, alignment_score


a = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
b = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"
scoring_matrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': float('nan')}
}

result = highest_scoring_alignment(a, b, scoring_matrix)
print("The Alignment is :")
print("a:", result[0])
print("b:", result[1])
print("Alignment Score:", result[2])
