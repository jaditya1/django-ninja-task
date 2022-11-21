from ninja import NinjaAPI

from SeedMgmt.api import router

api = NinjaAPI()

api.add_router("/seedx/v1/", router)