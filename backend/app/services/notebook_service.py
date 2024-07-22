from app.models import db, Notebook


def add_notebook(data):
    model = data.get("model")
    notebook = Notebook(model=model)
    db.session.add(notebook)
    db.session.commit()
    return notebook.to_dict(), 200
