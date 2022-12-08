def calculate_score(scores):
    score_list = []
    for idx, score in enumerate(scores, start=1):
        score_list.append((idx, score))

    score_list = sorted(score_list, key=lambda x: -x[1])[:5]

    answer_idx = list(map(str, sorted([idx[0] for idx in score_list])))
    answer_score = [score[1] for score in score_list]

    return sum(answer_score), " ".join(answer_idx)


if __name__ == "__main__":
    scores = []
    for _ in range(8):
        score = int(input())
        scores.append(score)

    answer = calculate_score(scores=scores)

    for ans in answer:
        print(ans)
