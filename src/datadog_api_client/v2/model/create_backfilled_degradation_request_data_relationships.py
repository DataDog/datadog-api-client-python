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
    from datadog_api_client.v2.model.create_backfilled_degradation_request_data_relationships_template import (
        CreateBackfilledDegradationRequestDataRelationshipsTemplate,
    )


class CreateBackfilledDegradationRequestDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_backfilled_degradation_request_data_relationships_template import (
            CreateBackfilledDegradationRequestDataRelationshipsTemplate,
        )

        return {
            "template": (CreateBackfilledDegradationRequestDataRelationshipsTemplate,),
        }

    attribute_map = {
        "template": "template",
    }

    def __init__(
        self_, template: Union[CreateBackfilledDegradationRequestDataRelationshipsTemplate, UnsetType] = unset, **kwargs
    ):
        """
        The supported relationships for creating a backfilled degradation.

        :param template: The template used to create the backfilled degradation.
        :type template: CreateBackfilledDegradationRequestDataRelationshipsTemplate, optional
        """
        if template is not unset:
            kwargs["template"] = template
        super().__init__(kwargs)
