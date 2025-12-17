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
    from datadog_api_client.v2.model.sankey_request_data_attributes_definition import (
        SankeyRequestDataAttributesDefinition,
    )
    from datadog_api_client.v2.model.sankey_request_data_attributes_sampling import SankeyRequestDataAttributesSampling
    from datadog_api_client.v2.model.sankey_request_data_attributes_search import SankeyRequestDataAttributesSearch
    from datadog_api_client.v2.model.sankey_request_data_attributes_time import SankeyRequestDataAttributesTime


class SankeyRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sankey_request_data_attributes_definition import (
            SankeyRequestDataAttributesDefinition,
        )
        from datadog_api_client.v2.model.sankey_request_data_attributes_sampling import (
            SankeyRequestDataAttributesSampling,
        )
        from datadog_api_client.v2.model.sankey_request_data_attributes_search import SankeyRequestDataAttributesSearch
        from datadog_api_client.v2.model.sankey_request_data_attributes_time import SankeyRequestDataAttributesTime

        return {
            "data_source": (str,),
            "definition": (SankeyRequestDataAttributesDefinition,),
            "enforced_execution_type": (str,),
            "request_id": (str,),
            "sampling": (SankeyRequestDataAttributesSampling,),
            "search": (SankeyRequestDataAttributesSearch,),
            "time": (SankeyRequestDataAttributesTime,),
        }

    attribute_map = {
        "data_source": "data_source",
        "definition": "definition",
        "enforced_execution_type": "enforced_execution_type",
        "request_id": "request_id",
        "sampling": "sampling",
        "search": "search",
        "time": "time",
    }

    def __init__(
        self_,
        data_source: Union[str, UnsetType] = unset,
        definition: Union[SankeyRequestDataAttributesDefinition, UnsetType] = unset,
        enforced_execution_type: Union[str, UnsetType] = unset,
        request_id: Union[str, UnsetType] = unset,
        sampling: Union[SankeyRequestDataAttributesSampling, UnsetType] = unset,
        search: Union[SankeyRequestDataAttributesSearch, UnsetType] = unset,
        time: Union[SankeyRequestDataAttributesTime, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data_source:
        :type data_source: str, optional

        :param definition:
        :type definition: SankeyRequestDataAttributesDefinition, optional

        :param enforced_execution_type:
        :type enforced_execution_type: str, optional

        :param request_id:
        :type request_id: str, optional

        :param sampling:
        :type sampling: SankeyRequestDataAttributesSampling, optional

        :param search:
        :type search: SankeyRequestDataAttributesSearch, optional

        :param time:
        :type time: SankeyRequestDataAttributesTime, optional
        """
        if data_source is not unset:
            kwargs["data_source"] = data_source
        if definition is not unset:
            kwargs["definition"] = definition
        if enforced_execution_type is not unset:
            kwargs["enforced_execution_type"] = enforced_execution_type
        if request_id is not unset:
            kwargs["request_id"] = request_id
        if sampling is not unset:
            kwargs["sampling"] = sampling
        if search is not unset:
            kwargs["search"] = search
        if time is not unset:
            kwargs["time"] = time
        super().__init__(kwargs)
