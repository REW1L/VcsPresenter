

class Committer:
    name = ''
    email = ''
    commits = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.commits = []

    def __str__(self):
        return self.name + " " + self.email

    def add_commit(self, commit):
        self.commits.append(commit)

    def get_commit(self, index):
        self.commits.index(index)