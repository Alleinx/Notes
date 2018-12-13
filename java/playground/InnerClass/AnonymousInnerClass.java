/**
 * AnonymousInnerClass
 * 
 * When only create small amount of instance of a class, 
 * it's a good time to try anonymous class.
 */

import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;
import javax.swing.Timer;

public class AnonymousInnerClass {

    public static void main(String[] args) {
        TalkingClock clock = new TalkingClock();
        clock.start(1000, true);

        JOptionPane.showMessageDialog(null, "Quit?");
        System.exit(0);
    }
}

class TalkingClock {
    public void start(int interval, final boolean beep) {
        ActionListener listener = new ActionListener(){
        
            @Override
            public void actionPerformed(ActionEvent e) {
                Date now = new Date();
                System.out.println("Time: " + now);
                if (beep) {
                    Toolkit.getDefaultToolkit().beep();
                }
            }
        };

        Timer t = new Timer(interval, listener);
        t.start();
    }
}