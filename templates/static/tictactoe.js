board = new Array("", "", "", "", "", "", "", "", "");
let gamestatus = -1
let isWaiting = 0;


function updateBoard(newboard) {
    for (let i=0;i<9;i++) {
      if ( newboard[i] == 'O' && gamestatus == -1) {
        $('#' + "square-" + (i+1)).html('<span class="fa-regular fa-circle" style="color:#e92626;"></span>')
      }
    }
}

function showBoard() {
  console.log("board state: " + board)
}

function showWinner(winner) {
    let endGameHeader = document.createElement("h4");
    let winningText = document.createTextNode(`${winner} won!`);
    let drawText = document.createTextNode("It's a DRAW!");
    endGameHeader.appendChild(winner === "DRAW" ? drawText : winningText);
    document.body.appendChild(endGameHeader);
    endGameHeader.classList.add("endgameheader");
}

function checkGameStatus(gamestatus) {
    if (gamestatus != -1) {

        if (gamestatus == 0) {
            showWinner("DRAW");
            return 0
        }
        else if (gamestatus == 99999) {
            showWinner("PLAYER");
            return 1
        }
            else if (gamestatus == -99999) {
            showWinner("AI")
            return 2
        }
    }
    return -1
}

function makeMove(id) {
  if (isWaiting == 0) {
      gamestatus = checkGameStatus(gamestatus)

      if (gamestatus != -1) {
            return
      }
      let square_id = id.charAt(id.length - 1) // square_id is in range 1-9
      let array_field_id = (square_id)-1 // array_field_id is in range 0-8

      if (board[array_field_id] == "" && gamestatus == -1) {
        $('#' + id).html('<span class="fa fa-times" style="color:#4ea54e;"></span>')
        board[array_field_id] = "X"
        isWaiting = 1;
        sendRequest(board, gamestatus)
      }
      if (board[array_field_id] == "X" || (board[array_field_id] == "O" &&  $('#' + id).html('<span class="fa-regular fa-circle" style="color:#e92626;"></span>').length))
      {
        console.log("its not empty")
      }
      }
}

function sendRequest(currboard, gamestatus) {
  gamestatus = checkGameStatus(gamestatus)
  if (gamestatus != -1) {
    return
  }
  const url = "move"

  fetch(url, {
    method: 'POST',
    body: JSON.stringify(currboard)
  })
  .then(response => response.json())
  .then(text => {
    gamestatus = checkGameStatus(gamestatus)
    if (gamestatus != -1) {
        return
    }
    board = JSON.parse(text)["board"];
    gamestatus = JSON.parse(text)["gamestatus"];
    updateBoard(board);
    showBoard()
    if (checkGameStatus(gamestatus) != -1) {
        return
    }
    isWaiting = 0;
  });
}