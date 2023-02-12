namespace cpp match_service

struct User {
    1: i32 id,
    2: string name,
    3: i32 score
}

service Match {
    # 向匹配池添加玩家
    i32 add_user(1: User user, 2: string info),

    # 向匹配池删除玩家
    i32 remove_user(1: User user, 2: string info),
}
