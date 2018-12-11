public class Demo {

    public static void main(String[] args) {
        TaskManager t1 = TaskManager.getInstance(1);
        TaskManager t2 = TaskManager.getInstance(2);

        System.out.println(TaskManager.getInstance(1));
        System.out.println(TaskManager.getInstance(2));
    }
}