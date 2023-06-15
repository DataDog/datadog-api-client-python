# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.monitor_config_policy_policy import MonitorConfigPolicyPolicy
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType
from datadog_api_client.v2.model.monitor_config_policy_policy import MonitorConfigPolicyPolicy
from datadog_api_client.v2.model.monitor_config_policy_tag_policy import MonitorConfigPolicyTagPolicy
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.monitor_config_policy_response_data import MonitorConfigPolicyResponseData


@dataclass
class MonitorConfigPolicyListResponseJSON:
    id: str
    policy: Union[MonitorConfigPolicyPolicy, MonitorConfigPolicyTagPolicy, UnsetType] = unset
    policy_type: Union[MonitorConfigPolicyType, UnsetType] = unset


class MonitorConfigPolicyListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_config_policy_response_data import MonitorConfigPolicyResponseData

        return {
            "data": ([MonitorConfigPolicyResponseData],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MonitorConfigPolicyListResponseJSON

    def __init__(self_, data: Union[List[MonitorConfigPolicyResponseData], UnsetType] = unset, **kwargs):
        """
        Response for retrieving all monitor configuration policies.

        :param data: An array of monitor configuration policies.
        :type data: [MonitorConfigPolicyResponseData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
