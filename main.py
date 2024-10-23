from akari_client import AkariClient
from depthai_handface.HandFaceTracker import HandFaceTracker
from depthai_handface.HandFaceRenderer import HandFaceRenderer
from controller.janken_controller import JankenController

def main():
    akari = AkariClient()
    m5 = akari.m5stack
    tracker = HandFaceTracker(use_gesture=True)
    renderer = HandFaceRenderer(tracker=tracker)
    controller = JankenController(m5)

    while True:
        frame, _, hands = tracker.next_frame()
        if frame is None:
            break

        for hand in hands:
            gesture_result = hand.gesture
            if gesture_result:
                controller.start_janken(gesture_result)

        if renderer.waitKey(1) == ord('q'):
            break

    renderer.exit()
    tracker.exit()

if __name__ == "__main__":
    main()
