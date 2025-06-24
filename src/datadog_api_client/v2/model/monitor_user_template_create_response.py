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
    from datadog_api_client.v2.model.monitor_user_template_response_data import MonitorUserTemplateResponseData


class MonitorUserTemplateCreateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_user_template_response_data import MonitorUserTemplateResponseData

        return {
            "data": (MonitorUserTemplateResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[MonitorUserTemplateResponseData, UnsetType] = unset, **kwargs):
        """
        Response for creating a monitor user template.

        :param data: Monitor user template list response data.
        :type data: MonitorUserTemplateResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
