public class Main {

    public static void main(String[] args) {
        Light sl = new smallLight();
        LightOnCommand lc = new LightOnCommand(sl);
        LightOffComand lf = new LightOffComand(sl);
        Invoker a = new Invoker();

        a.setCommand(1, lc, lf);

        a.onButtonPressed(1);
        a.offButtonPressed(3);
        a.offButtonPressed(1);
        a.onButtonPressed(8);
    }
}
