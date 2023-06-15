# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.monitor_config_policy_policy_create_request import (
    MonitorConfigPolicyPolicyCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType
from datadog_api_client.v2.model.monitor_config_policy_policy_create_request import (
    MonitorConfigPolicyPolicyCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_tag_policy_create_request import (
    MonitorConfigPolicyTagPolicyCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.monitor_config_policy_create_data import MonitorConfigPolicyCreateData


@dataclass
class MonitorConfigPolicyCreateRequestJSON:
    policy: Union[MonitorConfigPolicyPolicyCreateRequest, MonitorConfigPolicyTagPolicyCreateRequest, UnsetType] = unset
    policy_type: Union[MonitorConfigPolicyType, UnsetType] = unset


class MonitorConfigPolicyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_config_policy_create_data import MonitorConfigPolicyCreateData

        return {
            "data": (MonitorConfigPolicyCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MonitorConfigPolicyCreateRequestJSON

    def __init__(self_, data: MonitorConfigPolicyCreateData, **kwargs):
        """
        Request for creating a monitor configuration policy.

        :param data: A monitor configuration policy data.
        :type data: MonitorConfigPolicyCreateData
        """
        super().__init__(kwargs)

        self_.data = data
