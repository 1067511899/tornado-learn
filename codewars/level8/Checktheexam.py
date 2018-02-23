'''
The first input array contains the correct answers to an exam, like ["a", "a", "b", "d"]. The second one is "answers" array and contains student's answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty string).

If the score < 0, return 0.

For example:

checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
'''
def check_exam(arr1, arr2):
    result = 0
    le = len(arr1)
    for x in range(le):
        if arr2[x] == '':
            continue
        elif arr1[x] != arr2[x]:
            result -= 1
        else:
            result += 4
    if result <= 0:
        return 0
    return result
    
def check_exam1(arr1, arr2):
    score = sum(4 if a == arr1[i] else 0 if not a else -1 for i, a in enumerate(arr2))
    return 0 if score < 0 else score

if __name__ == '__main__':
    print(check_exam(["a", "a", "c", "b"], ["a", "a", "b", ""]))

