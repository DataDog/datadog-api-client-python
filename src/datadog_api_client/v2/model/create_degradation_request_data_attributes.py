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
    from datadog_api_client.v2.model.create_degradation_request_data_attributes_components_affected_items import (
        CreateDegradationRequestDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
        CreateDegradationRequestDataAttributesStatus,
    )


class CreateDegradationRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_request_data_attributes_components_affected_items import (
            CreateDegradationRequestDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
            CreateDegradationRequestDataAttributesStatus,
        )

        return {
            "components_affected": ([CreateDegradationRequestDataAttributesComponentsAffectedItems],),
            "description": (str,),
            "status": (CreateDegradationRequestDataAttributesStatus,),
            "title": (str,),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "description": "description",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        components_affected: List[CreateDegradationRequestDataAttributesComponentsAffectedItems],
        status: CreateDegradationRequestDataAttributesStatus,
        title: str,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The supported attributes for creating a degradation.

        :param components_affected: The components affected by the degradation.
        :type components_affected: [CreateDegradationRequestDataAttributesComponentsAffectedItems]

        :param description: The description of the degradation.
        :type description: str, optional

        :param status: The status of the degradation.
        :type status: CreateDegradationRequestDataAttributesStatus

        :param title: The title of the degradation.
        :type title: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.components_affected = components_affected
        self_.status = status
        self_.title = title
