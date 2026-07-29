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
    from datadog_api_client.v2.model.incident_on_call_page_data_attributes_request import (
        IncidentOnCallPageDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_on_call_page_type import IncidentOnCallPageType


class IncidentOnCallPageDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_on_call_page_data_attributes_request import (
            IncidentOnCallPageDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_on_call_page_type import IncidentOnCallPageType

        return {
            "attributes": (IncidentOnCallPageDataAttributesRequest,),
            "id": (str,),
            "type": (IncidentOnCallPageType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: IncidentOnCallPageType,
        attributes: Union[IncidentOnCallPageDataAttributesRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        On-call page data in a link request.

        :param attributes: Attributes for linking a page to an incident.
        :type attributes: IncidentOnCallPageDataAttributesRequest, optional

        :param id: The ID of the on-call page to link.
        :type id: str

        :param type: On-call page resource type.
        :type type: IncidentOnCallPageType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
