"""
Stores the information of a round of the game. Data like word, time, skips, drawing player and more
"""
from numpy import place

import time as t
from _thread import *
from .chat import Chat
from .game import Game

class Round(object):

    def __init__(self, word, player_drawing, players):
        """
        init object
        :param word: str
        :param player_drawing: Player
        :param players: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.players_score = {player:0 for player in players}
        self.time = 75
        self.chat = Chat(self)
        self.start = t.time()
        start_new_thread(self.time_thread, ())

    def time_thread(self):
        """
        Runs in thread to keep track of time
        :return: None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time's up!!!")

    def guess(self, player, wrd):
        """
        Return true if the player got guess correct
        :param player: Player
        :param wrd: str
        :return: None
        """
        correct = self.word == wrd
        if correct:
            self.player_guessed.append(player)
            # TODO Implement scoring system here

    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return:None
        """
        if player in self.players_score:
            del self.player_score[player]
        if player in self.player_guessed:
            self.player_guessed.remove(player)
        if player == self.player_drawing:
            self.end_round("Drawing player leaves!!!")

    def end_round(self, msg):
        # TODO Implement end round functionallity
        pass