def sort_rectangles(rectangle_records, record_title):
    for i in range(1, len(rectangle_records)):
        X = rectangle_records[i]
        j = i - 1
        while j >= 0 and X[record_title] < rectangle_records[j][record_title]:
            rectangle_records[j + 1] = rectangle_records[j]
            j -= 1
        rectangle_records[j + 1] = X
    return rectangle_records


# #Data
# rectangle_records = [{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}]

# #Function Call
# print(sort_rectangles(rectangle_records, "ID"))

# #Expected output
# [{"ID": "Rect1", "Length": 40, "Breadth": 25, "Color": "red"}, {"ID": "Rect2", "Length": 30, "Breadth": 20, "Color": "blue"}, {"ID": "Rect3", "Length": 70, "Breadth": 45, "Color": "green"}, {"ID": "Rect4", "Length": 20, "Breadth": 10, "Color": "purple"}]