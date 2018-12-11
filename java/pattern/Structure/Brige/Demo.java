public class Demo {
    public static void main(String[] args) {
        Pen pen = new BigPen();
        Color color1 = new Red();
        pen.setImpl(color1);
        pen.operation();
    }
}

interface Color {
    void operationImpl();
}

abstract class Pen {
    Color implementor;

    public void setImpl(Color impl) {
        this.implementor = impl;
    }
    public abstract void operation();
}

class BigPen extends Pen {
    @Override
    public void operation() {
        System.out.println("using huge size pen");
        implementor.operationImpl();
    }
}

class Red implements Color {
    @Override
    public void operationImpl() {
        System.out.println("using red dye");
    }
}