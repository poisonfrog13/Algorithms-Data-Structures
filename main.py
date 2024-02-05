from algorithms.bubblesort import bubblesort, bubblesort_2
from tests.sort import test_cases

if __name__ == "__main__":
    for _inp, expected_output in test_cases:
        found_output = bubblesort_2(_inp)
        # print(
        #     f"This is expected output: {expected_output}\nThis is the result: {found_output}"
        # )
        print(expected_output == found_output)
        print()
