public class Invoker {

    public Invoker() {
        onCommands = new Command[7];
        offCommands = new Command[7];
    }

    public void setCommand(int which, Command onCommand, Command offCommand) {
        if (which > 0 && which < 8) {
            onCommands[which - 1] = onCommand;
            offCommands[which - 1] = offCommand;
        } else {
            System.out.println("Invalid number.");
        }
    }

    public void onButtonPressed(int which) {
        if (which < 1 || which > 7) {
            System.out.println("Invalid number!");
            return;
        }

        if (onCommands[which - 1] != null) {
            onCommands[which - 1].execute();
        } else {
            System.out.println("Bind command first!");
        }
    }

    public void offButtonPressed(int which) {
        if (which < 1 || which > 7) {
            System.out.println("Invalid number!");
            return;
        }
        if (offCommands[which - 1] != null) {
            offCommands[which - 1].execute();
        } else {
            System.out.println("Bind command first!");
        }
    }

    private Command[] onCommands;
    private Command[] offCommands;

}
