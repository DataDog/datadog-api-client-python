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
    from datadog_api_client.v2.model.severity_override_response_data import SeverityOverrideResponseData
    from datadog_api_client.v2.model.severity_override_response_meta import SeverityOverrideResponseMeta


class SeverityOverrideResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.severity_override_response_data import SeverityOverrideResponseData
        from datadog_api_client.v2.model.severity_override_response_meta import SeverityOverrideResponseMeta

        return {
            "data": (SeverityOverrideResponseData,),
            "meta": (SeverityOverrideResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: SeverityOverrideResponseData,
        meta: Union[SeverityOverrideResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for the severity override request.

        :param data: Data of the severity override response.
        :type data: SeverityOverrideResponseData

        :param meta: Security findings skipped while processing the severity override request.
        :type meta: SeverityOverrideResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
