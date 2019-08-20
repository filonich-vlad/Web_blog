from src.models.user import User
from src.common.database import Database


def main():
    Database.initialize()
    user = User.get_by_email('filonich.v@')

    user.new_post("8c3644e7aa2a490a9e0c36b8b7279737", "Racism", "Racism is probably bad, yo know.")

    user.new_post("8c3644e7aa2a490a9e0c36b8b7279737", "Leninism", "Leninism in probably good, yo know.")


if __name__ == '__main__':
    main()
