import gradio as gr


class LogoutInterface:
    def __init__(self):
        self.interface = self.build()

    def build(self):
        with gr.Blocks() as logout_interface:
            gr.Markdown("# Logged Out")
            gr.Markdown("You have been successfully logged out.")

            gr.Button(
                "Return to Login",
                link="/",
                size="lg",
                variant="primary",
                elem_classes="btn-block",
            )

        return logout_interface
