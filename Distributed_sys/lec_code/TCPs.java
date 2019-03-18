/* TCP example server */

import java.io.*;
import java.net.*;

/**
 * TCPs
 */
public class TCPs {

    public static void main(String[] args) {
        ServerSocket ss = null;

        try {
            ss = new ServerSocket(12345);
            System.out.println("Server ready...");

            while (true) {
                Socket s = ss.accept();
                System.out.println("s = " + s);
                InputStreamReader isr = new InputStreamReader(s.getInputStream());

                BufferedReader br = new BufferedReader(isr, 512);
                String data = br.readLine();
                System.out.println("Msg = " + data);

                OutputStreamWriter osw = new OutputStreamWriter(s.getOutputStream());
                BufferedWriter bw = new BufferedWriter(osw, 512);
                PrintWriter pw = new PrintWriter(bw);
                pw.println("Message OK!");
                pw.flush();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
