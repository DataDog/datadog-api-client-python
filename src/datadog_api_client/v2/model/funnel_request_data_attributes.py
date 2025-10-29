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
    from datadog_api_client.v2.model.funnel_request_data_attributes_search import FunnelRequestDataAttributesSearch
    from datadog_api_client.v2.model.funnel_request_data_attributes_time import FunnelRequestDataAttributesTime


class FunnelRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.funnel_request_data_attributes_search import FunnelRequestDataAttributesSearch
        from datadog_api_client.v2.model.funnel_request_data_attributes_time import FunnelRequestDataAttributesTime

        return {
            "data_source": (str,),
            "enforced_execution_type": (str,),
            "request_id": (str,),
            "search": (FunnelRequestDataAttributesSearch,),
            "time": (FunnelRequestDataAttributesTime,),
        }

    attribute_map = {
        "data_source": "data_source",
        "enforced_execution_type": "enforced_execution_type",
        "request_id": "request_id",
        "search": "search",
        "time": "time",
    }

    def __init__(
        self_,
        data_source: Union[str, UnsetType] = unset,
        enforced_execution_type: Union[str, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        search: Union[FunnelRequestDataAttributesSearch, UnsetType] = unset,
        time: Union[FunnelRequestDataAttributesTime, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data_source:
        :type data_source: str, optional

        :param enforced_execution_type:
        :type enforced_execution_type: str, optional

        :param request_id:
        :type request_id: str, optional

        :param search:
        :type search: FunnelRequestDataAttributesSearch, optional

        :param time:
        :type time: FunnelRequestDataAttributesTime, optional
        """
        if data_source is not unset:
            kwargs["data_source"] = data_source
        if enforced_execution_type is not unset:
            kwargs["enforced_execution_type"] = enforced_execution_type
        if request_id is not unset:
            kwargs["request_id"] = request_id
        if search is not unset:
            kwargs["search"] = search
        if time is not unset:
            kwargs["time"] = time
        super().__init__(kwargs)
