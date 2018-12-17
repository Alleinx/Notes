import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

/**
 * ProxyFactory
 */
public class ProxyFactory {
    private Target target;

    public ProxyFactory(Target target) {
        this.target = target;
    }

    public void setTarget(Target target) {
        this.target = target;
    }

    public Object getProxyInstance() {
        return Proxy.newProxyInstance(target.getClass().getClassLoader(),
            target.getClass().getInterfaces(),
            new InvocationHandler(){
            
                @Override
                public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                    System.out.println("Start working......");
                    Object returnValue = method.invoke(target, args);
                    System.out.println("Finish working, system shutting down......");
                    return returnValue;
                }
            }
        );
    }
}