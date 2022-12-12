import json
from fastapi import APIRouter, Body
import sys
sys.path.append("..")
from api.backend.game import make_move, handle_game

router = APIRouter()

@router.post("/move")
async def process_move(board = Body(...)):
    board_decoded = json.loads(board)
    board_with_calculated_move = make_move(board_decoded)
    board_with_calculated_move_to_json = json.dumps(board_with_calculated_move)
    #gamestatus_to_json = json.dumps(board_with_calculated_move["gamestatus"])
    #print(f"gamestatus: {board_with_calculated_move_to_json[1]}")
    print(f"{board_with_calculated_move_to_json}")
    return board_with_calculated_move_to_json





