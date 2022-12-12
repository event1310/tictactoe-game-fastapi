board = new Array("", "", "", "", "", "", "", "", "");
gamestatus = -1

function endGame() {
    for (let i=0;i<9;i++) {
    console.log('square-' + (i+1));
    let currElement = document.getElementById('square-' + (i+1));
        currElement.onClick = function() {};
      }
}

function checkGameStatus(gamestatus) {
    if (gamestatus != -1) {
        endGame();
        if (gamestatus == 0) {
            console.log("DRAW")
        return 0
        }
        else if (gamestatus == 10) {
        console.log("PLAYER")
        return 1
        }
        else if (gamestatus == -10) {
        console.log("AI")
        return 2
        }
    }
    else {
    return -1
    }
}

function makeMove(id) {
  gamestatus = checkGameStatus(gamestatus)
  console.log("gamestatus while entering the makemove function: " + gamestatus)

  if (gamestatus != -1) {
        return
  }
  let square_id = id.charAt(id.length - 1) // square_id is in range 1-9
  let array_field_id = (square_id)-1 // array_field_id is in range 0-8
  console.log("square_id is " + square_id)

  console.log("gamestatus before trying to place the mark: " + gamestatus)
  if (board[array_field_id] == "" && gamestatus == -1) {
    $('#' + id).html('<span class="fa fa-times"></span>')
    board[array_field_id] = "X"
    sendRequest(board, gamestatus)
  }
  if (board[array_field_id] == "X" || (board[array_field_id] == "O" &&  $('#' + id).html('<span class="fa fa-times" style="color:#06d458;"></span>').length))
  {
    console.log("its not empty")
  }
}

function updateBoard(newboard) {
    console.log("newboard is: " + newboard)
    for (let i=0;i<9;i++) {
      console.log("newboard[i] is: " + newboard[i])
      console.log(i)
      if ( newboard[i] == 'O' && gamestatus == -1) {
        $('#' + "square-" + (i+1)).html('<span class="fa fa-times" style="color:#06d458;"></span>')
        console.log("we have put it in : " + i)
      }
    }
}

function updateBoard2(data) {
    return data
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
    // Parse the JSON string to a JavaScript array
    console.log("text: " + text);
    received_board = JSON.parse(text)["board"];
    gamestatus = JSON.parse(text)["gamestatus"];
    board = updateBoard2(received_board)
    updateBoard(received_board);
    showBoard()
    if (checkGameStatus(gamestatus) != -1) {
        return
    }
  });
}

function showBoard() {
  console.log("board state: " + board) 

}