import java.util.ArrayList;

public class TaskManager {
    private static int SIZE = 3;
    private TaskManager() {};

    private static class Holder {
        private static ArrayList<TaskManager> instance = new ArrayList<>();
    }
    
    public static TaskManager getInstance(int i) {
        if (i > SIZE) return null;
        
        if (i > Holder.instance.size()) {
            Holder.instance.add(new TaskManager());
        }

        return Holder.instance.get(i-1);
    }

}