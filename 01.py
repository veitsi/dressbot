from typing import List


class Question():
    def __init__(self, text: str, answers: List[str], parent=None):
        assert text
        assert len(answers) in [0, 2, 3, 4, 5]
        self.parent = parent  # type:Question
        self.text = text  # type:str
        self.answers = answers  # type:List[str]
        self.children = [None] * len(answers)  # type:List[Question]

    def ask_question(self) -> int:
        print(self.text)
        for i in range(len(self.answers)):
            print(str(i) + ": " + self.answers[i])
        while True:
            ans = int(input('--> '))  # type:int
            if ans >= 0 and ans < len(self.answers):
                break
        return ans

    def is_childfree(self) -> bool:
        return len(self.answers) == 0

    def is_lastchild(self) -> bool:
        return self.parent.children[len(self.parent.answers) - 1] == self


class Tree():
    def __init__(self, text: str, answers: List[str]):
        self.questions = [Question(text, answers)]  # type: List[Question]
        self.parent_index = 0
        self.parent_capacity = len(answers)
        self.layer_capacity = [1, len(answers), 0]  # type:List[int]
        self.layer_index = 1  # type:int
        self.child_index = 0  # type:int

    def add_child(self, text: str, answers: List[str]):
        self.questions.append(Question(text, answers))
        self.questions[self.parent_index].children[self.child_index] = Question(text, answers)
        self.layer_capacity[]

def start_interview(self):
    while True:
        ans = self.cursor.ask_question()
        print(ans)
        if self.cursor.children[ans].is_childfree():
            break
        break
    print(self.cursor.children[ans].question)


q00 = Question("Select your gender: ", ["male", "female"])
assert not q00.is_childfree()
q10 = Question("You adore Dart Vader suite, are not you?", [], q00)
assert q10.is_childfree()
tree = Tree(q00)
tree.add_child(q10)
assert not q10.is_lastchild()

print(tree)

# tree = {
#     'male': {
#         'party': "smoking",
#         'job': {},
#         'church': {}
#     },
#     'female': {}
# }
