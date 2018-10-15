import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map; 

import javax.imageio.ImageIO; 


import com.google.zxing.*;
import com.google.zxing.client.j2se.BufferedImageLuminanceSource;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.common.HybridBinarizer;

public class QRCodeGenerator {

    public void generateQrCode(String text, String format,String path)
    {
            
            int width = 200;   
            int height = 200;   

            Hashtable<EncodeHintType, String> hints = new Hashtable<EncodeHintType, String>();  
            hints.put(EncodeHintType.CHARACTER_SET, "utf-8");
            BitMatrix bitMatrix = null;
            try {
                bitMatrix = new MultiFormatWriter().encode(text, BarcodeFormat.QR_CODE, width, height, hints);
            } catch (WriterException e1) { 
                e1.printStackTrace();
            }    
            File outputFile = new File(path);  
            try {
                MatrixToImageWriter.writeToFile(bitMatrix, format, outputFile);
            } catch (IOException e) { 
                e.printStackTrace();
            }

    }
}