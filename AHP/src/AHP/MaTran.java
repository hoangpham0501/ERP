/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package AHP;

import java.util.Scanner;

public class MaTran {

    int n;
    float arr[][];
    EigenVector eigenVector;
    String nameCol[] = new String[n];
    Scanner sc = new Scanner(System.in);

    public MaTran(int n, String[] name) {
        this.n = n;
        arr = new float[n][n];
        eigenVector = new EigenVector(n);
        nameCol = name;
    }

    public void input() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
            	if(i == j) {
            		arr[i][j] = 1;
            	}
            	else if(arr[i][j] == 0) {
            		System.out.println("[" + nameCol[i] + "][" + nameCol[j] + "]: ");
                    arr[i][j] = sc.nextFloat();
                    arr[j][i] = 1/ arr[i][j];
                    sc.nextLine();
            	}            
            }
        }
    }

    public void display() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(arr[i][j] + "\t");
            }
            System.out.println("");
        }
    }

    public EigenVector getEigenVector() {
        float[] sum = new float[n];
        
        //Sum of each column
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sum[i] += arr[j][i];
            }
        }
        
        //divide each element of arr with the respective sum
        float[][] temp = new float[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                temp[j][i] = arr[j][i] / sum[i];
            }
        }
        
        float[] result = new float[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i] += temp[i][j];
            }
        }
        
        float s =0;
        for(int i=0; i<n; i++) {
        	s += result[i];
        }
        
        for (int i = 0; i < n; i++) {
            eigenVector.arrVector[i] = result[i] / s;
        }
        
        return eigenVector;
    }

}
