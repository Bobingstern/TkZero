"""
Generate event sequences for key combos
"""

import tkinter as tk
from typing import Union

from TkZero import Platform


def generate_event_sequence(
    widget: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    ctrl_cmd: bool,
    ctrl_ctrl: bool,
    shift_shift: bool,
    alt_option: bool,
    letter: str,
) -> str:
    """
    Generate an event sequence you can pass in to bind_to_event on a widget
    from a key combo.

    :param widget: A Tkinter thing that we need to use so we can call into Tk.
     (Probably something like root or self)
    :param ctrl_cmd: Require control (command for macOS) to be pressed for the
     event. A bool.
    :param ctrl_ctrl: Require control (all platforms) to be pressed for the
     event. ctrl_cmd and ctrl_ctrl do the same thing on win32 and x11. A bool.
    :param shift_shift: Require shift (all platforms) to be pressed for the
     event. A bool.
    :param alt_option: Require alt (option for macOS) to be pressed for the
     event. A bool.
    :param letter: The letter to be pressed along with the modifier keys. A
     str. Must be one character long.
    :return: A str which is the not-so-human-friendly event sequence which
     you can pass into the bind_to_event on a widget.
    """
    if not isinstance(widget, (tk.Widget, tk.Tk, tk.Toplevel)):
        raise TypeError(
            f"widget is not a Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]! "
            f"(type passed in: {repr(type(widget))})"
        )
    if not isinstance(ctrl_cmd, bool):
        raise TypeError(
            f"ctrl_cmd is not a bool! (type passed in: {repr(type(ctrl_cmd))})"
        )
    if not isinstance(ctrl_ctrl, bool):
        raise TypeError(
            f"ctrl_ctrl is not a bool! " f"(type passed in: {repr(type(ctrl_ctrl))})"
        )
    if not isinstance(shift_shift, bool):
        raise TypeError(
            f"shift_shift is not a bool! "
            f"(type passed in: {repr(type(shift_shift))})"
        )
    if not isinstance(alt_option, bool):
        raise TypeError(
            f"alt_option is not a bool! " f"(type passed in: {repr(type(alt_option))})"
        )
    if not isinstance(letter, str):
        raise TypeError(f"letter is not a str! (type passed in: {repr(type(letter))})")
    sequence = "<"
    if Platform.on_aqua(widget):
        if ctrl_cmd:
            sequence += "Command-"
        if alt_option:
            sequence += "Option-"
    else:
        if ctrl_cmd:
            sequence += "Control-"
        if alt_option:
            sequence += "Alt-"
    if ctrl_ctrl and "Control-" not in sequence:
        sequence += "Control-"
    if shift_shift:
        sequence += "Shift-"
    sequence += letter[0].upper() if shift_shift else letter[0].lower()
    sequence += ">"
    return sequence


def generate_accelerator_sequence(
    widget: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    ctrl_cmd: bool,
    ctrl_ctrl: bool,
    shift_shift: bool,
    alt_option: bool,
    letter: str,
) -> str:
    """
    Generate an accelerator sequence you can display in menus.

    :param widget: A Tkinter thing that we need to use so we can call into Tk.
     (Probably something like root or self)
    :param ctrl_cmd: Require control (command for macOS) to be pressed for the
     event. A bool.
    :param ctrl_ctrl: Require control (all platforms) to be pressed for the
     event. ctrl_cmd and ctrl_ctrl do the same thing on win32 and x11. A bool.
    :param shift_shift: Require shift (all platforms) to be pressed for the
     event. A bool.
    :param alt_option: Require alt (option for macOS) to be pressed for the
     event. A bool.
    :param letter: The letter to be pressed along with the modifier keys. A
     str. Must be one character long.
    :return: A str of the accelerator.
    """
    if not isinstance(widget, (tk.Widget, tk.Tk, tk.Toplevel)):
        raise TypeError(
            f"widget is not a Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]! "
            f"(type passed in: {repr(type(widget))})"
        )
    if not isinstance(ctrl_cmd, bool):
        raise TypeError(
            f"ctrl_cmd is not a bool! (type passed in: {repr(type(ctrl_cmd))})"
        )
    if not isinstance(ctrl_ctrl, bool):
        raise TypeError(
            f"ctrl_ctrl is not a bool! " f"(type passed in: {repr(type(ctrl_ctrl))})"
        )
    if not isinstance(shift_shift, bool):
        raise TypeError(
            f"shift_shift is not a bool! "
            f"(type passed in: {repr(type(shift_shift))})"
        )
    if not isinstance(alt_option, bool):
        raise TypeError(
            f"alt_option is not a bool! " f"(type passed in: {repr(type(alt_option))})"
        )
    if not isinstance(letter, str):
        raise TypeError(f"letter is not a str! (type passed in: {repr(type(letter))})")
    sequence = ""
    if ctrl_cmd:
        sequence += "Command-" if Platform.on_aqua(widget) else "Control-"
    if ctrl_ctrl:
        if "Control-" in sequence:
            raise ValueError(
                "ctrl_cmd and ctrl_ctrl is True and " "we are not on Aqua!"
            )
        else:
            sequence += "Control-"
    if shift_shift:
        sequence += "Shift-"
    if alt_option:
        sequence += "Option-" if Platform.on_aqua(widget) else "Alt-"
    sequence += letter[0].upper()
    if not Platform.on_aqua(widget):
        sequence = sequence.replace("-", "+")
    return sequence
