# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class ExperimentsCreateExperimentProtocolRequestDataAttributes(ModelNormal):
    validations = {
        "name": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "description": (str, none_type),
            "migration_metadata": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
                none_type,
            ),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "migration_metadata": "migration_metadata",
        "name": "name",
    }

    def __init__(
        self_,
        name: str,
        description: Union[str, none_type, UnsetType] = unset,
        migration_metadata: Union[Dict[str, Any], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Create a draft protocol with the organization default subject type.

        :param description: Optional text that explains the protocol.
        :type description: str, none_type, optional

        :param migration_metadata: Metadata for imported resources. Must encode to at most 4096 bytes. Null clears it; omission preserves it on update.
        :type migration_metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param name: Protocol name. Leading and trailing spaces are removed. The trimmed name must contain 1 to 255 characters.
        :type name: str
        """
        if description is not unset:
            kwargs["description"] = description
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        super().__init__(kwargs)

        self_.name = name
