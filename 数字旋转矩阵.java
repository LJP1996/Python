package com.Liu.Work.File;


public class NUM {
	static int a = 6;
	int[][] arr = new int[a][a];
	public static void main(String[] args) {
		NUM num = new NUM();
		num.Create(1,0,a);
		num.Obervice();
	}
	public void Obervice() {
		// TODO Auto-generated method stub
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < a; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println("\n");
		}
	}
	public void Create(int number,int start,int size) {
		// TODO Auto-generated method stub
		if (size==1) {
			arr[start][start] = number;
			return;
		}
		if (size<=0) {
			return;
		}
		int i = start;
		int j = start;
		
		for(int k=0;k<size-1;k++){
			arr[i][j]=number;
			number++;
			i++;
		}
		for(int k=0;k<size-1;k++){
			arr[i][j]=number;
			number++;
			j++;
		}
		for(int k=0;k<size-1;k++){
			arr[i][j]=number;
			number++;
			i--;
		}
		for(int k=0;k<size-1;k++){
			arr[i][j]=number;
			number++;
			j--;
		}
		
		Create(number, start+1, size-2);
		
	}
	
}
