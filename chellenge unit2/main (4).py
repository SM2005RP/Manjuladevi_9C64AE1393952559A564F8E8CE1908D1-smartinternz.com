class player:
 
  def play(self):
    print("the player is playing cricket.")
 
class Batman(player):
  def play(self):
        print("the batman is batting.")

class Bowler(player):
  def play(self):
     print("the bowler is bowling.")
          
batman = Batman()
bowler = Bowler()

batman.play()
bowler.play()
      

