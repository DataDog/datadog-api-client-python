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
    from datadog_api_client.v2.model.flaky_test_attributes import FlakyTestAttributes
    from datadog_api_client.v2.model.flaky_test_type import FlakyTestType


class FlakyTest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flaky_test_attributes import FlakyTestAttributes
        from datadog_api_client.v2.model.flaky_test_type import FlakyTestType

        return {
            "attributes": (FlakyTestAttributes,),
            "id": (str,),
            "type": (FlakyTestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[FlakyTestAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[FlakyTestType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A flaky test object.

        :param attributes: Attributes of a flaky test.
        :type attributes: FlakyTestAttributes, optional

        :param id: Test's ID. This ID is the hash of the test's Fully Qualified Name and Git repository ID. On the Test Runs UI it is the same as the ``test_fingerprint_fqn`` tag.
        :type id: str, optional

        :param type: The type of the flaky test from Flaky Test Management.
        :type type: FlakyTestType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
