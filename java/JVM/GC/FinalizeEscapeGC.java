/**
 * FinalizeEscapeGC
 * This program demonstrate how GC works in JVM
 * Algorithm used: reachability analysis + second chance 
 * 
 * reachability analysis: similar to Tree construct in Graph (DFS, BFS)
 * second chance: first chance (failed in reachability analysis) + second chance (self-resuce)
 * 
 * If an object run out of its chance ->GC will collect it.
 */
public class FinalizeEscapeGC {

    public static FinalizeEscapeGC SAVE_HOOK = null;

    public void isAlive() {
        System.out.println("Still alive here :)");
    }

    /* Note: finalize() only be executed once in JVM, even it may be invoked for many times; */
    @Override
    protected void finalize() throws Throwable {
        super.finalize();
        System.out.println("finalize() executed");
        FinalizeEscapeGC.SAVE_HOOK = this;
    }

    public static void main(String[] args) throws Throwable{
        SAVE_HOOK = new FinalizeEscapeGC();

        /* run out of first chance here */
        SAVE_HOOK = null;
        System.gc();

        Thread.sleep(1000); /* wait for F-Queue's Finalizer to execute */

        if (SAVE_HOOK != null) {
            SAVE_HOOK.isAlive();
        } else {
            System.out.println("No, dead here :(");
        }

        /* Same code as above but dead */
        SAVE_HOOK = null;
        System.gc();

        Thread.sleep(1000);
        if (SAVE_HOOK != null) {
            SAVE_HOOK.isAlive();
        } else {
            System.out.println("No, dead here QAQ");
        }

    }
}