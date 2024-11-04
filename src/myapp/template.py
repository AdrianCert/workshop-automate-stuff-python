from pathlib import Path
from minijinja import Environment


class TemplateWorker:
    def __init__(self):
        self.env = Environment(self.loader)

    def loader(self, path: str):
        template_path = Path(__file__).parent / "template.html.jinja"
        return template_path.read_text()

    def render(self, **options):
        return self.env.render_template("_", **options)


if __name__ == "__main__":
    result = TemplateWorker().render(receiver_name="EU", sender_name="TOT EU")
    print(result)
