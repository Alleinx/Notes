import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;

public class HistoryPanel extends JPanel {
    private Bank m;

    public HistoryPanel(Bank m) {
        this.m = m;
    }

    private int historyMax(ArrayList<Integer> t) {
        int result = 0;
        for (Integer e : t) {
            if (result < e) {
                result = e;
            }
        }
        return result;
    }

    private int historyMin(ArrayList<Integer> t) {
        int result = 0;
        for (Integer e : t) {
            if (result > e) {
                result = e;
            }
        }
        return result;
    }

    private int historyRange(ArrayList<Integer> t) {
        int max = historyMax(t);
        int min = historyMin(t);
        int result = max - min;
        if (result < 100) {
            return 100;
        }

        return result;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        ArrayList<Integer> history = m.getHistory();
        int min = historyMin(history);
        int range = historyRange(history);
        int maxX = getWidth() - 1;
        int maxY = getHeight() - 1;
        int zero = maxY + min * maxY / range;

        g.setColor(Color.BLUE);
        g.drawLine(0, zero, maxX, zero);

        g.setColor(Color.red);
        if (history.size() == 1) {
            g.drawRect(0, (zero - history.get(0) * maxY / range), 1, 1);
        }
        else {
            for (int i = 1; i < history.size(); i++) {
                int prv_x = 10 * (i-1);
                int prv_y = zero - history.get(i-1) * maxY / range;
                int x = 10 * i;
                int y = zero - history.get(i) * maxY / range;
                g.drawLine(prv_x, prv_y, x, y);
            }
        }
    }
}
