from database import session, UserTg, Message, sa


def push_database(data: dict) -> tuple:
    user = create_user(user_id=str(data['chat']['id']))
    if not user:
        user = UserTg.where(user_id=str(data['chat']['id'])).first()
    create_message(
        user_id=str(data['chat']['id']),
        body=data.get('text', ''),
        branch=user.branch,
        usertg=user,
    )
    return user.branch, user.status


def create_user(**kwargs) -> bool:
    """
    Creates a new user by params in kwargs
    :param kwargs: <dict> kwargs['user_id'] , kwargs['branch'] and all columns in the table usertg
    :return: None or user object
    """
    assert kwargs.get('user_id'), f'This func requires `user_id` key in kwargs,' \
                                  f' because it will create user by this value. Received {kwargs}'
    try:
        user = UserTg.create(**kwargs)
        session.commit()
        return user
    except sa.exc.IntegrityError as _er:
        # print(f'Problem with `.commit()` or `.create()`. '
        #       f'There can be errors with your rows. Exception description {_er}')
        session.rollback()
        return None


def update_user_state(**kwargs):
    """
    Updates a new user by params in kwargs
    :param kwargs: <dict> kwargs['user_id'] , kwargs['branch'], kwargs['status'] and all columns in the table usertg
    :return: None
    """
    assert kwargs.get('user_id'), f'This func requires `user_id` key in kwargs,' \
                                  f' because it will select user by this value. Received {kwargs}'
    user = UserTg.where(user_id=kwargs['user_id']).first()
    if kwargs.get('branch'):
        user.branch = kwargs['branch']
    if kwargs.get('status'):
        user.status = kwargs['status']
    session.commit()


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
