const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.username}</td>
            <td>{user.email}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return  (
        <table>
            <thead>
                <tr>
                    <th>username</th>
                    <th>email</th>
                    <th>first_name</th>
                    <th>last_name</th>
                </tr>
            </thead>
            <tbody>
            {users.map((user) => <UserItem user={user} />)}
            </tbody>
        </table>
    )
}

export default UserList;