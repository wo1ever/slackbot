from chatlogic import reply


print("불렀어?" == reply("애란"))
print(
    {
        "주사위를 던졌더니 1 나왔다.",
        "주사위를 던졌더니 2 나왔다.",
        "주사위를 던졌더니 3 나왔다.",
        "주사위를 던졌더니 4 나왔다.",
        "주사위를 던졌더니 5 나왔다.",
        "주사위를 던졌더니 6 나왔다.",
    } == {reply("주사위") for _ in range(1000)}
)
