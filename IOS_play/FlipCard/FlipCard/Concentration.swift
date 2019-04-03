//
//  Concentration.swift
//
//  Created by noObject on 2019/4/1.
//  Copyright © 2019 noObject. All rights reserved.
//


class Concentration {
    private var cards = [Card]()
    
    init(numberOfPairsOfCards: Int) {
        for _ in 0 ..< numberOfPairsOfCards {
            let card = Card()
            
            cards += [card, card] //copy two card into cards 
            //cards.append(card)
        }
        //TODO: Shuffle the cards
    }
    
    func chooseCard(at index: Int) {
        
    }
}
