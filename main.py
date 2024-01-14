from crossmodules.connections.database import DatabaseTest


def get_user_by_id(user_id: int):
    query: str = 'SELECT user_id, username, email FROM users WHERE user_id = ?'
    parameters = (user_id,)
    return DatabaseTest.select_data(query, parameters)


if __name__ == '__main__':
    # Example usage for retrieving products by user ID:
    user_id_to_retrieve = 1
    user_data = get_user_by_id(user_id_to_retrieve)
    print(f"Products Data for User ID {user_id_to_retrieve}: {user_data}")
