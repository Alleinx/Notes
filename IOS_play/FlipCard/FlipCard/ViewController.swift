//
//  ViewController.swift
//  Created by noObject on 2019/3/31.
//  Copyright © 2019 noObject. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet weak var flipCountLabel: UILabel! //Text content in UI
    
    @IBOutlet var cardButtons: [UIButton]! //Buttons on UI
    
    private lazy var game = Concentration(numberOfPairsOfCards: cardButtons.count / 2)
    
    private var flipCount: Int = 0 {
        didSet {
            flipCountLabel.text = "Flips: \(flipCount)"
            //Everytime filpCount changes, codes will be executed.
        }
    }
    
    private var emojiChoices: [String] = ["🍔", "🥓", "🌎", "❄️", "💥", "🥊", "🍅",
                                          "🍉", "🍇", "🍈", "🍞", "🥒", "🍒", "🍟",
                                          "🍣","🍘", "🍝", "🥪", "🥠", "🌒"]
    
    private var emoji = Dictionary<Int, String>()
    
    @IBAction func touchCard(_ sender: UIButton) {
        //Everytime Buttons on UI are clicked, this func will be executed.
        //Hold 'control' key and drag the method into code area.
        
        flipCount += 1
        
        if let cardNumber = cardButtons.index(of: sender) {
            //return: nil -> optional is not set
            //If optional is set -> return corresponding value with corresponding data type.
            //could use ! after optional value to unwrap the value
            //also could use if else like this.
            game.flipCard(at: cardNumber) //flip the card
            updateViewFromModel()
        } else {
            print("Chosen card was not in cardButtons")
        }
    }

    
func updateViewFromModel() {
        
        for index in cardButtons.indices {
            let button = cardButtons[index]
            let card = game.cards[index]
            
            if card.isFaceUp {
                button.setTitle(emoji(for: card), for: UIControl.State.normal)
                button.backgroundColor = #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)
            } else {
                button.setTitle("", for: UIControl.State.normal)
                button.backgroundColor = card.isMatched ? #colorLiteral(red: 1, green: 1, blue: 1, alpha: 0) : #colorLiteral(red: 1, green: 0.5763723254, blue: 0, alpha: 1)    //If the card is matched, then make it invisible.
            }
        }
    }
    
    func emoji(for card: Card) -> String {
        if emoji[card.identifier] == nil {
            if emojiChoices.count > 0 {
                let randomIndex = Int(arc4random_uniform(UInt32(emojiChoices.count)))
                emoji[card.identifier] = emojiChoices.remove(at: randomIndex)
            }
        }
        
        return emoji[card.identifier] ?? "?"
    }
}

