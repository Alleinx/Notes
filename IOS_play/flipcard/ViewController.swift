//
//  ViewController.swift
//  Wearing
//
//  Created by noObject on 2019/3/31.
//  Copyright © 2019 noObject. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    private var flipCount: Int = 0 {
        didSet {
            flipCountLabel.text = "Flips: \(flipCount)"
            //Everytime filpCount changes, codes will be executed.
        }
    }
    
    private var emojiChoices: [String] = ["🍔", "🥓", "🍔", "🥓"]
    
    @IBOutlet weak var flipCountLabel: UILabel!
    @IBOutlet var cardButtons: [UIButton]!
    
    @IBAction func touchCard(_ sender: UIButton) {
        //@IBAction 'circle in line 25', indicates which component is related to this method.
        //Hold 'control' key and drag the method into code area.
        flipCount += 1
        if let cardNumber = cardButtons.index(of: sender) {
            //return: nil -> optional is not set
            //If optional is set -> return corresponding value with corresponding data type.
            //could use ! after optional value to unwrap the value
            //also could use if else like this.
            flipCard(withEmoji: emojiChoices[cardNumber], on: sender)
        
        } else {
            print("Chosen card was not in cardButtons")
        }

        
    }
    
    func flipCard(withEmoji emoji: String, on button: UIButton) {
        
        if button.currentTitle == emoji {
            button.setTitle("", for: UIControl.State.normal)
            button.backgroundColor = #colorLiteral(red: 1, green: 0.5763723254, blue: 0, alpha: 1)
        
        } else {
            button.setTitle(emoji, for: UIControl.State.normal)
            button.backgroundColor = #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)
        }
    }
}

