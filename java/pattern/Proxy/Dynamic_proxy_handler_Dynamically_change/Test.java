/**
 * Static Proxy
 */
public class Test {
    public static void main(String[] args) {
        
        Target t1 = new Target("T1");
        Target t2 = new Target("T2");
        
        I_Handler proxyHandler1 = new ProxyHandler();

        ProxyFactory factory = new ProxyFactory(t1, proxyHandler1);
        I_Proxy proxy = (I_Proxy)factory.getProxyInstance();

        proxy.save();

        factory.setTarget(t2);


        proxy = (I_Proxy)factory.getProxyInstance();
        proxy.save();

        // factory.setHandler(proxyHandler2); => dynamically change Handler
    }
}