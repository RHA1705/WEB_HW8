from models import Author
import connect

id_numbers = ['67447d8b9cf5ae4385de67b9', '67447d8c9cf5ae4385de67ba']

for i in id_numbers:
    note = Author.objects(id=i).delete()

print('--- Deleted ---')