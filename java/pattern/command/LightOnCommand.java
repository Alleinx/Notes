public class LightOnCommand implements Command{

    public LightOnCommand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() {
        light.on();
    }

    private Light light;
}
