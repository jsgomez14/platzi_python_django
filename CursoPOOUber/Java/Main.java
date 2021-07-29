package CursoPOOUber.Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Account a = new Account(1,"Andres");

        Car car = new Car("ABC123",a);
        System.out.println(car.toString());

        UberX car2 = new UberX("ABC1DFG456",new Account(2, "Yanse"), "Chevrolet", "Spark");
        System.out.println(car2.toString());

        UberVan van = new UberVan("ABCD463",new Account(2, "Yanse"),null,null);
        System.out.println(van.toString());
    }
}