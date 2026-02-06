# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class FormDatastoreConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "datastore_id": (UUID,),
            "primary_column_name": (str,),
            "primary_key_generation_strategy": (str,),
        }

    attribute_map = {
        "datastore_id": "datastore_id",
        "primary_column_name": "primary_column_name",
        "primary_key_generation_strategy": "primary_key_generation_strategy",
    }

    def __init__(self_, datastore_id: UUID, primary_column_name: str, primary_key_generation_strategy: str, **kwargs):
        """
        Configuration for the form's associated datastore.

        :param datastore_id: The unique identifier of the datastore.
        :type datastore_id: UUID

        :param primary_column_name: The name of the primary key column.
        :type primary_column_name: str

        :param primary_key_generation_strategy: The strategy used for generating primary keys.
        :type primary_key_generation_strategy: str
        """
        super().__init__(kwargs)

        self_.datastore_id = datastore_id
        self_.primary_column_name = primary_column_name
        self_.primary_key_generation_strategy = primary_key_generation_strategy
