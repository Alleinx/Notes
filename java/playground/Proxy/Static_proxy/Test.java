/**
 * Static Proxy
 */
public class Test {
    public static void main(String[] args) {
        I_Proxy proxy = new ProxyStuff(new Target());
        proxy.save();
    }
}