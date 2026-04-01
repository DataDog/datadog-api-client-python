# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_user_defined_field_response_data import (
        IncidentUserDefinedFieldResponseData,
    )
    from datadog_api_client.v2.model.incident_user_defined_field_list_meta import IncidentUserDefinedFieldListMeta


class IncidentUserDefinedFieldListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_field_response_data import (
            IncidentUserDefinedFieldResponseData,
        )
        from datadog_api_client.v2.model.incident_user_defined_field_list_meta import IncidentUserDefinedFieldListMeta

        return {
            "data": ([IncidentUserDefinedFieldResponseData],),
            "meta": (IncidentUserDefinedFieldListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[IncidentUserDefinedFieldResponseData], meta: IncidentUserDefinedFieldListMeta, **kwargs
    ):
        """
        Response containing a list of incident user-defined fields.

        :param data: An array of user-defined field objects.
        :type data: [IncidentUserDefinedFieldResponseData]

        :param meta: Pagination metadata for the user-defined field list response.
        :type meta: IncidentUserDefinedFieldListMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
