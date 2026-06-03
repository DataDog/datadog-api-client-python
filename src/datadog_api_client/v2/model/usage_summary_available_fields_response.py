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
    from datadog_api_client.v2.model.usage_summary_available_fields_body import UsageSummaryAvailableFieldsBody


class UsageSummaryAvailableFieldsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_summary_available_fields_body import UsageSummaryAvailableFieldsBody

        return {
            "data": (UsageSummaryAvailableFieldsBody,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[UsageSummaryAvailableFieldsBody, UnsetType] = unset, **kwargs):
        """
        Response listing every field name returned by ``GET /api/v1/usage/summary``
        at each of its three response levels. Includes both typed fields and untyped
        ``additionalProperties`` keys.

        :param data: Available-fields data.
        :type data: UsageSummaryAvailableFieldsBody, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
