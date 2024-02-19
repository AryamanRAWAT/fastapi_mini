from pydantic import BaseModel, Field
from typing import List, Optional


class UserSchema(BaseModel):
	id : int
	first_name : str
	last_name : str
	company_name : Optional[str] = None
	age : int
	city : str
	state : str
	zip : int
	email : str
	web : Optional[str] = None

	class Config:
		orm_mode = True
