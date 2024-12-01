import gradio as gr


class LoginInterface:
    def __init__(self):
        self.interface = self.build()

    def build(self):
        with gr.Blocks() as login_interface:
            gr.Markdown("# Login")
            with gr.Row():
                gr.Markdown(
                    "Welcome! Please click the button below to login with Auth0"
                )

            gr.Button(
                "Login with Auth0",
                link="/login",
                size="lg",
                variant="primary",
                elem_classes="btn-block",
            )

        return login_interface
