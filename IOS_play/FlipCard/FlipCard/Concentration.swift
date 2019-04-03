//
//  Concentration.swift
//
//  Created by noObject on 2019/4/1.
//  Copyright © 2019 noObject. All rights reserved.
//


class Concentration {
    var cards = [Card]()
    
    var indexOfOneAndOnlyFaceUpCard : Int?
    
    init(numberOfPairsOfCards: Int) {
        for _ in 0 ..< numberOfPairsOfCards {
            let card = Card()
            
            cards += [card, card] //copy two card into cards 
            //cards.append(card)
        }
        cards.shuffle()
    }
    
    func flipCard(at toMatch: Int) {
        if !cards[toMatch].isMatched {
            if let alreadyFliped = indexOfOneAndOnlyFaceUpCard , alreadyFliped != toMatch {
                if cards[alreadyFliped].identifier == cards[toMatch].identifier {
                    // Check if cards match
                    cards[alreadyFliped].isMatched = true
                    cards[toMatch].isMatched = true
                }
                
                cards[toMatch].isFaceUp = true
                indexOfOneAndOnlyFaceUpCard = nil
                
            } else {
                //either no cards or 2 cards are face up
                for flipDownIndex in cards.indices {
                    cards[flipDownIndex].isFaceUp = false
                }
                cards[toMatch].isFaceUp = true
                indexOfOneAndOnlyFaceUpCard = toMatch
            }
        }
        
        gameOver()
    }
    
    func gameOver() {
        for index in cards.indices {
            if cards[index].isMatched == false {
                return
            }
        }
        
        print("Game Over")
    }
}
