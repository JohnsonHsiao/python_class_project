from telegram import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters
import random

class Othello:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3] = '⚫'
        self.board[3][4] = '⚪'
        self.board[4][3] = '⚪'
        self.board[4][4] = '⚫'
        self.current_player = '⚫'

    def get_board_markup(self):
        keyboard = [[InlineKeyboardButton(self.board[i][j], callback_data=f'{i}-{j}') for j in range(8)] for i in range(8)]
        return InlineKeyboardMarkup(keyboard)

    
    def make_move(self, row: int, col: int, color: str):
        self.board[row][col] = color
        self.flip_pieces(row, col, color)
    
    def flip_pieces(self, row: int, col: int, color: str):
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            x, y = row + dx, col + dy
            if self.is_inside_board(x, y) and self.board[x][y] == ('⚫' if color == '⚪' else '⚪'):
                pieces_to_flip = []
                while self.is_inside_board(x, y) and self.board[x][y] != ' ':
                    if self.board[x][y] == color:
                        break
                    pieces_to_flip.append((x, y))
                    x, y = x + dx, y + dy
            else:
                pieces_to_flip = []

            if self.is_inside_board(x, y) and self.board[x][y] == color:
                for rx, ry in pieces_to_flip:
                    self.board[rx][ry] = color

    def is_inside_board(self, row: int, col: int) -> bool:
        return 0 <= row < 8 and 0 <= col < 8
    
    def make_random_move(self):
        empty_cells = [(i, j) for i in range(8) for j in range(8) if self.is_valid_move(i, j, '⚪')]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = '⚪'
            self.flip_pieces(i, j, '⚪')
            self.current_player = '⚫'
        else:
            self.current_player = '⚫'

    def is_valid_move(self, row: int, col: int, color: str) -> bool:
            if self.board[row][col] != ' ':
                return False

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                x, y = row + dx, col + dy
                if self.is_inside_board(x, y) and self.board[x][y] == ('⚫' if color == '⚪' else '⚪'):
                    while self.is_inside_board(x, y) and self.board[x][y] != ' ':
                        if self.board[x][y] == color:
                            return True
                        x, y = x + dx, y + dy
            return False

    def is_valid_move_any(self, color: str) -> bool:
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(i, j, color):
                    return True
        return False

    def is_game_over(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def count_pieces(self):
        black_count = 0
        white_count = 0
        for row in self.board:
            for piece in row:
                if piece == '⚫':
                    black_count += 1
                elif piece == '⚪':
                    white_count += 1
        return black_count, white_count

game = None

async def start(update, context):
    user = update.effective_user
    await update.message.reply_text("你好，請輸入 /game_start 開始遊戲")

async def game_start(update, context):
    global game
    game = Othello()
    await update.message.reply_text('遊戲開始！', reply_markup=game.get_board_markup())

async def handle_move(update, context):
    global game
    if game is None:
        await update.message.reply_text('No game in progress. Start a new game with /game_start.')
        return
    query = update.callback_query
    row, col = map(int, query.data.split('-'))
    if game.is_valid_move(row, col, '⚫'):
        game.make_move(row, col, '⚫')
        game.make_random_move()
        await query.edit_message_text('Board:', reply_markup=game.get_board_markup())
        if game.is_game_over():
            black_count, white_count = game.count_pieces()
            result_message = f"遊戲結束！黑子數量：{black_count}，白子數量：{white_count}"
            if black_count > white_count:
                result_message += "，黑子勝利！"
            elif black_count < white_count:
                result_message += "，白子勝利！"
            else:
                result_message += "，平局！"
            await query.message.reply_text(result_message)
    elif not game.is_valid_move(row, col, '⚫'):
        if not game.is_valid_move_any('⚫'):
            game.make_random_move()
        if not game.is_valid_move_any('⚫') and not game.is_valid_move_any('⚪'):
            black_count, white_count = game.count_pieces()
            result_message = f"遊戲結束！黑子數量：{black_count}，白子數量：{white_count}"
            if black_count > white_count:
                result_message += "，黑子勝利！"
            elif black_count < white_count:
                result_message += "，白子勝利！"
            else:
                result_message += "，平局！"
            await query.message.reply_text(result_message)
            return
        await query.answer('Invalid move. 請重新選擇下子位置')
        return
    else:
        await query.answer('Invalid move. 請重新選擇下子位置')

    


def main():
    application = Application.builder().token("6285139779:AAFNENxs_yVb5BU0OI2HClCBl0JCp56uyek").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("game_start", game_start))
    application.add_handler(CallbackQueryHandler(handle_move))

    application.run_polling()

if __name__ == "__main__":
    main()