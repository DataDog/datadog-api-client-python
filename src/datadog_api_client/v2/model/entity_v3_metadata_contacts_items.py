# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class EntityV3MetadataContactsItems(ModelNormal):
    validations = {
        "name": {
            "min_length": 2,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "contact": (str,),
            "name": (str,),
            "type": (str,),
        }

    attribute_map = {
        "contact": "contact",
        "name": "name",
        "type": "type",
    }

    def __init__(self_, contact: str, type: str, name: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of Entity V3 Metadata Contacts Items object.

        :param contact: Contact value
        :type contact: str

        :param name: Contact name
        :type name: str, optional

        :param type: Contact type.
        :type type: str
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.contact = contact
        self_.type = type
