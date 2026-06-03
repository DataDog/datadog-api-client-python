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
    from datadog_api_client.v2.model.usage_summary_available_fields_attributes import (
        UsageSummaryAvailableFieldsAttributes,
    )
    from datadog_api_client.v2.model.usage_summary_available_fields_type import UsageSummaryAvailableFieldsType


class UsageSummaryAvailableFieldsBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_summary_available_fields_attributes import (
            UsageSummaryAvailableFieldsAttributes,
        )
        from datadog_api_client.v2.model.usage_summary_available_fields_type import UsageSummaryAvailableFieldsType

        return {
            "attributes": (UsageSummaryAvailableFieldsAttributes,),
            "id": (str,),
            "type": (UsageSummaryAvailableFieldsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UsageSummaryAvailableFieldsAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[UsageSummaryAvailableFieldsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Available-fields data.

        :param attributes: The lists of field names returned by ``GET /api/v1/usage/summary`` at each
            of its three response levels. Each list contains every key the data endpoint
            emits—both typed fields declared in the OpenAPI spec and untyped keys
            exposed through ``additionalProperties``.
        :type attributes: UsageSummaryAvailableFieldsAttributes, optional

        :param id: The identifier for the discovery scope. Always ``"all"``.
        :type id: str, optional

        :param type: Type of available-fields data.
        :type type: UsageSummaryAvailableFieldsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
