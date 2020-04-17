// ARRAYS

var country1 = "USA";

var country2 = "Germany";

var country3 = "China";

var countries = ["USA", "Germany", "China"];

var countries2 = ["USA",
                  "Germany",
                  "China"];

// immutable - string
country1[2] = "B"
console.log(country1); // USA

//mutable - array
countries[2] = "Spain"
console.log(countries); // [ "USA", "Germany", "Spain" ]


var mixed = [true, 20, 'string'];
console.log(mixed.length); // 3


var myArr = ['one', 'two', 'trhee'];

//Remove item
var lastItem = myArr.pop();
console.log(lastItem);  // three
console.log(myArr);  // [ "one", "two" ]

//Add lastItem
myArr.push('new_item');
console.log(myArr); // [ "one", "two", "new_item" ]

//Index last item
console.log(myArr[myArr.length - 1]);  // new_item


// Array Iteration

var arr = ['A', 'B', 'C'];
for (var i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}

for (letter of arr) {  // letter become a temp variable
  console.log(letter);
}

for (letter of arr) {
  alert(letter);
}

arr.forEach(alert);

function addAwesome(name){
  console.log(name + 'is awesome!');
}
addAwesome('Django');

var topics = ['Python', 'Django', 'Science'];
topics.forEach(addAwesome);
