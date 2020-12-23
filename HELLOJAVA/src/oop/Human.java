package oop;

public class Human extends Animal{
	public int moneypower = 11;
	
	public void makeMoney(int earnmoney) {
		moneypower += earnmoney;
	}
}