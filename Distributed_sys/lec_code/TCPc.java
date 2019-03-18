/* TCP sample client */

import java.io.*;
import java.net.*;

public class TCPc {
    public static void main(String[] args) {
        InetAddress ia = null;
        
        try {
            ia = InetAddress.getByName("localhost");
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }

        Socket soc = null;

        try {
            soc = new Socket(ia, 12345);
            OutputStreamWriter osw = new OutputStreamWriter(soc.getOutputStream());
            BufferedWriter bw = new BufferedWriter(osw, 512);
            PrintWriter pw = new PrintWriter(bw);
            pw.println("Sunny is Sleepy now");
            pw.flush();

            InputStreamReader isr = new InputStreamReader(soc.getInputStream());
            BufferedReader br = new BufferedReader(isr, 512);
            String data = br.readLine();
            System.out.println("Reply from Sever = " + data);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
