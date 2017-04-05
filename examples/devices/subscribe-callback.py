# ---------------------------------------------------------------------------
#   The confidential and proprietary information contained in this file may
#   only be used by a person authorised under and to the extent permitted
#   by a subsisting licensing agreement from ARM Limited or its affiliates.
#
#          (C) COPYRIGHT 2017 ARM Limited or its affiliates.
#              ALL RIGHTS RESERVED
#
#   This entire notice must be reproduced on all copies of this file
#   and copies of this file may only be made by a person if such person is
#   permitted to do so under the terms of a subsisting license agreement
#   from ARM Limited or its affiliates.
# --------------------------------------------------------------------------
"""Example showing basic usage of device resource subscriptions."""
from mbed_cloud.devices import DeviceAPI

BUTTON_RESOURCE = "/3200/0/5501"


def _current_val(value):
    # Print the current value
    print("Current value: %r" % (value,))


def _subscription_handler(value):
    _current_val(value)


def _main():
    api = DeviceAPI()
    api.start_long_polling()
    devices = api.list_connected_devices().as_list()
    if not devices:
        raise Exception("No connected devices registered. Aborting")

    # Synchronously get the initial/current value of the resource
    value = api.get_resource_value(devices[0].id, BUTTON_RESOURCE)
    _current_val(value)

    # Register a subscription for new values
    api.add_subscription_with_callback(devices[0].id, BUTTON_RESOURCE, _subscription_handler)

    # Run forever
    while True:
        pass


if __name__ == "__main__":
    _main()
