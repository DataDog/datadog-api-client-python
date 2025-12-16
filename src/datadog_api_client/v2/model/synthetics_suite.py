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
    from datadog_api_client.v2.model.synthetics_suite_options import SyntheticsSuiteOptions
    from datadog_api_client.v2.model.synthetics_suite_test import SyntheticsSuiteTest
    from datadog_api_client.v2.model.synthetics_suite_type import SyntheticsSuiteType


class SyntheticsSuite(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_suite_options import SyntheticsSuiteOptions
        from datadog_api_client.v2.model.synthetics_suite_test import SyntheticsSuiteTest
        from datadog_api_client.v2.model.synthetics_suite_type import SyntheticsSuiteType

        return {
            "message": (str,),
            "name": (str,),
            "options": (SyntheticsSuiteOptions,),
            "public_id": (str,),
            "tags": ([str],),
            "tests": ([SyntheticsSuiteTest],),
            "type": (SyntheticsSuiteType,),
        }

    attribute_map = {
        "message": "message",
        "name": "name",
        "options": "options",
        "public_id": "public_id",
        "tags": "tags",
        "tests": "tests",
        "type": "type",
    }
    read_only_vars = {
        "public_id",
    }

    def __init__(
        self_,
        message: str,
        name: str,
        options: SyntheticsSuiteOptions,
        tests: List[SyntheticsSuiteTest],
        type: SyntheticsSuiteType,
        public_id: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing details about a Synthetic suite.

        :param message: Notification message associated with the suite.
        :type message: str

        :param name: Name of the suite.
        :type name: str

        :param options: Object describing the extra options for a Synthetic suite.
        :type options: SyntheticsSuiteOptions

        :param public_id: The public ID for the test.
        :type public_id: str, optional

        :param tags: Array of tags attached to the suite.
        :type tags: [str], optional

        :param tests:
        :type tests: [SyntheticsSuiteTest]

        :param type: Type of the Synthetic suite, ``suite``.
        :type type: SyntheticsSuiteType
        """
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.message = message
        self_.name = name
        self_.options = options
        self_.tests = tests
        self_.type = type
