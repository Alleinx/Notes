/**
 * ProxyStuff
 */
public class ProxyStuff implements I_Proxy{
    private Target target;
    public ProxyStuff(Target target) {
        this.target = target;
    }

    @Override
    public void save() {
        System.out.println("Initialing data......");
        target.save();
        System.out.println("Finished, System shutting down......");
    }
}