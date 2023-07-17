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
    from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes import (
        CIAppCreatePipelineEventRequestAttributes,
    )
    from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data_type import (
        CIAppCreatePipelineEventRequestDataType,
    )


class CIAppCreatePipelineEventRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes import (
            CIAppCreatePipelineEventRequestAttributes,
        )
        from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data_type import (
            CIAppCreatePipelineEventRequestDataType,
        )

        return {
            "attributes": (CIAppCreatePipelineEventRequestAttributes,),
            "type": (CIAppCreatePipelineEventRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CIAppCreatePipelineEventRequestAttributes, UnsetType] = unset,
        type: Union[CIAppCreatePipelineEventRequestDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the pipeline event to create.

        :param attributes: Attributes of the pipeline event to create.
        :type attributes: CIAppCreatePipelineEventRequestAttributes, optional

        :param type: Type of the event.
        :type type: CIAppCreatePipelineEventRequestDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
