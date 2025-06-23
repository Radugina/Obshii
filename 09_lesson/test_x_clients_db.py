from sqlalchemy import create_engine, text

db = create_engine("postgresql://postgres:1234@localhost:5433/postgres")


def test_create_students():
    connection = db.connect()
    сonnection.execute(text("select * from Student"))
    connection.close()

def test_create_subjects():
    connection = db.connect()
    max_id_result = connection.execute(
        text("SELECT MAX(subject_id) FROM subject")).fetchone()
    max_id = max_id_result[0] if max_id_result else 0
    new_id = (max_id or 0) + 1

    new_subject_title = 'Football'
    connection.execute(text(
        f""" INSERT INTO subject (subject_id, subject_title) VALUES ({new_id},
        '{new_subject_title}') """))

    fetched_subject = connection.execute(
        text(f"SELECT subject_title FROM subject WHERE subject_id={new_id}")
    ).fetchone()
    assert fetched_subject[0] == new_subject_title
    connection.close()


def test_update_subject_name():
    connection = db.connect()

    max_id_result = connection.execute(text(
        "SELECT MAX(subject_id) FROM subject")).fetchone()
    test_id = (max_id_result[0] or 0) + 1
    original_title = 'Football'

    connection.execute(text(
        f"INSERT INTO subject (subject_id, subject_title) VALUES ({test_id}, '{original_title}')"
    ))

    new_title = 'Baseball'
    connection.execute(text(
        f"UPDATE subject SET subject_title = '{new_title}' WHERE subject_id = {test_id}"
    ))

    result = connection.execute(text(
        f"SELECT subject_title FROM subject WHERE subject_id = {test_id}"
    )).fetchone()

    assert result is not None
    assert result[0] == new_title

    connection.execute(text(
        f"DELETE FROM subject WHERE subject_id = {test_id}"))


def test_delete_subject():
    connection = db.connect()
    max_id_result = connection.execute(text(
        "SELECT MAX(subject_id) FROM subject")).fetchone()
    max_id = max_id_result[0] if max_id_result else 0
    new_id = (max_id or 0) + 1

    new_subject_title = 'Biathlon'
    connection.execute(text(
        f""" INSERT INTO subject (subject_id, subject_title) VALUES (
    {new_id}, '{new_subject_title}') """))

    fetched_subject = connection.execute(text(
        f"SELECT subject_title FROM subject WHERE subject_id={new_id}")
    ).fetchone()
    assert fetched_subject[0] == new_subject_title

    delete_id = new_id
    connection.execute(text(
        f"DELETE FROM subject WHERE subject_id={delete_id}")
    )

    deleted_subject = connection.execute(text(
        f"SELECT * FROM subject WHERE subject_id={delete_id}")
    ).fetchone()
    assert deleted_subject is None
    connection.close()
