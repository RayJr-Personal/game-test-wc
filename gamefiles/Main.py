"""Module for testing BowlingGame.py
Author: Unknown
Date: 25th of September 2021
"""

import unittest
import BowlingGame
	
class TestBowlingGame(unittest.TestCase):
    """
    This class is designed to contain and conduct test cases using unittest.
    
    """
    
    
    def setUp(self):
        """Creates an instance of BowlingGame for testing."""
        self.game = BowlingGame.BowlingGame()
        
    def testGutterGame(self):
        """Tests a game where each roll is a gutter ball."""
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score()==0
        
    def testAllOnes(self):
        """Tests a game where each roll scores one pin."""
        self.rollMany(1, 20)
        assert self.game.score()==20
        
    def testOneSpare(self):
        """Tests if the game implements the score bonus
        of scoring a spare.
        """
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16
        
    def testOneStrike(self):
        """Tests if the game implements the score bonus
        of scoring a strike.
        """
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
        
    def testPerfectGame(self):
        """Tests a perfect game."""
        self.rollMany(10,12)
        assert self.game.score()==300
        
    def testSpareGame(self):
        """Tests a game where every frame is a spare."""
        self.rollMany(5,21)
        assert self.game.score()==150
        
    def rollMany(self, pins,rolls):
        """Fills the list of rolls in BowlingGame.
        
        Keyword arguments:
        pins -- the number of pins knocked down for every single roll
        rolls -- the amount of rolls to fill the list with (must amount to 10 frames worth of rolls)
        """
        for i in range(rolls):
            self.game.roll(pins)

#unittest.main()