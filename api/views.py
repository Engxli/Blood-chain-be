from django.db.models import F
from django.http import HttpRequest, JsonResponse

from nft.models import NFT


def get_nft_info_by_id(request: HttpRequest, nft_id: int) -> JsonResponse:
    try:
        nft = NFT.objects.get(id=nft_id)
    except NFT.DoesNotExist:
        return JsonResponse({"error": "Nft does not exist"}, status=404)

    attributes = nft.attributes.values(
        "value", trait_type=F("attr_name__name")
    )
    return JsonResponse(
        {
            "attributes": list(attributes),
            "description": nft.description,
            "image": request.build_absolute_uri(nft.image.url),
            "name": nft.name,
        }
    )
