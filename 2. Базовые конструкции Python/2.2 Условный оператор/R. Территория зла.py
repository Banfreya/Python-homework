first_triangle_side = int(input())
second_triangle_side = int(input())
third_triangle_side = int(input())
squared_fts = first_triangle_side ** 2
squared_sts = second_triangle_side ** 2
squared_tts = third_triangle_side ** 2
if squared_fts + squared_sts == squared_tts \
    or squared_fts + squared_tts == squared_sts \
        or squared_tts + squared_sts == squared_fts:
    print("100%")
elif squared_fts + squared_sts < squared_tts \
    or squared_fts + squared_tts < squared_sts \
        or squared_tts + squared_sts < squared_fts:
    print("велика")
else:
    print("крайне мала")
