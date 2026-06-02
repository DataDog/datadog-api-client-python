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
    from datadog_api_client.v2.model.assignee_response_data import AssigneeResponseData
    from datadog_api_client.v2.model.assignee_response_meta import AssigneeResponseMeta


class AssigneeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.assignee_response_data import AssigneeResponseData
        from datadog_api_client.v2.model.assignee_response_meta import AssigneeResponseMeta

        return {
            "data": (AssigneeResponseData,),
            "meta": (AssigneeResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: AssigneeResponseData, meta: Union[AssigneeResponseMeta, UnsetType] = unset, **kwargs):
        """
        Response for the assign or unassign request.

        :param data: Data of the assignee response.
        :type data: AssigneeResponseData

        :param meta: Per-finding warnings and failures produced while processing the bulk assignee request.
        :type meta: AssigneeResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
