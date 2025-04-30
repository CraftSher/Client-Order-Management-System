# def user_name_raport(data):
#     finish_list = []
#     for name, comments in data.items():
#         if comments['name'] == 'Alice':
#             result = (comments['name'], comments["comments"])
#             finish_list.append(result)
#     return finish_list
#
# data = {
#     "user1": {
#         "name": "Alice",
#         "comments": [
#             {"comment": "Great job!", "date": "2025-04-01"},
#             {"comment": "Very helpful!", "date": "2025-04-02"}
#         ]
#     },
#     "user2": {
#         "name": "Bob",
#         "comments": [
#             {"comment": "Nice work!", "date": "2025-04-03"},
#         ]
#     }
# }
# reports = user_name_raport(data)
# for name, comments in reports:
#     print(f'Комментарии от {name}:')
#     for comment in comments:
#         print(f"- {comment['comment']} ({comment['date']})")
#---------------------------------------------------------------

# def user_name_raport(data):
#     finish_list = []
#     for user_name, user_comments in data.items():
#         name = user_comments['name']
#         comments = user_comments['comments']
#         for comment in comments:
#             if comment["date"] > '2025-04-01':
#                 result = (name, comment['comment'], comment['date'])
#                 finish_list.append(result)
#     return finish_list
#
# data = {
#     "user1": {
#         "name": "Alice",
#         "comments": [
#             {"comment": "Great job!", "date": "2025-04-01"},
#             {"comment": "Very helpful!", "date": "2025-04-02"}
#         ]
#     },
#     "user2": {
#         "name": "Bob",
#         "comments": [
#             {"comment": "Nice work!", "date": "2025-04-03"},
#         ]
#     }
# }
# reports = user_name_raport(data)
# for name, comment, date in reports:
#     print(f'Комментарии от {name}: {comment} ({date})')

#---------------------------------------------------------------
def library_report(data, year):
    finish_list = []
    for item, value in data.items():
        for key in value:
            if key["year"] > year:
                result = (key['title'], key['author'], key['year'])
                finish_list.append(result)
    return finish_list

library = {
    "fiction": [
        {"title": "Book A", "author": "Author 1", "year": 2001},
        {"title": "Book B", "author": "Author 2", "year": 1995}
    ],
    "non_fiction": [
        {"title": "Book C", "author": "Author 3", "year": 2010},
        {"title": "Book D", "author": "Author 4", "year": 2020}
    ]
}

report = library_report(library, 2000)
print(report)