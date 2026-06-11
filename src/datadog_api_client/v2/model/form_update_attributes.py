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
    from datadog_api_client.v2.model.form_datastore_config_attributes import FormDatastoreConfigAttributes


class FormUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_datastore_config_attributes import FormDatastoreConfigAttributes

        return {
            "datastore_config": (FormDatastoreConfigAttributes,),
            "description": (str,),
            "name": (str,),
        }

    attribute_map = {
        "datastore_config": "datastore_config",
        "description": "description",
        "name": "name",
    }

    def __init__(
        self_,
        datastore_config: Union[FormDatastoreConfigAttributes, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The fields to update on a form. At least one field must be provided.

        :param datastore_config: The datastore configuration for a form.
        :type datastore_config: FormDatastoreConfigAttributes, optional

        :param description: The updated description of the form.
        :type description: str, optional

        :param name: The updated name of the form.
        :type name: str, optional
        """
        if datastore_config is not unset:
            kwargs["datastore_config"] = datastore_config
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
