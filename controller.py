import view as v
import calculator as cc


def button_click_complex():
    value_a = v.input_complex()
    value_b = v.input_complex()
    cc.calculator(value_a, value_b)


def button_click_rac():
    value_a = v.input_rac()
    value_b = v.input_rac()
    cc.calculator(value_a, value_b)
