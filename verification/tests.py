"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3,4,5]],
            "answer": [0, 2, 0, 4, 0]
        },
        {
            "input": [[0, 0, 0]],
            "answer": [0, 0, 0]
        },
        {
            "input": [[]],
            "answer": []
        },
        {
            "input": [[1, 0, 2]],
            "answer": [0, 0, 0]
        }
    ],
    "Extra": [
        {
            "input": [[5, 5, 5]],
            "answer": [0, 5, 0]
        },
        {
            "input": [[1, 2, 3, 5, 6]],
            "answer": [0, 2, 0, 5, 0]
        }
    ]
}
