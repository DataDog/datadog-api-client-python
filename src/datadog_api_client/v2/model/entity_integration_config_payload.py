# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class EntityIntegrationConfigPayload(ModelNormal):
    def __init__(self_, **kwargs):
        """
        Integration-specific configuration payload. The shape of this object depends on the integration identified by the path parameter. For ``github`` , the object must contain an ``enabled_repos`` array. For ``jira`` , it must contain an ``enabled_projects`` array. For ``pagerduty`` , it must contain an ``accounts`` array.
        """
        super().__init__(kwargs)
