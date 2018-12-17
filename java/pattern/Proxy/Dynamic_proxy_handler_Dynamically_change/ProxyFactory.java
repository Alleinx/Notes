import java.lang.reflect.Proxy;

/**
 * ProxyFactory
 */
public class ProxyFactory {
    private Target target;
    private I_Handler handler;

    public ProxyFactory(Target target, I_Handler handler) {
        this.target = target;
        this.handler = handler;
        this.handler.setTarget(this.target);
    }

    public void setTarget(Target target) {
        this.target = target;
        handler.setTarget(this.target);
    }

    public void setHandler(I_Handler handler) {
        this.handler = handler;
        this.handler.setTarget(target);
    }
    
    public Object getProxyInstance() {
        return Proxy.newProxyInstance(target.getClass().getClassLoader(),
            target.getClass().getInterfaces(),
            handler
        );
    }
}