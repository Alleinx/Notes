/**
 * Main
 */
public class Main {


    public static void main(String[] args) {
        QRCodeGenerator generator = new QRCodeGenerator();
        generator.generateQrCode("IT WORKED; GOOD NIGHT.", "png", "./Test.png");
    }
}