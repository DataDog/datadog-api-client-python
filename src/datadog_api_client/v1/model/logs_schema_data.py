# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LogsSchemaData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "class_name": (str,),
            "class_uid": (int,),
            "profiles": ([str],),
            "schema_type": (str,),
            "version": (str,),
        }

    attribute_map = {
        "class_name": "class_name",
        "class_uid": "class_uid",
        "profiles": "profiles",
        "schema_type": "schema_type",
        "version": "version",
    }

    def __init__(
        self_,
        class_name: str,
        class_uid: int,
        schema_type: str,
        version: str,
        profiles: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration of the schema data to use.

        :param class_name: Class name of the schema to use.
        :type class_name: str

        :param class_uid: Class UID of the schema to use.
        :type class_uid: int

        :param profiles: Optional list of profiles to modify the schema.
        :type profiles: [str], optional

        :param schema_type: Type of schema to use.
        :type schema_type: str

        :param version: Version of the schema to use.
        :type version: str
        """
        if profiles is not unset:
            kwargs["profiles"] = profiles
        super().__init__(kwargs)

        self_.class_name = class_name
        self_.class_uid = class_uid
        self_.schema_type = schema_type
        self_.version = version
