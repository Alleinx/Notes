import java.lang.reflect.InvocationHandler;

public interface I_Handler extends InvocationHandler {
    public void setTarget(Target target);
}