# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_test_config import SyntheticsTestConfig
        from datadog_api_client.v1.model.creator import Creator
        from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
        from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
        from datadog_api_client.v1.model.synthetics_step import SyntheticsStep
        from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
        from datadog_api_client.v1.model.synthetics_test_details_type import SyntheticsTestDetailsType

        return {
            "config": (SyntheticsTestConfig,),
            "creator": (Creator,),
            "locations": ([str],),
            "message": (str,),
            "monitor_id": (int,),
            "name": (str,),
            "options": (SyntheticsTestOptions,),
            "public_id": (str,),
            "status": (SyntheticsTestPauseStatus,),
            "steps": ([SyntheticsStep],),
            "subtype": (SyntheticsTestDetailsSubType,),
            "tags": ([str],),
            "type": (SyntheticsTestDetailsType,),
        }

    attribute_map = {
        "config": "config",
        "creator": "creator",
        "locations": "locations",
        "message": "message",
        "monitor_id": "monitor_id",
        "name": "name",
        "options": "options",
        "public_id": "public_id",
        "status": "status",
        "steps": "steps",
        "subtype": "subtype",
        "tags": "tags",
        "type": "type",
    }
    read_only_vars = {
        "creator",
        "monitor_id",
        "public_id",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing details about your Synthetic test.

        :param config: Configuration object for a Synthetic test.
        :type config: SyntheticsTestConfig, optional

        :param creator: Object describing the creator of the shared element.
        :type creator: Creator, optional

        :param locations: Array of locations used to run the test.
        :type locations: [str], optional

        :param message: Notification message associated with the test.
        :type message: str, optional

        :param monitor_id: The associated monitor ID.
        :type monitor_id: int, optional

        :param name: Name of the test.
        :type name: str, optional

        :param options: Object describing the extra options for a Synthetic test.
        :type options: SyntheticsTestOptions, optional

        :param public_id: The test public ID.
        :type public_id: str, optional

        :param status: Define whether you want to start ( ``live`` ) or pause ( ``paused`` ) a
            Synthetic test.
        :type status: SyntheticsTestPauseStatus, optional

        :param steps: For browser test, the steps of the test.
        :type steps: [SyntheticsStep], optional

        :param subtype: The subtype of the Synthetic API test, ``http`` , ``ssl`` , ``tcp`` ,
            ``dns`` , ``icmp`` , ``udp`` , ``websocket`` , ``grpc`` or ``multi``.
        :type subtype: SyntheticsTestDetailsSubType, optional

        :param tags: Array of tags attached to the test.
        :type tags: [str], optional

        :param type: Type of the Synthetic test, either ``api`` or ``browser``.
        :type type: SyntheticsTestDetailsType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestDetails, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
