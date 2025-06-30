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
    from datadog_api_client.v1.model.synthetics_mobile_test_config import SyntheticsMobileTestConfig
    from datadog_api_client.v1.model.synthetics_mobile_test_options import SyntheticsMobileTestOptions
    from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
    from datadog_api_client.v1.model.synthetics_mobile_step import SyntheticsMobileStep
    from datadog_api_client.v1.model.synthetics_mobile_test_type import SyntheticsMobileTestType


class SyntheticsMobileTest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_test_config import SyntheticsMobileTestConfig
        from datadog_api_client.v1.model.synthetics_mobile_test_options import SyntheticsMobileTestOptions
        from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
        from datadog_api_client.v1.model.synthetics_mobile_step import SyntheticsMobileStep
        from datadog_api_client.v1.model.synthetics_mobile_test_type import SyntheticsMobileTestType

        return {
            "config": (SyntheticsMobileTestConfig,),
            "device_ids": ([str],),
            "message": (str,),
            "monitor_id": (int,),
            "name": (str,),
            "options": (SyntheticsMobileTestOptions,),
            "public_id": (str,),
            "status": (SyntheticsTestPauseStatus,),
            "steps": ([SyntheticsMobileStep],),
            "tags": ([str],),
            "type": (SyntheticsMobileTestType,),
        }

    attribute_map = {
        "config": "config",
        "device_ids": "device_ids",
        "message": "message",
        "monitor_id": "monitor_id",
        "name": "name",
        "options": "options",
        "public_id": "public_id",
        "status": "status",
        "steps": "steps",
        "tags": "tags",
        "type": "type",
    }
    read_only_vars = {
        "monitor_id",
        "public_id",
    }

    def __init__(
        self_,
        config: SyntheticsMobileTestConfig,
        message: str,
        name: str,
        options: SyntheticsMobileTestOptions,
        type: SyntheticsMobileTestType,
        device_ids: Union[List[str], UnsetType] = unset,
        monitor_id: Union[int, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        status: Union[SyntheticsTestPauseStatus, UnsetType] = unset,
        steps: Union[List[SyntheticsMobileStep], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing details about a Synthetic mobile test.

        :param config: Configuration object for a Synthetic mobile test.
        :type config: SyntheticsMobileTestConfig

        :param device_ids: Array with the different device IDs used to run the test.
        :type device_ids: [str], optional

        :param message: Notification message associated with the test.
        :type message: str

        :param monitor_id: The associated monitor ID.
        :type monitor_id: int, optional

        :param name: Name of the test.
        :type name: str

        :param options: Object describing the extra options for a Synthetic test.
        :type options: SyntheticsMobileTestOptions

        :param public_id: The public ID of the test.
        :type public_id: str, optional

        :param status: Define whether you want to start ( ``live`` ) or pause ( ``paused`` ) a
            Synthetic test.
        :type status: SyntheticsTestPauseStatus, optional

        :param steps: Array of steps for the test.
        :type steps: [SyntheticsMobileStep], optional

        :param tags: Array of tags attached to the test.
        :type tags: [str], optional

        :param type: Type of the Synthetic test, ``mobile``.
        :type type: SyntheticsMobileTestType
        """
        if device_ids is not unset:
            kwargs["device_ids"] = device_ids
        if monitor_id is not unset:
            kwargs["monitor_id"] = monitor_id
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if status is not unset:
            kwargs["status"] = status
        if steps is not unset:
            kwargs["steps"] = steps
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.config = config
        self_.message = message
        self_.name = name
        self_.options = options
        self_.type = type
