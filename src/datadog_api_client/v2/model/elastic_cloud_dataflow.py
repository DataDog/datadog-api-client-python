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
    from datadog_api_client.v2.model.elastic_cloud_dataflow_id import ElasticCloudDataflowId
    from datadog_api_client.v2.model.integration_account_dataflow_status import IntegrationAccountDataflowStatus


class ElasticCloudDataflow(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_dataflow_id import ElasticCloudDataflowId
        from datadog_api_client.v2.model.integration_account_dataflow_status import IntegrationAccountDataflowStatus

        return {
            "enabled": (bool,),
            "id": (ElasticCloudDataflowId,),
            "status": (IntegrationAccountDataflowStatus,),
        }

    attribute_map = {
        "enabled": "enabled",
        "id": "id",
        "status": "status",
    }
    read_only_vars = {
        "status",
    }

    def __init__(
        self_,
        id: ElasticCloudDataflowId,
        enabled: Union[bool, UnsetType] = unset,
        status: Union[IntegrationAccountDataflowStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        An Elastic Cloud dataflow toggle. The set of dataflow ids is fixed by the interface schema.

        :param enabled: Whether the dataflow is enabled.
        :type enabled: bool, optional

        :param id: Identifier of an Elastic Cloud dataflow.
        :type id: ElasticCloudDataflowId

        :param status: Read-only, server-computed collection status of a dataflow.
        :type status: IntegrationAccountDataflowStatus, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)

        self_.id = id
