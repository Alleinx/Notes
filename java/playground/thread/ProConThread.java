/**
 * MyThread
 */
public class ProConThread {

    public static void main(String[] args) {
        Product product = new Product();

        Runnable pro = new Producer(product);
        Runnable con = new Consumer(product);

        Thread a = new Thread(pro, "Thread:Producer");
        Thread b = new Thread(con, "Thread:Consumer");

        a.start();
        b.start();

    }
}

class Producer implements Runnable {
    private Product product = null;

    public Producer(Product product) {
        this.product = product;
    }

    public void run() {
        for (int i = 0; i < 50; i++) {
            product.produce();
        }
    }
}

class Consumer implements Runnable {
    private Product product = null;

    public Consumer(Product product) {
        this.product = product;
    }

    public void run() {
        for (int i = 0; i < 50; i++) {
            product.consume();
        }
    }
}

class Product {
    private int numOfTV = 0;
    private boolean productGetByConsumer = true;

    public synchronized void produce() {
        if (!productGetByConsumer) {
            try {
                super.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        /* create new TV */
        numOfTV++; 
        productGetByConsumer = false;
        System.out.println(Thread.currentThread().getName() + "-->creating " + numOfTV + " TV.");
        super.notify();
    }
    
    public synchronized void consume() {
        if (productGetByConsumer) {
            try {
                super.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        /* consume new TV */
        System.out.println(Thread.currentThread().getName() + "-->consuming " + numOfTV + " TV.");
        productGetByConsumer = true;
        super.notify();
    }

}