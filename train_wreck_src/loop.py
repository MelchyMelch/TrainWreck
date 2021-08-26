def goto(file_stream, line_num):
    # M: This one might be trickier to implement separately...
    file_stream.seek(0)
    file_data = file_stream.readlines()[line_num:]
