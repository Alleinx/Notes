public class LightOffComand implements Command {

    public LightOffComand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.off();
    }

    private Light light; /* receiver */
}
