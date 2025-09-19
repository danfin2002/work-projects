from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from datetime import date


class PersonsOrm(Base):
	__tablename__ = "persons"
	
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	birthday: Mapped[date]# = mapped_column(Date)
	city: Mapped[str]