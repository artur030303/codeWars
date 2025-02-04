def rps(p1, p2):
    winning_result={
        'rock':'scissors',
        'scissors': 'paper',
        'paper': 'rock',

    }     
    if p1 == p2:
        return 'Draw!'
    elif winning_result[p1]==p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"


print(rps('paper', 'rock'))
print(rps('rock', 'rock'))
print(rps('paper', 'scissors'))
print(rps('rock', 'scissors'))
print(rps('scissors', 'rock'))




#    @test.it("Player 1 wins")
#     def player_1():
#         test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
#     @test.it("Player 2 wins")
#     def player_1():
#         test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
#     @test.it("Draw")
#     def draw():
#         test.assert_equals(rps('rock', 'rock'), 'Draw!')    