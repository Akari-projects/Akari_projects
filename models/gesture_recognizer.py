def recognize_gesture(gesture_result):
    if gesture_result == "FIST":
        return "グー"
    elif gesture_result == "PEACE":
        return "チョキ"
    elif gesture_result == "FIVE":
        return "パー"
    return None
