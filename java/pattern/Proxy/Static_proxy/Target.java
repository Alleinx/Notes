/**
 * StaticProxy
 */
public class Target implements I_Proxy{

    @Override
    public void save() {
        System.out.println("Saving data......");
    }
}