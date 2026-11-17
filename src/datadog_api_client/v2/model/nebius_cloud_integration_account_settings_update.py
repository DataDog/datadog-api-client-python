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
    from datadog_api_client.v2.model.nebius_cloud_integration_account_metrics_config_update import (
        NebiusCloudIntegrationAccountMetricsConfigUpdate,
    )


class NebiusCloudIntegrationAccountSettingsUpdate(ModelNormal):
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
        from datadog_api_client.v2.model.nebius_cloud_integration_account_metrics_config_update import (
            NebiusCloudIntegrationAccountMetricsConfigUpdate,
        )

        return {
            "account_tags": ([str],),
            "metrics_config": (NebiusCloudIntegrationAccountMetricsConfigUpdate,),
            "tenant_id": (str,),
        }

    attribute_map = {
        "account_tags": "account_tags",
        "metrics_config": "metrics_config",
        "tenant_id": "tenant_id",
    }

    def __init__(
        self_,
        account_tags: Union[List[str], UnsetType] = unset,
        metrics_config: Union[NebiusCloudIntegrationAccountMetricsConfigUpdate, UnsetType] = unset,
        tenant_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings for updating the Nebius Cloud integration account. Only the fields provided are changed.

        :param account_tags: Tags applied to all metrics, logs, and resources collected from this Nebius Cloud account. Sending it replaces the whole list; send an empty array to remove all tags, or omit it to keep the stored list.
        :type account_tags: [str], optional

        :param metrics_config: Configuration for metric collection. Only the fields provided are changed.
        :type metrics_config: NebiusCloudIntegrationAccountMetricsConfigUpdate, optional

        :param tenant_id: ID of the Nebius tenant to monitor. An empty value is ignored and the stored tenant ID is kept.
        :type tenant_id: str, optional
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        if metrics_config is not unset:
            kwargs["metrics_config"] = metrics_config
        if tenant_id is not unset:
            kwargs["tenant_id"] = tenant_id
        super().__init__(kwargs)
