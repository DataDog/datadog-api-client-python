# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_gate_response_data_attributes_created_by import (
        DeploymentGateResponseDataAttributesCreatedBy,
    )
    from datadog_api_client.v2.model.deployment_gate_response_data_attributes_updated_by import (
        DeploymentGateResponseDataAttributesUpdatedBy,
    )


class DeploymentGateResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gate_response_data_attributes_created_by import (
            DeploymentGateResponseDataAttributesCreatedBy,
        )
        from datadog_api_client.v2.model.deployment_gate_response_data_attributes_updated_by import (
            DeploymentGateResponseDataAttributesUpdatedBy,
        )

        return {
            "created_at": (datetime,),
            "created_by": (DeploymentGateResponseDataAttributesCreatedBy,),
            "dry_run": (bool,),
            "env": (str,),
            "identifier": (str,),
            "service": (str,),
            "updated_at": (datetime,),
            "updated_by": (DeploymentGateResponseDataAttributesUpdatedBy,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "dry_run": "dry_run",
        "env": "env",
        "identifier": "identifier",
        "service": "service",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: DeploymentGateResponseDataAttributesCreatedBy,
        dry_run: bool,
        env: str,
        identifier: str,
        service: str,
        updated_at: Union[datetime, UnsetType] = unset,
        updated_by: Union[DeploymentGateResponseDataAttributesUpdatedBy, UnsetType] = unset,
        **kwargs,
    ):
        """
        Basic information about a deployment gate.

        :param created_at: The timestamp when the deployment gate was created.
        :type created_at: datetime

        :param created_by: Information about the user who created the deployment gate.
        :type created_by: DeploymentGateResponseDataAttributesCreatedBy

        :param dry_run: Whether this gate is run in dry-run mode.
        :type dry_run: bool

        :param env: The environment of the deployment gate.
        :type env: str

        :param identifier: The identifier of the deployment gate.
        :type identifier: str

        :param service: The service of the deployment gate.
        :type service: str

        :param updated_at: The timestamp when the deployment gate was last updated.
        :type updated_at: datetime, optional

        :param updated_by: Information about the user who updated the deployment gate.
        :type updated_by: DeploymentGateResponseDataAttributesUpdatedBy, optional
        """
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.dry_run = dry_run
        self_.env = env
        self_.identifier = identifier
        self_.service = service
