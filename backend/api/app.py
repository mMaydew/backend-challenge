from connexion import App


app = App(
    __name__,
    specification_dir="./",
    options={"swagger_ui": True},
)
app.add_api("./api-spec.yml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
