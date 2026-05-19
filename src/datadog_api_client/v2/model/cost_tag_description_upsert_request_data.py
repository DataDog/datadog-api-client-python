# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_tag_description_upsert_request_data_attributes import (
        CostTagDescriptionUpsertRequestDataAttributes,
    )
    from datadog_api_client.v2.model.cost_tag_description_type import CostTagDescriptionType


class CostTagDescriptionUpsertRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_description_upsert_request_data_attributes import (
            CostTagDescriptionUpsertRequestDataAttributes,
        )
        from datadog_api_client.v2.model.cost_tag_description_type import CostTagDescriptionType

        return {
            "attributes": (CostTagDescriptionUpsertRequestDataAttributes,),
            "id": (str,),
            "type": (CostTagDescriptionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CostTagDescriptionUpsertRequestDataAttributes,
        type: CostTagDescriptionType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Resource envelope carrying the tag key description being upserted. The ``id`` is informational; the authoritative tag key is taken from the URL path.

        :param attributes: Mutable attributes set when creating or updating a Cloud Cost Management tag key description.
        :type attributes: CostTagDescriptionUpsertRequestDataAttributes

        :param id: Identifier of the tag key the description applies to. Matches the ``tag_key`` path parameter.
        :type id: str, optional

        :param type: Type of the Cloud Cost Management tag description resource.
        :type type: CostTagDescriptionType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
