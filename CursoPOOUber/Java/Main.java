package CursoPOOUber.Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Account a = new Account(1,"Andres");
        Car car = new Car(1,"ABC123",a,2);
        System.out.println(car.toString());
        Car car2 = new Car(2,"DFG456",new Account(2, "Yanse"),4);
        System.out.println(car2.toString());
    }
}