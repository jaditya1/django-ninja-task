from ninja import Schema
from ninja import Router
from .models import Tag,Seed
from ninja.orm import create_schema
from ninja.pagination import paginate
from typing import List
from django.shortcuts import get_object_or_404
from functools import wraps


router = Router()

ListTagSchema = create_schema(Tag,exclude=[])
TagSchema = create_schema(Tag,exclude=["created_by","updated_by","id","deleted"])

class Message(Schema):
	message: str



# For authentication check
def auth_check(view_func):
	@wraps(view_func)
	def wrapper(request, *args, **kwargs):
		if not request.user.is_authenticated:
			return 401, {"message": "Please sign in first!!"}

		return view_func(request, *args, **kwargs)

	return wrapper


# Api endpoints
@router.get('/tags', response={200:List[ListTagSchema],401:Message})
@auth_check
@paginate
def list_tag(request):
	return Tag.objects.all()



@router.post('/tags/create', response={200:Message,401:Message,422:Message})
@auth_check
def create_tag(request,tag:TagSchema):
	try:
		data_dict = tag.dict()
		data_dict["created_by_id"] = request.user.id
		Tag.objects.create(**data_dict)
		return 200, {"message":"Tag is created successfully!!"}
	except Exception as e:
		return 422,{"message":str(e)}


@router.put('/tags/update/{tag_id}', response={200:Message,401:Message,404:Message,422:Message})
@auth_check
def update_tag(request,tag:TagSchema,tag_id:int):
	try:
		tag_row = Tag.objects.filter(id=tag_id)
		if tag_row.first():
			pass
		else:
			return 404,{"message":"Tag is not found!!"}
		data_dict = tag.dict()
		data_dict["updated_by_id"] = request.user.id
		tag_row.update(**data_dict)
		return 200, {"message":"Tag is updated successfully!!"}
	except Exception as e:
		return 422,{"message":str(e)}



@router.delete('tags/delete/{tag_id}',response={401:Message,404:Message,200:Message})
@auth_check
def delete_tag(request,tag_id:int):
	tag = Tag.objects.filter(id=tag_id)
	if tag.first():
		pass
	else:
		return 404,{"message":"Tag is not found!!"}
	tag.update(deleted=True)
	return  200, {"message":"Tag is deleted successfully!!"}



def sh_recursion(value,tag_id,index_value=1):
	sh = value[:index_value]
	record_check = Tag.objects.filter(short_name=sh)
	if record_check.count()==0:
		Tag.objects.filter(id=tag_id).update(short_name=sh)
	else:
		index_value = index_value+1
		sh_recursion(value,tag_id,index_value)
	return sh



@router.get('/seeds')
def list_seeds(request):
	query = Seed.objects.filter(tag__deleted=False).select_related("tag")
	result = []
	for i in query:
		data_dict = {}
		data_dict["id"] = i.id
		data_dict["column"] = i.column
		data_dict["row"] = i.row
		data_dict["tags"] = {}
		data_dict["tags"]["value"] = i.tag.tag_value
		if i.tag.short_name==None:
			data_dict["tags"]["short_name"] = sh_recursion(
												value=data_dict["tags"]["value"],
												tag_id=i.tag.id,
												index_value=1
											)
		else:
			data_dict["tags"]["short_name"] = i.tag.short_name
		result.append(data_dict)
	return result



