/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package AHP;

import java.awt.BorderLayout;
import java.awt.Color;
import java.util.ArrayList;
import java.util.Scanner;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;


public class MainClass {

    static Scanner sc = new Scanner(System.in);
    int noCon;
    String[] nameCon;
    int noRes;
    String[] nameRes;
    ArrayList<MaTran> arrMatranRes = new ArrayList<>();
    float[] arrF;
    MaTran matrixCon;

    public void MatrixCon() {
        System.out.println("So luong tieu chi: ");
        noCon = sc.nextInt();
        sc.nextLine();
        nameCon = new String[noCon];
        for (int i = 0; i < noCon; i++) {
            System.out.println("Ten tieu chi " + (i + 1) + ": ");
            nameCon[i] = sc.nextLine();
        }
        matrixCon = new MaTran(noCon, nameCon);

        System.out.println("-----Nhap ma tran tieu chi-----");
        matrixCon.input();
        System.out.println("Ta co MA TRAN TIEU CHI nhu sau: ");
        matrixCon.display();
        System.out.println("VECTOR RIENG cua Ma tran tieu chi: ");
        matrixCon.getEigenVector().display();

    }

    public void MatrixRes() {
        System.out.println("-----So luong PHUONG AN-----");
        noRes = sc.nextInt();
        sc.nextLine();
        nameRes = new String[noRes];
        arrF = new float[noRes];
        for (int i = 0; i < noRes; i++) {
            System.out.println("Ten PHUONG AN " + (i + 1) + ": ");
            nameRes[i] = sc.nextLine();
        }
        for (int i = 0; i < noCon; i++) {
            System.out.println("---NHAP MA TRAN PHUONG AN CUA TIEU CHI " + nameCon[i].toUpperCase() + "---");
            MaTran matrixRes = new MaTran(noRes, nameRes);
            matrixRes.input();
            System.out.println("Ta co MA TRAN PHUONG AN cua TIEU CHI " + nameCon[i].toUpperCase() + " như sau: ");
            matrixRes.display();
            System.out.println("VECTOR RIENG cua Ma tran nay: ");
            matrixRes.getEigenVector().display();
            arrMatranRes.add(matrixRes);
        }
    }

    public void f() {
        float f;
        for (int i = 0; i < noRes; i++) {
            f = 0;
            for (int j = 0; j < noCon; j++) {
                f += arrMatranRes.get(j).eigenVector.arrVector[i] * matrixCon.eigenVector.arrVector[j];
            }
            arrF[i] = f;
        }
    }

    public void displayResult() {
        System.out.println("----------------------------***RESULT***----------------------------");
        for (int i = 0; i < noCon; i++) {
            System.out.println("---***Ket qua theo tieu chi " + nameCon[i].toUpperCase() + "***---");
            for (int j = 0; j < noRes; j++) {
                System.out.println("Phuong an " + nameRes[j] + ":\t" + arrMatranRes.get(i).eigenVector.arrVector[j]);
            }
        }
        System.out.println("-----***FINAL RESULT***-----");
        for (int i = 0; i < noRes; i++) {
            System.out.println("f(" + nameRes[i] + ") = " + arrF[i]);
        }
        
        float max = arrF[0];
        int index = 0;
        for(int i=1; i< noRes; i++) {
        	if(arrF[i] > max) {
        		max = arrF[i];
        		index = i;
        	}
        }
        System.out.println("Vay ta chon phuong an: "+ nameRes[index]);
    }
    
    public static void main(String[] args) {
        MainClass m = new MainClass();
        m.MatrixCon();
        m.MatrixRes();
        m.f();
        m.displayResult();
    }
}
