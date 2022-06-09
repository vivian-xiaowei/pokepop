def find_length(ball_list, count, push):
    start, end = count, count
    while start > 0 and ball_list[start].type == ball_list[start - 1].type:
        start -= 1
    while end < len(ball_list) - 2 and ball_list[end].type == ball_list[end + 1].type:
        end += 1
    if end <= len(ball_list) - 2 and ball_list[end + 1].type == ball_list[count].type and end + 2 == len(ball_list):
        end += 2
    if count == len(ball_list) - 1 and ball_list[count].type == push:
        end += 1
    return start, end
