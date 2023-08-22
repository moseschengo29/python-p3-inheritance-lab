#!/usr/bin/env python

import random
from user import User  

all_knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        if knowledge is None:
            knowledge = all_knowledge
        self._knowledge = knowledge

    def get_knowledge(self):
        return self._knowledge

    def set_knowledge(self, knowledge):
        if isinstance(knowledge, list):
            self._knowledge = knowledge

    knowledge = property(get_knowledge, set_knowledge)

    def teach(self):
        if self._knowledge:
            return random.choice(self._knowledge)  # Return a random item from knowledge
        else:
            return None   

    
    
techear = Teacher('da', 'da')
techear.teach()    