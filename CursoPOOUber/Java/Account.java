package CursoPOOUber.Java;

public class Account {
    private Integer id;
    private String name;
    private String document;
    private String email;
    private String password;

    public Account(Integer id, String name){
        this.id = id;
        this.name = name;
        // this.document = document;
        // this.email = email;
        // this.password = password;
    }

    public String getName() {
        return name;
    }
}
