// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name) {
  roster.push(name);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function remove(name) {
  for (var i = 0; i < name.length; i++) {
    if (roster[i] === name) {
      delete roster[i];
      // SOLUCAO DO EXERCICIO
      // var index = roster.indexOf(name);
      // roster.splice(index,1)

    }
  }
}

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display(){
  for (r of roster) {
    console.log(r);
    // SOLUCAO DO EXERCICIO
    // console.log(roster);
  }
}

// Start by asking if they want to use the web app
var name = ''
var resp = prompt('Would you like to start the roster web app? y/n ');
if (resp==='y') {
      while (resp==='y') {
        var option = prompt('Type a option \n1 - Add Student\n2 - Remove Student\n3 - List Students\n4 - Exit');
        if (option==='1') {
          name = prompt('Type the name of Student: ');
          addNew(name);
        }else if (option==='2') {
          name = prompt('Type the name of Student: ');
          remove(name);
        }else if (option==='3') {
          display()
        }else if (option==='4') {
          resp = 'n'
        }
      }
  }
confirm('Adios!')

// SOLUCAO DO EXERCICIO
// if (start === "y") {
//   while (request !== "quit") {
//     request = prompt("Please select an action: add, remove, display, or quit.")
//     if (request === "add") {
//       addNew();
//     }else if (request === "display") {
//       display();
//     }else if (request == "remove") {
//       remove();
//     }
//   }
// }

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
