from hands import YatzyHand
from dice import D6
from scoresheets import YatzyScoresheet

monopoly = YatzyHand()
d1 = D6(value=4)
d2 = D6(value=5)
monopoly[:] = [d1, d2]

print(monopoly)
print(monopoly.doubles)