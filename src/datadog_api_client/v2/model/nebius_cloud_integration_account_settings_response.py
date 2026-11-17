# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.nebius_cloud_integration_account_metrics_config_response import (
        NebiusCloudIntegrationAccountMetricsConfigResponse,
    )


class NebiusCloudIntegrationAccountSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_integration_account_metrics_config_response import (
            NebiusCloudIntegrationAccountMetricsConfigResponse,
        )

        return {
            "account_tags": ([str],),
            "metrics_config": (NebiusCloudIntegrationAccountMetricsConfigResponse,),
            "tenant_id": (str,),
        }

    attribute_map = {
        "account_tags": "account_tags",
        "metrics_config": "metrics_config",
        "tenant_id": "tenant_id",
    }

    def __init__(
        self_,
        tenant_id: str,
        account_tags: Union[List[str], UnsetType] = unset,
        metrics_config: Union[NebiusCloudIntegrationAccountMetricsConfigResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings configured on the Nebius Cloud integration account.

        :param account_tags: Tags applied to all data collected from this Nebius Cloud account.
        :type account_tags: [str], optional

        :param metrics_config: Metric collection settings configured on the Nebius Cloud integration account. Absent or empty when no filters are configured.
        :type metrics_config: NebiusCloudIntegrationAccountMetricsConfigResponse, optional

        :param tenant_id: ID of the Nebius tenant being monitored.
        :type tenant_id: str
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        if metrics_config is not unset:
            kwargs["metrics_config"] = metrics_config
        super().__init__(kwargs)

        self_.tenant_id = tenant_id
