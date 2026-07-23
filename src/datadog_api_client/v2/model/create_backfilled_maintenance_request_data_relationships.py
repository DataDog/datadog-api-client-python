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
    from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_relationships_template import (
        CreateBackfilledMaintenanceRequestDataRelationshipsTemplate,
    )


class CreateBackfilledMaintenanceRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_backfilled_maintenance_request_data_relationships_template import (
            CreateBackfilledMaintenanceRequestDataRelationshipsTemplate,
        )

        return {
            "template": (CreateBackfilledMaintenanceRequestDataRelationshipsTemplate,),
        }

    attribute_map = {
        "template": "template",
    }

    def __init__(
        self_, template: Union[CreateBackfilledMaintenanceRequestDataRelationshipsTemplate, UnsetType] = unset, **kwargs
    ):
        """
        The supported relationships for creating a backfilled maintenance.

        :param template: The template used to create the backfilled maintenance.
        :type template: CreateBackfilledMaintenanceRequestDataRelationshipsTemplate, optional
        """
        if template is not unset:
            kwargs["template"] = template
        super().__init__(kwargs)
