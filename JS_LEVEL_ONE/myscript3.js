var x = 0;

while (x < 5) {
  console.log('x is currently: ' + x);

  if (x === 3) {
    console.log('X IS EQUAL TO THREE!');
    break;
  }
  console.log('x is still less than 5, adding 1 to x');

  x += 1
}

var even = 0

while (even <= 10) {
  if (even % 2 == 0) {
    console.log(even);
    }
      even +=1
}
