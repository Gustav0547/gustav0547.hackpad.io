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
    [KC.TO(1), KC.TO(2), KC.TO(3), KC.LCTRL(KC.INS),
     KC.LCTRL(KC.P1), KC.LCTRL(KC.P2), KC.LCTRL(KC.P3), KC.LCTRL(KC.HOME),
     KC.LCTRL(KC.P4), KC.LCTRL(KC.P5), KC.LCTRL(KC.P6), KC.LCTRL(KC.PGUP),
     KC.LCTRL(KC.DEL), KC.LCTRL(KC.END), KC.LCTRL(KC.PGDN), KC.TO(0)],
    # Layer 1
    [KC.TO(1), KC.TO(2), KC.TO(3), KC. LCTRL(KC.P7),
     KC.LALT(KC.P1), KC.LALT(KC.P2), KC.LALT(KC.P3), KC.LCTRL(KC.P8),
     KC.LALT(KC.P4), KC.LALT(KC.P5), KC.LALT(KC.P6), KC.LCTRL(KC.P9),
     KC.LALT(KC.P7), KC.LALT(KC.P8), KC.LALT(KC.P9), KC.TO(0)],
     # Layer 2
    [KC.TO(1), KC.TO(2), KC.TO(3), KC.L,
     KC.T, KC.Y, KC.U, KC.N,
     KC.I, KC.O, KC.P, KC.M,
     KC.H, KC.J, KC.K, KC.TO(0)],
    # Layer 3
    [KC.TO(1), KC.TO(2), KC.TO(3), KC.F22,
    KC.F13, KC.F14, KC.F15, KC.F23,
    KC.F16, KC.F17, KC.F18, KC.F24,
    KC.F19, KC.F20, KC.F21, KC.TO(0)]
]

if __name__ == '__main__':
    keyboard.go()
