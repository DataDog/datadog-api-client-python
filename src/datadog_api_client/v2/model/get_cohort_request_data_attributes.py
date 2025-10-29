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
    from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition import (
        GetCohortRequestDataAttributesDefinition,
    )
    from datadog_api_client.v2.model.get_cohort_request_data_attributes_time import GetCohortRequestDataAttributesTime


class GetCohortRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition import (
            GetCohortRequestDataAttributesDefinition,
        )
        from datadog_api_client.v2.model.get_cohort_request_data_attributes_time import (
            GetCohortRequestDataAttributesTime,
        )

        return {
            "data_source": (str,),
            "definition": (GetCohortRequestDataAttributesDefinition,),
            "enforced_execution_type": (str,),
            "request_id": (str,),
            "time": (GetCohortRequestDataAttributesTime,),
            "window_size": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "definition": "definition",
        "enforced_execution_type": "enforced_execution_type",
        "request_id": "request_id",
        "time": "time",
        "window_size": "window_size",
    }

    def __init__(
        self_,
        data_source: Union[str, UnsetType] = unset,
        definition: Union[GetCohortRequestDataAttributesDefinition, UnsetType] = unset,
        enforced_execution_type: Union[str, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        time: Union[GetCohortRequestDataAttributesTime, UnsetType] = unset,
        window_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data_source:
        :type data_source: str, optional

        :param definition:
        :type definition: GetCohortRequestDataAttributesDefinition, optional

        :param enforced_execution_type:
        :type enforced_execution_type: str, optional

        :param request_id:
        :type request_id: str, optional

        :param time:
        :type time: GetCohortRequestDataAttributesTime, optional

        :param window_size:
        :type window_size: str, optional
        """
        if data_source is not unset:
            kwargs["data_source"] = data_source
        if definition is not unset:
            kwargs["definition"] = definition
        if enforced_execution_type is not unset:
            kwargs["enforced_execution_type"] = enforced_execution_type
        if request_id is not unset:
            kwargs["request_id"] = request_id
        if time is not unset:
            kwargs["time"] = time
        if window_size is not unset:
            kwargs["window_size"] = window_size
        super().__init__(kwargs)
