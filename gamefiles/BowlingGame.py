"""Module consisting of the educational bowling game's mechanics.
Author: Unknown
Date: 25th of September 2021
"""

class BowlingGame:
    """This class contains the bowling game mechanics."""
    
    
    def __init__(self):
        self.rolls=[]

    def roll(self,pins):
        """Adds a 'roll' in the list of rolls.
        
        Keyword arguments:
        pins -- The number of pins knocked down for one roll.
        This gets added to the list of rolls.
        """
        self.rolls.append(pins)

    def score(self):
        """Calculates the total score based on the list of rolls.
        Returns the calculated sum."""
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
        return result

    def isStrike(self, rollIndex):
        """Checks whether a specified roll equals 10.
        
        Keyword arguments:
        rollIndex -- index used to get the specific roll score to be compared
        """
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        """Checks whether two specified rolls equal 10.
        
        Keyword arguments:
        rollIndex -- index used to get the specific roll scores to be compared
        """        
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    def strikeScore(self,rollIndex):
        """Returns the next frame's score plus 10 for scoring a strike.
        
        Keyword arguments:
        rollIndex -- index used to get the specific roll scores to be added
        """        
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        """Returns the next frame's first roll score plus 10 for scoring a spare.
        
        Keyword arguments:
        rollIndex -- index used to get the specific roll score to be added
        """
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        """Returns the score for one frame.
        
        Keyword arguments:
        rollIndex -- index used to get the specific frame score
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]

