scores = [55, 72, 89, 90, 61, 47, 88]
formatted_scores = " ".join(str(x) for x in scores)
def passing_scores(mine):
    new_list = []
    for x in mine:
        if x >= 70:
            new_list.append(x)
    return new_list
new = passing_scores(scores)
formatted_new = " ".join(str(x) for x in new)
def average_passing(lst):
    total = 0
    for x in lst:
        total += x
    return total/len(lst)
average = average_passing(new)
print(f"All scores: {formatted_scores}")
print(f"Passing scores: {formatted_new}")
print(f"Average passing score: {average:.2f}")