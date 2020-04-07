// Nao fiz
var restart = document.querySelector("#b");

// Fiz, so usei nome da variavel one
var squares = document.querySelectorAll('td')

// play = "X"

// Não Fiz
function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = "";
  }
}

// Nao fiz
restart.addEventListener('click', clearBoard);

// Outro metodo - Generico
function changeMarker(){
  if (this.textContent === '') {
    this.textContent = 'X'
  }else if (this.textContent === 'X') {
    this.textContent = 'O'
  }else{
    this.textContent = ''
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click', changeMarker);
}




// var cellOne = document.querySelector('#one');
//
// // Mudei o nome da variavel e usei um else if no final
// cellOne.addEventListener("click", function(){
//
//   if (cellOne.textContent === ""){
//     cellOne.textContent = "X";
//   }else if (cellOne.textContent==="X") {
//     cellOne.textContent = "O";
//   }else {
//     cellOne.textContent = "";
//   }
// });


// Mudei o nome da variavel e usei um else if no final
// one.addEventListener("click", function(){
//
//   if (one.textContent === " "){
//     one.textContent = "X";
//   }else if (one.textContent==="X") {
//     one.textContent = "O";
//   }else if (one.textContent==="O") {
//     one.textContent = " ";
//
//   }
// })
