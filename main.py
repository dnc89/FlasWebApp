from website import create_app

app = create_app()
print("starting")
if __name__ == "__main__":
    app = create_app()
    print("starting the webserver")
    app.run(debug=False, port=5000)


