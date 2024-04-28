def solution(queries):
    text = ""
    cursor_pos = 0
    selected_start = None
    selected_end = None
    clipboard = ""

    def insert_text(input_text):
        nonlocal text, cursor_pos
        if has_selection():
            delete_selection()
        text = text[:cursor_pos] + input_text + text[cursor_pos:]
        cursor_pos += len(input_text)

    def set_selection(start, end):
        nonlocal selected_start, selected_end, cursor_pos
        selected_start = max(0, min(start, len(text))
        selected_end = max(0, min(end, len(text))
        cursor_pos = selected_end

    def move_cursor(position):
        nonlocal cursor_pos
        cursor_pos = max(0, min(position, len(text))

    def remove_character():
        nonlocal text, cursor_pos
        if cursor_pos > 0:
            if has_selection():
                delete_selection()
            else:
                text = text[:cursor_pos - 1] + text[cursor_pos:]
                cursor_pos -= 1

    def copy_to_clipboard():
        nonlocal clipboard
        if has_selection():
            clipboard = text[selected_start:selected_end]

    def paste_from_clipboard():
        nonlocal text, cursor_pos
        if clipboard:
            if has_selection():
                delete_selection()
            text = text[:cursor_pos] + clipboard + text[cursor_pos:]
            cursor_pos += len(clipboard)

    def delete_selection():
        nonlocal text, cursor_pos, selected_start, selected_end
        text = text[:selected_start] + text[selected_end:]
        cursor_pos = selected_start
        selected_start = None
        selected_end = None

    def has_selection():
        return selected_start is not None and selected_end is not None

    result = []
    for query in queries:
        operation = query[0]
        if operation == "INSERT":
            insert_text(query[1])
        elif operation == "SELECT":
            set_selection(int(query[1]), int(query[2]))
        elif operation == "MOVE":
            move_cursor(int(query[1]))
        elif operation == "REMOVE":
            remove_character()
        elif operation == "COPY":
            copy_to_clipboard()
        elif operation == "PASTE":
            paste_from_clipboard()
        result.append(text)

    return result
