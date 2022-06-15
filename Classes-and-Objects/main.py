from logging import exception


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

   # creating the methods

    def change_name(self, new_name):
        # self.name = new_name
        print("the new name is", new_name)

    def change_age(self, new_age):
        self.age = new_age
        print("The new age is", new_age)

        # validation for new_age
        try:
            new_age = int(new_age)
        except:
            print("Enter a valid data type.")
            raise exception

    def add_track(self, new_tracks):
        self.tracks.append(new_tracks)
        print("The new track is", self.tracks)

    def get_score(self):
        # since there is no new score to be passed, we should return the initial score.
        print("The new score is", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)


# h = Student()
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
