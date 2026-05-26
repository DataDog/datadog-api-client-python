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
    from datadog_api_client.v2.model.security_monitoring_dataset_definition import SecurityMonitoringDatasetDefinition


class SecurityMonitoringDatasetAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_definition import (
            SecurityMonitoringDatasetDefinition,
        )

        return {
            "definition": (SecurityMonitoringDatasetDefinition,),
            "description": (str,),
            "version": (int,),
        }

    attribute_map = {
        "definition": "definition",
        "description": "description",
        "version": "version",
    }

    def __init__(
        self_,
        definition: SecurityMonitoringDatasetDefinition,
        description: Union[str, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a dataset create or update request.

        :param definition: The definition of the dataset. The shape depends on the value of ``data_source``.
            Use ``reference_table`` or ``managed_resource`` for a referential dataset, or one of the
            event platform sources (for example ``logs`` , ``audit`` , ``events`` , ``spans`` , ``rum`` ) for
            an event platform dataset.
        :type definition: SecurityMonitoringDatasetDefinition

        :param description: The description of the dataset. Maximum 255 characters.
        :type description: str, optional

        :param version: The expected current version of the dataset for optimistic concurrency control on updates.
            If the dataset's current version does not match, the request is rejected with a 409 Conflict.
        :type version: int, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.definition = definition
