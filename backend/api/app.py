from connexion import App


app = App(__name__, specification_dir="./")
app.add_api("api-spec.yml")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
