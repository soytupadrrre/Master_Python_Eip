import pathlib
import pygubu
try: 
    from .accuracy import AccuracyApp
    from .alldata import AllDataApp
    from .delete_last import DeleteLastApp
    from .delete import DeleteIdApp
    from .insert import InsertApp
    from .predict import PredictApp
    from .resume import ResumeApp
    from .update_last import UpdateLastApp
    from .update import UpdateIdApp
    from .flower import FlowerApp
except:
    from accuracy import AccuracyApp
    from alldata import AllDataApp
    from delete_last import DeleteLastApp
    from delete import DeleteIdApp
    from insert import InsertApp
    from predict import PredictApp
    from resume import ResumeApp
    from update_last import UpdateLastApp
    from update import UpdateIdApp
    from flower import FlowerApp

PROJECT_PATH = pathlib.Path(__file__).parent.parent.parent
PROJECT_UI = PROJECT_PATH / "resources" / "interface.ui"


class HomeApp:
    def __init__(self, master=None, project_path=PROJECT_PATH, project_ui=PROJECT_UI):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(project_path)
        builder.add_from_file(project_ui)
        self.mainwindow = builder.get_object("home", master)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def open_all_data_view(self):
        app = AllDataApp()
        app.run()

    def open_resume_view(self):
        app = ResumeApp()
        app.run()

    def open_accuracy_view(self):
        app = AccuracyApp()
        app.run()

    def open_flower_view(self):
        app = FlowerApp()
        app.run()

    def open_insert_data_view(self):
        app = InsertApp()
        app.run()

    def open_predict_data_view(self):
        app = PredictApp()
        app.run()

    def open_update_last_view(self):
        app = UpdateLastApp()
        app.run()

    def open_update_by_id_view(self):
        app = UpdateIdApp()
        app.run()

    def open_delete_last_view(self):
        app = DeleteLastApp()
        app.run()

    def open_delete_by_id_view(self):
        app = DeleteIdApp()
        app.run()


if __name__ == "__main__":
    app = HomeApp()
    app.run()

