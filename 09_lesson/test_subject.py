import pytest

from  sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = create_engine(db_connection_string)

def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names() #список таблиц

    assert names[11] == 'subject'

def test_select():
    connection = db.connect()  # Создаем соединение
    rows = connection.execute(text("select * from subject s")) #строки таблицы

    assert len(rows) > 0

    connection.close()

def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("insert into subject (subject_title) values (:new_name)")
    rows = connection.execute(sql, {"new_name":"Arabian"})

    assert rows[15]["subject_title"] == "Arabian"

    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("update subject s set subject_id = '16' where s.subject_title = :subject")
    rows = connection.execute(sql,{"s.subject_title": 'Arabian'})

    assert rows[15]["subject_id"] == "16"

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("delete from subject where subject.subject_id = :id")
    rows = connection.execute(sql, {"id": 16})

    assert len(rows) == 0

    transaction.commit()
    connection.close()
