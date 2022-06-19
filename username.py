"""
データ型:UseName
    属性:
        実際のユーザー名
    ルール:
        ユーザー名は4文字以上20文字以内である
    できること:
        ユーザー名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        # 4文字以上20文字内のチェック
        if not (4 <= len(name) <= 20):
            raise ValueError(f"#{name}はルール違反です")
        self.name = name

    def screen_name(self):
        return self.name.upper()


tanaka = UserName(name="tanaka")
# bob = UserName(name="Bob")

print(tanaka.screen_name())
# print(bob.name)
