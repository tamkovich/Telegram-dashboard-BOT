from database import session, UserTg, Message, engine, sa


def test_create_user():
    try:
        _bob = UserTg.create(user_id='20490124')
        session.commit()
    except sa.exc.IntegrityError as _er:
        print(f'Problem with `.commit()` or `.create()`. '
              f'There can be errors with your rows. Exception description {_er}')


def test_create_message():
    bob = UserTg.where(user_id='20490124').first()
    _msg = Message.create(body='Привет Мир!', usertg=bob, branch='dec5')
    session.commit()


def test_update_user():
    bob = UserTg.where(user_id='20490124').first()
    bob.branch = 'licvidation'
    session.commit()


def test_update_message():
    bob = Message.query.first()
    bob.branch = 'licvidation'
    session.commit()


def test_add_column(table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))


def test_alter_user():
    columns = list()
    columns.append(sa.Column('branch', sa.String(30)))
    columns.append(sa.Column('status', sa.Integer))
    for column in columns:
        test_add_column(UserTg.__tablename__, column)


def test_alter_message():
    columns = list()
    columns.append(sa.Column('branch', sa.String(30)))
    for column in columns:
        test_add_column(Message.__tablename__, column)


def test_clear_tables():
    """
    use it ONLY for test reason.
    Be carefully! Here is better way to destroy this func, than to use it.
    :return: None
    """
    Message.query.delete()
    UserTg.query.delete()
    session.commit()


if __name__ == '__main__':
    test_create_user()
