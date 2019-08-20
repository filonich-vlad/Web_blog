from src.models.user import User
from src.common.database import Database


def main():
    Database.initialize()
    user = User.get_by_email('filonich.v@')

    user.new_blog(title='Power is everything',
                  description='Heihachi')


if __name__ == '__main__':
    main()
