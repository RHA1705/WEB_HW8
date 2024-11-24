<<<<<<< HEAD
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======
from models import Cats
import connect


print('--- All notes ---')
notes = Cats.objects()
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

print('--- Notes with tag Fun ---')

notes = Cats.objects(tags__name='Fun')
for note in notes:
    records = [f'description: {record.description}, done: {record.done}' for record in note.records]
    tags = [tag.name for tag in note.tags]
    print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

>>>>>>> 9972e5fa3ac37e93259c30ee4a6ac494ed5a18bf
