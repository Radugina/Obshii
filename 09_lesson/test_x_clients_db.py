from sqlalchemy import create_engine

db = create_engine("postgresql://postgres:1234@localhost:5433/postgres")


def test_create_students():
    connection = db.connect()
    connection.execute("select * from student")


def test_create_subjects():
    connection = db.connect()
    max_id = connection.execute(
        "SELECT MAX(subject_id) FROM subject").fetchone()[0]
    new_id = max_id + 1 if max_id else 1

    new_subject_title = 'Football'
    connection.execute(
        f""" INSERT INTO subject (subject_id, subject_title) VALUES ({new_id},
        '{new_subject_title}') """)

    fetched_subject = connection.execute(
        f"SELECT subject_title FROM subject WHERE subject_id={new_id}"
    ).fetchone()
    assert fetched_subject[0] == new_subject_title


def test_update_subject_name():
    connection = db.connect()
    new_id = connection.execute(
        "SELECT COUNT(*) FROM subject").fetchone()[0]
    subject_title = 'Football'
    new_subject_title = 'Baseball'
    connection.execute(
        " ALTER subjects RENAME COLUMN subject_title TO new_subject_title")
    fetched_subject = connection.execute(
        "SELECT COUNT(*) FROM subject").fetchone()[0]
    assert fetched_subject[0] == new_subject_title


def test_delete_subject():
    connection = db.connect()
    max_id = connection.execute(
        "SELECT MAX(subjekt_id) FROM subject").fetchone()[0]
    new_id = max_id + 1 if max_id else 1

    new_subject_title = 'Biathlon'
    connection.execute(
        f""" INSERT INTO subject (subject_id, subject_title) VALUES (
        {new_id}, '{new_subject_title}') """)

    fetched_subject = connection.execute(
        f"SELECT subject_title FROM subject WHERE subject_id={new_id}"
    ).fetchone()
    assert fetched_subject[0] == new_subject_title

    delete_id = new_id
    deleted_subject = connection.execute(
        f"DELETE FROM subject WHERE subject_id={delete_id}"
    ).fetchone()
    assert deleted_subject is None
