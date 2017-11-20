/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package AHP;

public class EigenVector {
    float arrVector[];
    int n;
    public EigenVector(int n){
        this.n = n;
        arrVector = new float[n];
    }
    public void display(){
        for(float a : arrVector){
            System.out.println(a);
        }
    }
    
}
