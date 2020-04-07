// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function(){
    console.log(`The name "${this.name}" size is: ${this.name.length}`)
  }
}
employee.nameLength()

// Add a method called nameLength that prints out the
// length of the employees name to the console.


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}

// NA AULA ELE CRIOU UM METODO report: function(){aler...}
alert(`Name is ${employee.name}, Job is ${employee.job}, Age is ${employee.age}`)
// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.



///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function(){
    console.log(this.name.split(" ").pop());
    // COLOQUEI employee, DEVERIA TER COLOCADO this.
    //NA AULA COLOCOU .split(" ")[1] QUE SO SERVE PARA NOME COM 1 SOBRENOME
  }
}
employee.lastName()

// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
