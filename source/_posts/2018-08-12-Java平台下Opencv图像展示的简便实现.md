---
title: Java平台下Opencv图像展示的简便实现
date: 2018-08-12 21:21:14
categories: OpenCV
tags: [OpenCV]
description: 在C++环境下的OpenCV中，展示Mat图像可以通过imshow()实现。但在Java平台上该怎样简便地实现呢？
---

在C++环境下的OpenCV中，展示Mat图像可以通过imshow()实现。但在Java平台上该怎样简便地实现呢？

通常的做法是将读取到的Mat转化为BufferedImage，将BufferedImage作为GUI中的icon进行展示。下方是将Mat转化为BufferedImage的代码。
```Java
	/**
     * Mat转换成BufferedImage
     * 
     * @param matrix 要转换的Mat
     * @param fileExtension 格式为 ".jpg", ".png", etc
     * @return 转换后的BufferedImage
     */
    public static BufferedImage Mat2BufferedImage (Mat matrix, String fileExtension) {
        // convert the matrix into a matrix of bytes appropriate for this file extension
        MatOfByte mob = new MatOfByte();
        Imgcodecs.imencode(fileExtension, matrix, mob);
        // convert the "matrix of bytes" into a byte array
        byte[] byteArray = mob.toArray();
        BufferedImage bufImage = null;
        try {
            InputStream in = new ByteArrayInputStream(byteArray);
            bufImage = ImageIO.read(in);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return bufImage;
    }
```

这里提供一种简单的方法，实现了类似C++的图像展示方式。


```Java
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.image.BufferedImage;

import javax.swing.JFrame;
import javax.swing.JPanel;

import org.opencv.core.Mat;

public class ImageUI extends JPanel implements KeyListener {


    public ImageUI(Mat m, String window) {
        super();
        init(m, window);
    }

    //Elements for paint.
    private Mat mat;
    private boolean firstPaint = true; 
    private BufferedImage out;
    int type;
    private String WINDOW = ""; 
    private JFrame jframe = new JFrame();        
    byte[] data;
    private void Mat2BufIm(){               
        mat.get(0, 0, data);
        out.getRaster().setDataElements(0, 0, mat.cols(), mat.rows(), data);
    }
    private void init(Mat m,String window){
        this.mat = m;
        data = new byte[mat.cols() * mat.rows() * (int)mat.elemSize()];

        WINDOW = window;

        if(mat.channels() == 1)
            type = BufferedImage.TYPE_BYTE_GRAY;
        else
            type = BufferedImage.TYPE_3BYTE_BGR;
        out = new BufferedImage(mat.cols(), mat.rows(), type);
        Mat2BufIm();    
        jframe.add(this);  
        jframe.setSize(mat.cols(), mat.rows());  
        jframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        jframe.setTitle(WINDOW);
        jframe.addKeyListener(this);
    }
    @Override  
    public void paintComponent(Graphics g) {  
            g.drawImage(out, 0, 0, null);   
        }
    public ImageUI imshow(){
        if(firstPaint){
            jframe.setVisible(true); 
            firstPaint = false;
            }
        Mat2BufIm();
        this.repaint();
        return this;
    }

    //Elements for waitKey.
    private static Object mt = new Object();
    private static int lastKey = 0;
    private static int key = 0;
    public static int waitKey(int millisecond){
        //TODO 实现监听键盘
        try {
            if(millisecond == 0){
                synchronized(mt){
                    mt.wait();
                }
            }
            Thread.sleep(millisecond);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        int ret = -1;
        if(key != lastKey){
            ret = key;
            lastKey = key;          
        }
        return ret;
    }
    @Override
    public void keyPressed(KeyEvent e) {
        synchronized(mt){
            mt.notifyAll();
        }
        this.key = e.getKeyCode();
    }
    @Override
    public void keyReleased(KeyEvent arg0) {
        // TODO Auto-generated method stub

    }
    @Override
    public void keyTyped(KeyEvent arg0) {
        // TODO Auto-generated method stub

    }  
}
```

在项目中添加上面的源码后，可以通过以下方式实现图像的展示：

```Java
    Mat mat = Mat.eye(1000, 2000, CvType.CV_8UC3);
    String window_name = "mat"
    ImageUI ig = new ImageGui(mat,window_name);
    ig.imshow();
    ig.waitKey(0);
```

或者，可以通过另一种简单的方法实现：

```Java
    Mat mat = Mat.eye(1000, 2000, CvType.CV_8UC3);
    new ImageGui(mat,"mat").imshow().waitKey(0);
```