/**
 * 
 */
public class Target implements I_Proxy{
    private String name;

    public Target(String name) {
        this.name = name;
    }

    @Override
    public void save() {
        System.out.println(name + " Saving data......");
    }

}