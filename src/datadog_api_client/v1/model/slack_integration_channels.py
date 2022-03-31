# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.slack_integration_channel import SlackIntegrationChannel

    globals()["SlackIntegrationChannel"] = SlackIntegrationChannel


class SlackIntegrationChannels(ModelSimple):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "value": ([SlackIntegrationChannel],),
        }

    def __init__(self, *args, **kwargs):
        """
        A list of configured Slack channels.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: A list of configured Slack channels.
        :type value: [SlackIntegrationChannel]
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=self._path_to_item,
                valid_classes=(self.__class__,),
            )

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
