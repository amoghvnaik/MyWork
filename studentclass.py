class student:
    def __init__(self, english_score, maths_score, science_score):
        self.english_score = english_score
        self.maths_score = maths_score
        self.science_score = science_score
    def get_average(self):
        print((self.english_score + self.maths_score + self.science_score)/3)
        
student(50,50,50).get_average()
student(60,60,60).get_average()
student(70,70,70).get_average()
