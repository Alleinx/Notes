/* This program demonstrate when init mechanism will be triggered in JVM */

/** 
 * 1. InitCase will be init because it contains main() function.
 * 2. SuperClass will be init because SuperClass.value is being used.
 * 3. SubClass may or may not be init (Depends on implementation of JVM)
 *    Could use -XX:+TraceClassLoading args to observe SubClass's loading.
 */

public class InitCase {
    public static void main(String[] args) {
        
        System.out.println(SubClass.value);
        System.out.println(SubClass.subValue); /* will trigger SubClass init */
    }
}

class SuperClass {
    static {
        System.out.println("SuperClass init!");
    }

    public static int value = 123;
    
}

class SubClass extends SuperClass {

    static {
        System.out.println("SubClass init!");
    }

    public static int subValue = 1; 
    /**
     * If use 'final' in declaration, then SubClass's init will not be triggered because 
     * 'subValue' has been stored in constant pool.
     */
}