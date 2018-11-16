from database import session, UserTg, Message, sa


def push_database(data: dict):
    user = create_user(user_id=str(data['chat']['id']))
    if not user:
        user = UserTg.where(user_id=str(data['chat']['id'])).first()
    create_message(
        user_id=str(data['chat']['id']),
        body=data.get('text', ''),
        usertg=user,
    )
    return user.step


def update_user_step(**kwargs):
    """
    Updates a new user by params in kwargs
    :param kwargs: <dict> kwargs['user_id'] , kwargs['step'] and all columns in the table usertg
    :return: None
    """
    assert kwargs.get('user_id'), f'This func requires `user_id` key in kwargs,' \
                                  f' because it will select user by this value. Received {kwargs}'
    user = UserTg.where(user_id=kwargs['user_id']).first()
    if kwargs.get('step'):
        user.step = kwargs['step']
        session.commit()


def create_user(**kwargs):
    """
    Creates a new user by params in kwargs
    :param kwargs: <dict> kwargs['user_id'] and all columns in the table usertg
    :return: None or user object
    """
    assert kwargs.get('user_id'), f'This func requires `user_id` key in kwargs,' \
                                  f' because it will create user by this value. Received {kwargs}'
    try:
        user = UserTg.create(**kwargs)
        session.commit()
        return user
    except sa.exc.IntegrityError as _er:
        session.rollback()
        return


def create_message(user_id: str, **kwargs):
    """
    Creates a new message by params in kwargs
    :param user_id: <str> Telegram user_id
    :param kwargs: <dict> kwargs with all columns in the table message
    :return: None
    """
    user = UserTg.where(user_id=user_id).first()
    kwargs['usertg'] = user
    _msg = Message.create(**kwargs)
    session.commit()
