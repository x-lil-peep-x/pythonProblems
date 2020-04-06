while True:
    try:
        chart_length = int(input())
        if chart_length > 2:
            print((chart_length*2)-2)
        else:
            print(chart_length)
    except:
        break
