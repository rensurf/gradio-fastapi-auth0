import gradio as gr


class MainApplicationInterface:
    def __init__(self, demo_name: str = "demo"):
        self.demo_name = demo_name
        self.interface = self.build()

    def build(self):
        with gr.Blocks() as app_interface:
            gr.Markdown(f"# {self.demo_name}")
            with gr.Row():
                gr.Button("Logout", link="/logout", size="sm", variant="secondary")

            with gr.Tabs():
                with gr.TabItem("Tab 1"):
                    gr.Markdown("Content for Tab 1")
                with gr.TabItem("Tab 2"):
                    gr.Markdown("Content for Tab 2")

        return app_interface
