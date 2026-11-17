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
    from datadog_api_client.v2.model.nebius_cloud_integration_account_metrics_config_request import (
        NebiusCloudIntegrationAccountMetricsConfigRequest,
    )


class NebiusCloudIntegrationAccountSettingsRequest(ModelNormal):
    validations = {
        "tenant_id": {
            "max_length": 255,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.nebius_cloud_integration_account_metrics_config_request import (
            NebiusCloudIntegrationAccountMetricsConfigRequest,
        )

        return {
            "account_tags": ([str],),
            "metrics_config": (NebiusCloudIntegrationAccountMetricsConfigRequest,),
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
        metrics_config: Union[NebiusCloudIntegrationAccountMetricsConfigRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings for creating the Nebius Cloud integration account.

        :param account_tags: Tags applied to all metrics, logs, and resources collected from this Nebius Cloud account. Defaults to no tags.
        :type account_tags: [str], optional

        :param metrics_config: Configuration for metric collection from this Nebius Cloud account.
        :type metrics_config: NebiusCloudIntegrationAccountMetricsConfigRequest, optional

        :param tenant_id: ID of the Nebius tenant to monitor, the organizational workspace identifier. Found in the Nebius console under Administration > Organization.
        :type tenant_id: str
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        if metrics_config is not unset:
            kwargs["metrics_config"] = metrics_config
        super().__init__(kwargs)

        self_.tenant_id = tenant_id
