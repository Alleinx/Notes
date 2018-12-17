/**
 * A specific implementation of Handler.
 */
import java.lang.reflect.Method;

public class ProxyHandler implements I_Handler{

    private Target target;

    @Override
    public void setTarget(Target target) {
        this.target = target;
    }

    /* If Want to change the behavior of this handler, change this invoke function. */
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("Start working......");
        Object returnValue = method.invoke(target, args);
        System.out.println("Finish working, system shutting down......");
        return returnValue;
    }
}