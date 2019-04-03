//
//  Card.swift
//  Wearing
//
//  Created by noObject on 2019/4/1.
//  Copyright © 2019 noObject. All rights reserved.
//



struct Card {
    var isFaceUp = false
    var isMatched = false
    var identifier : Int
    
    static var identifierFactory = 0
    
    static func getUniqueIdentifier() -> Int {
        identifierFactory += 1
        
        return identifierFactory
    }
    
    init() {
        identifier = Card.getUniqueIdentifier()
    }
}
