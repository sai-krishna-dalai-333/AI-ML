#defining cleaning function
def clean(c):
  goal_state={}
  goal_state[c]='0'
  print("location  is cleaned ",c)
  
#defining move_right function 
def move_right(c):
  print("Move Right to location ",c)
  
 #defining move_left function
def move_left(c):
  print("Move left to location",c)
  
  def vacuum():
        
    goal_state = {'A': '0', 'B': '0'}
    location_input = input("Enter Location of Vacuum") #user_input of location vacuum is placed
    status_input = input("Enter status of " + location_input) #user_input if location is dirty or clean
    status_input_complement = input("Enter status of other room")
    

    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1': #check whether our location is dirty
            print("Location A is Dirty.")  # if it is true clean it...
            clean('A')
            
            if status_input_complement == '1': #check our opposite room is dirty 
                print("Location B is Dirty.") #if its true move cleaner to right and clean
                move_right('B')
                clean('B')
               
            else:   #if opposite room is already clened the no need to clean
                print("Location B is already clean.")

        if status_input == '0':    #if room is clean no need to clean again
            print("Location A is already clean ")
            if status_input_complement == '1': # check for opposite room
                print("Location B is Dirty.")
                move_right('B') 
                clean('B')
                
            else:
                print("Location B is already clean.")

    else:
        print("Vacuum is placed in location B")
        if status_input == '1':
            print("Location B is Dirty.")
            clean('B')
           
            if status_input_complement == '1':
                print("Location A is Dirty.")
                move_left('A')
                clean('A')
        else:
            print("Location B is already clean.")

            if status_input_complement == '1': # if A is Dirty
                print("Location A is Dirty.")
                move_left('A')
                clean('A')
            else:
                print("Location A is already clean.")

 
    print("GOAL STATE: ")
    print(goal_state)
    
vacuum()
