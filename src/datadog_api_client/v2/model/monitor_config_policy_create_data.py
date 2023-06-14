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
from datadog_api_client.v2.model.monitor_config_policy_attribute_create_request import (
    MonitorConfigPolicyAttributeCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_policy_create_request import (
    MonitorConfigPolicyPolicyCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_tag_policy_create_request import (
    MonitorConfigPolicyTagPolicyCreateRequest,
)
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.monitor_config_policy_resource_type import MonitorConfigPolicyResourceType


@dataclass
class MonitorConfigPolicyCreateDataJSON:
    policy: Union[MonitorConfigPolicyPolicyCreateRequest, MonitorConfigPolicyTagPolicyCreateRequest, UnsetType] = unset
    policy_type: Union[MonitorConfigPolicyType, UnsetType] = unset


class MonitorConfigPolicyCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_config_policy_resource_type import MonitorConfigPolicyResourceType

        return {
            "attributes": (MonitorConfigPolicyAttributeCreateRequest,),
            "type": (MonitorConfigPolicyResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = MonitorConfigPolicyCreateDataJSON

    def __init__(
        self_, attributes: MonitorConfigPolicyAttributeCreateRequest, type: MonitorConfigPolicyResourceType, **kwargs
    ):
        """
        A monitor configuration policy data.

        :param attributes: Policy and policy type for a monitor configuration policy.
        :type attributes: MonitorConfigPolicyAttributeCreateRequest

        :param type: Monitor configuration policy resource type.
        :type type: MonitorConfigPolicyResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
