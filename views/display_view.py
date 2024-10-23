from akari_client.color import Colors
from akari_client.position import Positions

def display_result(m5, player_hand, akari_hand, result):
    m5.set_display_text(
        text=f"あなたの手: {player_hand}",
        pos_x=Positions.CENTER,
        pos_y=30,
        size=2,
        text_color=Colors.RED,
        back_color=Colors.WHITE,
        refresh=False,
    )
    m5.set_display_text(
        text=f"Akariの手: {akari_hand}",
        pos_x=Positions.CENTER,
        pos_y=90,
        size=2,
        text_color=Colors.RED,
        back_color=Colors.WHITE,
        refresh=False,
    )
    m5.set_display_text(
        text=f"結果: {result}",
        pos_x=Positions.CENTER,
        pos_y=150,
        size=2,
        text_color=Colors.RED,
        back_color=Colors.WHITE,
        refresh=True,
    )

def display_countdown(m5, count):
    m5.set_display_text(
        text=f"じゃんけんスタートまで{count}秒",
        pos_x=Positions.CENTER,
        pos_y=Positions.CENTER,
        size=2,
        text_color=Colors.RED,
        back_color=Colors.WHITE,
        refresh=True,
    )
