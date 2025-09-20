from database import sync_engine, async_engine, sync_session_factory, async_session_factory, Base
from models import PersonsOrm#,DogsOrm
from datetime import date
#from sqlalchemy import MetaData
#Её нужно будет создать раз через миграции
# def create_tables()->None: #Миграции - старую удалять и создавать новую неправильно
# 	sync_engine.echo=False
# 	Base.metadata.drop_all(sync_engine)
# 	Base.metadata.create_all(sync_engine)
# 	sync_engine.echo=True

	
def insert_data_sync():
	person_daniel = PersonsOrm(name="Daniel", birthday=date(2002, 11, 19), city="Ryazan")
	person_andrew = PersonsOrm(name="Andrew", birthday=date(2002, 7, 31), city="Engels")
	#dog_jack = DogsOrm(name="Jack")
	with sync_session_factory() as session:
		session.add_all([person_daniel, person_andrew])
		session.commit()
	
	
	
async def insert_data_async():
	person_daniel = PersonsOrm(name="Daniel", birthday=date(2002, 11, 19), city="Ryazan")
	person_andrew = PersonsOrm(name="Andrew", birthday=date(2002, 7, 31), city="Engels")
	#dog_jack = DogsOrm(name="Jack")
	async with async_session_factory() as session:
		session.add_all([person_daniel, person_andrew])
		await session.commit()