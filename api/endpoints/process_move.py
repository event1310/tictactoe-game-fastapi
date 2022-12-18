import json
from fastapi import APIRouter, Body
from api.backend import game

router = APIRouter()

@router.post("/move")
async def process_move(board = Body(...)):
    game_instance = game.TicTacToeGame()
    board_decoded = json.loads(board)
    print(f"board decoded: {board_decoded}")
    board_with_calculated_move = game_instance.make_move(board_decoded)
    board_with_calculated_move_to_json = json.dumps(board_with_calculated_move)
    print(f"board_with_calculated_move_to_json: {board_with_calculated_move_to_json}")
    print(f"{board_with_calculated_move_to_json}")
    return board_with_calculated_move_to_json





