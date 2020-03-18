import unittest

class TestGame(unittest.TestCase):
    def setUP(self):
        self.game = Game()
        self.player = Player()

    def test_move(self):
        current_room = WaterRoom()
        room_2 = DesertRoom()

        self.game.connect_room(current_room, room_2, self.game.ASLEFTROOM)

        self.game.set_player_room(current_room)

        self.player.move_east()

        self.assertEquals(self.player.get_player_room(), room_2)

if __name__ == '__main__':
    unittest.main()

