/**
 * This program demonstrate Local Inner Class
 * 
 * If there is only one function in an inner class and only be invoked in a specific function,
 * then, it's a good time to use local inner class.
 * 
 * Local inner class can't be declared as public or private, and it's completely invisible from outside world.
 * 
 */
import java.util.Date;

public class LocalInnerClass {
    
    public void start(final int value) {

        class LocalInner {
            
            public void getDate(int value) {
                Date now = new Date();
                System.out.println("At this lovely moment, the time is: " + now);
                System.out.println("Could also use local var here, but local var should be declared as final.");
                System.out.println("Local var:" + value);
                System.out.println("Could also use instance var: " + TestValue);
            }
        }

        LocalInner local = new LocalInner();
        TestValue = 0xC;
        local.getDate(value);
        
    }

    public static void main(String[] args) {
        LocalInnerClass localTest = new LocalInnerClass();
        localTest.start(100);
        
    }

    private int TestValue;
}