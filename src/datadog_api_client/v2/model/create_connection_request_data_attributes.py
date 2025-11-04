# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
        CreateConnectionRequestDataAttributesFieldsItems,
    )


class CreateConnectionRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
            CreateConnectionRequestDataAttributesFieldsItems,
        )

        return {
            "fields": ([CreateConnectionRequestDataAttributesFieldsItems],),
            "join_attribute": (str,),
            "join_type": (str,),
            "metadata": ({str: (str,)},),
            "type": (str,),
        }

    attribute_map = {
        "fields": "fields",
        "join_attribute": "join_attribute",
        "join_type": "join_type",
        "metadata": "metadata",
        "type": "type",
    }

    def __init__(
        self_,
        join_attribute: str,
        join_type: str,
        type: str,
        fields: Union[List[CreateConnectionRequestDataAttributesFieldsItems], UnsetType] = unset,
        metadata: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param fields:
        :type fields: [CreateConnectionRequestDataAttributesFieldsItems], optional

        :param join_attribute:
        :type join_attribute: str

        :param join_type:
        :type join_type: str

        :param metadata:
        :type metadata: {str: (str,)}, optional

        :param type:
        :type type: str
        """
        if fields is not unset:
            kwargs["fields"] = fields
        if metadata is not unset:
            kwargs["metadata"] = metadata
        super().__init__(kwargs)

        self_.join_attribute = join_attribute
        self_.join_type = join_type
        self_.type = type
