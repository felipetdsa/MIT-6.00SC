from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#Name: Felipe Trovão de Sá
#Time: 2 hours


def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    wscore = 0
    cword = None
    #lword = []
    for i in xrange(1, HAND_SIZE + 1):
        for word in get_perms(hand, i):
            if word in word_list:
                #lword.append(word)
                if (get_word_score(word, HAND_SIZE)) > wscore:
                    wscore = get_word_score(word, HAND_SIZE)
                    cword = word
    return cword        #, lword
        

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    points = 0
    while calculate_handlen(hand) > 0:
        print 'Current hand: ',
        display_hand(hand)
        print '- SkyNet, enter your guess: '
        guessed = comp_choose_word(hand, word_list)        
        if guessed == None:
            print
            print '- I have no more guess, Master!'
            print 'Total scored: ' + str(points)
            return
        else:
            print guessed
            print
            points += get_word_score(guessed, len(hand))
            update_hand(hand, guessed)
    print 'No more guesses. Total scored: ' + str(points)
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    while True:
        opt = str.lower(raw_input('Enter your option: "n", "r", "e": '))
        if opt == 'n':
            hand = deal_hand(HAND_SIZE)
            opt2 = str.lower(raw_input('Enter "u" for human play or "c" for computer play: '))
            while True:
                if opt2 =='u':                    
                    play_hand(hand.copy(), word_list)
                    print
                    break
                elif opt2 == 'c':
                    comp_play_hand(hand.copy(), word_list)
                    print
                    break
                else:
                    print '1-Invalid option, please, try again.'
        elif opt == 'r':
            opt2 = str.lower(raw_input('Enter "u" for human play or "c" for computer play: '))
            while True:
                if opt2 =='u':                    
                    play_hand(hand.copy(), word_list)
                    print
                    break
                elif opt2 == 'c':
                    comp_play_hand(hand.copy(), word_list)
                    print
                    break
                else:
                    print '2-Invalid option, please, try again.'            
        elif opt == 'e':
            return
        else:            
            print '3-Invalid option, please, try again.'
            print

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
