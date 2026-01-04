print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3,)
keyboard.row_pins = (board.D6, board.D10, board.D9, board.D8,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    # Layer 0
    [KC.LCTRL(KC.P1), KC.LCTRL(KC.P2), KC.LCTRL(KC.P3), KC.NO,
     KC.LCTRL(KC.P4), KC.LCTRL(KC.P5), KC.LCTRL(KC.P6), KC.TT(1),
     KC.LCTRL(KC.DEL), KC.LCTRL(KC.END), KC.LCTRL(KC.PGDN), KC.TT(2),
     KC.LCTRL(KC.INS), KC.LCTRL(KC.HOME), KC.LCTRL(KC.PGUP), KC.TT(3)],
    # Layer 1
    [KC.LALT(KC.P1), KC.LALT(KC.P2), KC.LALT(KC.P3), KC.TT(0),
     KC.LALT(KC.P4), KC.LALT(KC.P5), KC.LALT(KC.P6), KC.NO,
     KC.LALT(KC.P7), KC.LALT(KC.P8), KC.LALT(KC.P9), KC.TT(2),
     KC.B, KC.NO, KC.NO, KC.TT(3)],
     # Layer 2
    [KC.NO, KC.NO, KC.NO, KC.TT(0),
    KC.NO, KC.NO, KC.NO, KC.TT(1),
    KC.NO, KC.NO, KC.NO, KC.NO,
    KC.C, KC.NO, KC.NO, KC.TT(3)],
    # Layer 3
    [KC.NO, KC.NO, KC.NO, KC.TT(0),
    KC.NO, KC.NO, KC.NO, KC.TT(1),
    KC.NO, KC.NO, KC.NO, KC.TT(2),
    KC.D, KC.NO, KC.NO, KC.NO]
]

if __name__ == '__main__':
    keyboard.go()
