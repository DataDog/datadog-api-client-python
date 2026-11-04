# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.commitments_list_response_attributes import CommitmentsListResponseAttributes
    from datadog_api_client.v2.model.commitments_list_response_type import CommitmentsListResponseType


class CommitmentsListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_list_response_attributes import CommitmentsListResponseAttributes
        from datadog_api_client.v2.model.commitments_list_response_type import CommitmentsListResponseType

        return {
            "attributes": (CommitmentsListResponseAttributes,),
            "id": (str,),
            "type": (CommitmentsListResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: CommitmentsListResponseAttributes, id: str, type: CommitmentsListResponseType, **kwargs
    ):
        """
        The commitments list resource.

        :param attributes: Attributes of a commitments list response.
        :type attributes: CommitmentsListResponseAttributes

        :param id: The identifier of the commitments list response.
        :type id: str

        :param type: Type of the commitments list response resource.
        :type type: CommitmentsListResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
