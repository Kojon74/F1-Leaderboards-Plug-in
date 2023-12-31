import math
import ac

X_ROW_1 = 100
X_ROW_2 = 150
X_ROW_3 = 200
Y_COL_2 = 200
Y_COL_3 = 400

class LeaderboardsUI:
    def __init__(self, app_window, current_user, best_lap_time):
        ac.setSize(app_window, 900, 300)
        current_user_label = ac.addLabel(app_window, "{}".format(current_user))
        rival_lap_label = ac.addLabel(app_window, "Rival Lap")
        best_lap_label = ac.addLabel(app_window, "Best Lap")
        self.best_lap_time = ac.addLabel(app_window, self.ms_to_time_str(best_lap_time))
        self.best_lap_delta = ac.addLabel(app_window, "0")
        cur_lap_label = ac.addLabel(app_window, "Current Lap")
        self.cur_lap_time = ac.addLabel(app_window, "0:00.000")
        self.invalidated_label = ac.addLabel(app_window, "")

        ac.setFontColor(self.best_lap_delta, 1, 0, 0, 1)

        ac.setFontSize(current_user_label, 30)
        ac.setFontSize(rival_lap_label, 30)
        ac.setFontSize(best_lap_label, 30)
        ac.setFontSize(self.best_lap_time, 30)
        ac.setFontSize(self.cur_lap_time, 30)
        ac.setFontSize(self.best_lap_delta, 30)
        ac.setFontSize(cur_lap_label, 30)
        ac.setFontSize(self.invalidated_label, 30)

        ac.setPosition(cur_lap_label, 0, X_ROW_1)
        ac.setPosition(self.cur_lap_time, Y_COL_2, X_ROW_1)
        ac.setPosition(self.invalidated_label, Y_COL_3, X_ROW_1)
        ac.setPosition(current_user_label, 0, 50)
        ac.setPosition(rival_lap_label, 0, X_ROW_3)
        ac.setPosition(best_lap_label, 0, X_ROW_2)
        ac.setPosition(self.best_lap_time, Y_COL_2, X_ROW_2)
        ac.setPosition(self.best_lap_delta, Y_COL_3, X_ROW_2)

    def update_delta(self, delta):
        delta_str = round(delta)/1000
        ac.setText(self.best_lap_delta, "{}".format(delta_str))
        color = [0, 1, 0, 1] if delta < 0 else [1, 0, 0, 1]
        ac.setFontColor(self.best_lap_delta, *color)

    def update_lap_time(self, lap_time):
        lap_time_str = self.ms_to_time_str(lap_time)
        ac.setText(self.cur_lap_time, lap_time_str)

    def update_invalidated(self, invalidated):
        ac.setText(self.invalidated_label, "INVALIDATED" if invalidated else "")

    def update_best_lap_time(self, best_lap_time):
        best_lap_time_str = self.ms_to_time_str(best_lap_time)
        ac.setText(self.best_lap_time, best_lap_time_str)

    def ms_to_time_str(self, ms):
        time_str = "{}:{}.{}".format(math.floor(ms/60000), "{}".format(math.floor(ms/1000) % 60).zfill(2), "{}".format(ms%1000).zfill(3))
        return time_str
