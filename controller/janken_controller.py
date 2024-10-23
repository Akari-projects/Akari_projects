import threading
import queue
from models.janken_model import judge, get_random_hand
from models.gesture_recognizer import recognize_gesture
from views.display_view import display_result, display_countdown

class JankenController:
    def __init__(self, m5):
        self.m5 = m5
        self.janken_in_progress = False
        self.result_queue = queue.Queue()

    def start_janken(self, gesture_result):
        if self.janken_in_progress:
            return

        self.janken_in_progress = True
        akari_hand = get_random_hand()
        threading.Thread(target=self._janken_sequence, args=(akari_hand, gesture_result)).start()

    def _janken_sequence(self, akari_hand, gesture_result):
        for i in range(3, 0, -1):
            display_countdown(self.m5, i)
            time.sleep(1)

        player_hand = recognize_gesture(gesture_result)
        result = judge(player_hand, akari_hand)
        display_result(self.m5, player_hand, akari_hand, result)
        
        self.janken_in_progress = False

    def get_result(self):
        if not self.result_queue.empty():
            return self.result_queue.get()
        return None
