Single Inheritence
// Parent class
class Parent {
    void displayParent() {
        System.out.println("This is the Parent class.");
    }
}

// Child class
class Child extends Parent {
    void displayChild() {
        System.out.println("This is the Child class.");
    }
}

public class SingleInheritance {
    public static void main(String[] args) {
        Child child = new Child();
        child.displayParent();
        child.displayChild();
    }
}
---------------------------------------------------------------------
MULTILEVEL INHERITENCE

// Grandparent class
class Grandparent {
    void displayGrandparent() {
        System.out.println("This is the Grandparent class.");
    }
}

// Parent class
class Parent extends Grandparent {
    void displayParent() {
        System.out.println("This is the Parent class.");
    }
}

// Child class
class Child extends Parent {
    void displayChild() {
        System.out.println("This is the Child class.");
    }
}

public class MultilevelInheritance {
    public static void main(String[] args) {
        Child child = new Child();
        child.displayGrandparent();
        child.displayParent();
        child.displayChild();
    }
}


