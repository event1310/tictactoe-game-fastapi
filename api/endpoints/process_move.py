import json
from fastapi import APIRouter, Body
import sys
sys.path.append("..")
from api.backend.game import TicTacToeGame

router = APIRouter()

@router.post("/move")
async def process_move(board = Body(...)):
    game_instance = TicTacToeGame()
    board_decoded = json.loads(board)
    board_with_calculated_move = game_instance.make_move(board_decoded)
    board_with_calculated_move_to_json = json.dumps(board_with_calculated_move)
    print(f"{board_with_calculated_move_to_json}")
    return board_with_calculated_move_to_json





