class Test():
    def __init__(self):
        self.date = UIData()
        self.date.set_btn_back_state(True).set_btn_cancel_match_state(True).set_light_state(True)
        print(self.date.btn_cancel_match_state)


class UIData():
    btn_back_state = True
    btn_cancel_match_state = False
    btn_goto_lobby = False
    light_state = False
    tex_1_str = ""
    tex_2_str = ""

    def set_btn_back_state(self, show):
        self.btn_back_state = show
        return self

    def set_btn_cancel_match_state(self, show):
        self.btn_cancel_match_state = show
        return self

    def set_btn_goto_lobby(self, show):
        self.btn_goto_lobby = show
        return self

    def set_light_state(self, show):
        self.light_state = show
        return self

    def set_tex_1_str(self, tex_str):
        self.tex_1_str = tex_str
        return self

    def set_tex_2_str(self, tex_str):
        self.tex_2_str = tex_str
        return self