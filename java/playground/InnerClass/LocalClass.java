/**
 * This program demonstrate basic syntax for Inner class
 */
public class LocalClass {

    private class InnerClass {
        private void inner() {
            System.out.println("Private Inner class + private function");
        }
    }

    public void test() {
        InnerClass inner = new InnerClass();
        inner.inner();
    }

    public static void main(String[] args) {
        LocalClass outer = new LocalClass();
        outer.test();
        /**
         * When trying out of the class:
         * following operations are valid when InnerCLass is declared as public and inner() is also public 
         * LocalClass.InnerClass inner = outer.new InnerClass(); 
         * inner.inner();
         */
    }
}
