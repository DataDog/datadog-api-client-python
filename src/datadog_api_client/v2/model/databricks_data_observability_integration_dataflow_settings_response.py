# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DatabricksDataObservabilityIntegrationDataflowSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "do_crawlers_cron": (str,),
            "sync_system_catalog": (bool,),
        }

    attribute_map = {
        "do_crawlers_cron": "do_crawlers_cron",
        "sync_system_catalog": "sync_system_catalog",
    }

    def __init__(
        self_,
        do_crawlers_cron: Union[str, UnsetType] = unset,
        sync_system_catalog: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings of the Databricks data observability dataflow.

        :param do_crawlers_cron: Cron expression setting how often the data observability crawlers run.
        :type do_crawlers_cron: str, optional

        :param sync_system_catalog: Whether the Databricks ``system`` catalog is synchronized alongside your data catalogs.
        :type sync_system_catalog: bool, optional
        """
        if do_crawlers_cron is not unset:
            kwargs["do_crawlers_cron"] = do_crawlers_cron
        if sync_system_catalog is not unset:
            kwargs["sync_system_catalog"] = sync_system_catalog
        super().__init__(kwargs)
