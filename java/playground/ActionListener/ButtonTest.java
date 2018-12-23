import java.awt.EventQueue;
import javax.swing.JFrame;

/**
 * ButtonTest
 */
public class ButtonTest {

    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable(){
        
            @Override
            public void run() {
                // ButtonFrame frame = new ButtonFrame();
                AnoButtonFrame frame = new AnoButtonFrame();
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setVisible(true);
            }
        });
    }
}