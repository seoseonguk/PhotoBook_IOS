from rest_framework.decorators import api_view
from rest_framework.response import Response as RestResponse


@api_view(["GET"])
def api_home(request):
    data = {
        "groups":{
        },

        "users":{

        }

    }
    return RestResponse(data)