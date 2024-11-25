from models import Author
import connect

authors = Author.objects()
for author in authors:
    print(f"id: {author.id}, name: {author.fullname}")

# print('--- All notes ---')
# for cat in Cats.objects():
#     cat_names = [f'Cat name: ']
# notes = Cats.objects()
# for note in notes:
#     print(note.name)
#     records = [f'description: {record.description}, done: {record.done}' for record in note.records]
#     tags = [tag.name for tag in note.tags]
#     print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

# print('--- Notes with tag Fun ---')
#
# notes = Cats.objects(tags__name='Fun')
# for note in notes:
#     records = [f'description: {record.description}, done: {record.done}' for record in note.records]
#     tags = [tag.name for tag in note.tags]
#     print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

